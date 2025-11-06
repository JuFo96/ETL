from collections import OrderedDict, deque
from pathlib import Path

import config


def get_table_dependencies(
    sql_procedure_path: Path, connection
) -> list[tuple[str, str]]:
    with open(file=sql_procedure_path, mode="r") as file:
        content = file.read()
    with connection.cursor() as cursor:
        cursor.execute(content)
        table_relations = cursor.fetchall()
    return table_relations


def build_dependency_graph(
    table_relations: list[tuple[str, str]],
) -> dict[str, set[str]]:
    table_set = set()

    for table, _ in table_relations:
        table_set.add(table)

    dependency_graph = {child_table: set() for child_table in table_set}

    for child_table, parent_table in table_relations:
        if parent_table is not None:
            dependency_graph[child_table].add(parent_table)

    return dependency_graph


def topological_sort(graph: dict[str, set[str]]) -> list[str]:
    """Topological sort based on Kahn's Algorithm.

    Args:
        Dictionary containing all tables with values given by their dependencies.

    Returns:
        List of tables names sorted in topological order.
    """
    results = []

    # Sorts dict by amount of parent tables, low to high
    sorted_graph = OrderedDict(sorted(graph.items(), key=lambda x: len(x[1])))

    queue = deque([node for node, edge in sorted_graph.items() if not edge])

    while queue:
        free_node = queue.popleft()
        results.append(free_node)

        # Remove nodes with no dependencies from all other nodes dependencies
        for node in sorted_graph:
            if free_node in sorted_graph[node]:
                sorted_graph[node].discard(free_node)

                # If node now has no dependencies, add it to the queue
                if not sorted_graph[node]:
                    queue.append(node)

    if len(results) != len(sorted_graph):
        remaining = [node for node in sorted_graph if node not in results]
        raise ValueError(f"Cyclic dependency detected between nodes: {remaining}")

    return results


def get_insert_order(sql_procedure_path: Path, connection) -> list[str]:
    table_relations = get_table_dependencies(
        sql_procedure_path=config.DEPENDENCIES_PROCEDURE, connection=connection
    )
    graph = build_dependency_graph(table_relations)
    sorted_table = topological_sort(graph)
    if not sorted_table:
        raise ValueError("Table insert order is empty: check get_depencies.sql")
    return sorted_table

def run_sql_schema(file, connection) -> None:
    """Reads a schema file and executes commands sequentially split by ;

    Args:
        Connection to a database
    """
    with open(file, 'r') as file:
        content = file.read()
    with connection.cursor() as cur:
        for statement in content.split(";"):
            statement = statement.strip()
            if statement:
                cur.execute(statement)
        connection.commit()


def main():
    graph = {
        "customers": {"orders"},
        "order_items": {"orders", "products"},
        "orders": {"customers", "stores"},
        "staffs": set(),
        "stores": set(),
        "brands": set(),
        "categories": set(),
        "products": {"brands", "categories"},
        "stocks": {"products", "stores"},
    }

    # print(topological_sort(graph))


if __name__ == "__main__":
    main()
