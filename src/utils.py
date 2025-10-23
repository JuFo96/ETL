from pathlib import Path

import pandas as pd
from collections import OrderedDict, deque


def transform_column_names(file: Path, name_translation: dict):
    data = pd.read_csv(file)
    # print(data.columns)
    renamed_df = data.rename(columns=name_translation)

    return renamed_df


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

    print(topological_sort(graph))


if __name__ == "__main__":
    main()
