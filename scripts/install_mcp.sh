#!/bin/bash

# Script d'installation pour Garmin MCP Server

echo "Configuration du serveur MCP Garmin pour Claude Desktop..."

# Chemin vers le serveur MCP
MCP_SERVER_PATH="/Users/andre/Documents/_dev/garmin_mcp-master"
PYTHON_PATH="$MCP_SERVER_PATH/.venv/bin/python"
SERVER_SCRIPT="$MCP_SERVER_PATH/garmin_mcp_server.py"

# Vérifier que l'environnement virtuel existe
if [ ! -f "$PYTHON_PATH" ]; then
    echo "Erreur: L'environnement virtuel n'existe pas. Exécutez 'uv sync' d'abord."
    exit 1
fi

# Vérifier que le serveur existe
if [ ! -f "$SERVER_SCRIPT" ]; then
    echo "Erreur: Le script serveur n'existe pas: $SERVER_SCRIPT"
    exit 1
fi

# Configuration Claude Desktop
CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
CLAUDE_CONFIG_FILE="$CLAUDE_CONFIG_DIR/claude_desktop_config.json"

# Créer le répertoire de configuration si nécessaire
mkdir -p "$CLAUDE_CONFIG_DIR"

# Vérifier si le fichier de configuration existe
if [ ! -f "$CLAUDE_CONFIG_FILE" ]; then
    echo "Création du fichier de configuration Claude Desktop..."
    cat > "$CLAUDE_CONFIG_FILE" << EOF
{
  "mcpServers": {
    "garmin": {
      "command": "$PYTHON_PATH",
      "args": ["$SERVER_SCRIPT"],
      "env": {
        "PATH": "$MCP_SERVER_PATH/.venv/bin:\$PATH"
      }
    }
  }
}
EOF
else
    echo "Fichier de configuration existant détecté."
    echo "Vous devez ajouter manuellement la configuration Garmin MCP."
fi

echo "Configuration terminée !"
echo ""
echo "Configuration à ajouter dans Claude Desktop:"
echo "{"
echo "  \"mcpServers\": {"
echo "    \"garmin\": {"
echo "      \"command\": \"$PYTHON_PATH\","
echo "      \"args\": [\"$SERVER_SCRIPT\"],"
echo "      \"env\": {"
echo "        \"PATH\": \"$MCP_SERVER_PATH/.venv/bin:\$PATH\""
echo "      }"
echo "    }"
echo "  }"
echo "}"
echo ""
echo "Redémarrez Claude Desktop après avoir ajouté cette configuration."