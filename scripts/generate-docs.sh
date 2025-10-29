#!/bin/sh
# Complete documentation generation pipeline
# Runs inside Alpine container with tbls installed

set -e

echo "📚 Database Documentation Generator"
echo "=================================="

# Install dependencies if not present
if ! command -v tbls > /dev/null; then
    echo "→ Installing tbls..."
    wget -q https://github.com/k1LoW/tbls/releases/latest/download/tbls_linux_amd64.tar.gz
    tar xzf tbls_linux_amd64.tar.gz
    mv tbls /usr/local/bin/
    rm tbls_linux_amd64.tar.gz
fi

# Configuration
DB_DSN="${DB_DSN:-mysql://root:password@mysql:3306/integrated_db}"
OUTPUT_DIR="/docs"
SCHEMA_NAME="database-schema"

# Wait for database to be ready
echo "→ Waiting for database..."
sleep 5

# Generate Mermaid diagram from database
echo "→ Generating Mermaid diagram from live database..."
tbls out -t mermaid -o "${OUTPUT_DIR}/${SCHEMA_NAME}.mmd" "$DB_DSN"

if [ $? -eq 0 ]; then
    echo "✅ Mermaid diagram generated: ${SCHEMA_NAME}.mmd"
else
    echo "❌ Failed to generate Mermaid diagram"
    exit 1
fi

# Generate full documentation
echo "→ Generating full documentation..."
tbls doc "$DB_DSN" "${OUTPUT_DIR}/db"

echo ""
echo "✅ Documentation generation complete!"
echo "   Outputs:"
echo "   - ${OUTPUT_DIR}/${SCHEMA_NAME}.mmd (Mermaid source)"
echo "   - ${OUTPUT_DIR}/db/ (Full HTML documentation)"
echo ""
echo "Next steps:"
echo "   1. Convert Mermaid to SVG:"
echo "      docker-compose run --rm mermaid -i ${SCHEMA_NAME}.mmd -o ${SCHEMA_NAME}.svg"
echo "   2. View documentation in ${OUTPUT_DIR}/db/README.md"