#!/bin/bash

# Script de test pour le serveur MCP Garmin

echo "🧪 Test du serveur MCP Garmin"
echo "============================"

PROJECT_DIR="/Users/andre/Documents/_dev/garmin_mcp-master"
cd "$PROJECT_DIR"

# Vérifier que l'environnement virtuel existe
if [ ! -f ".venv/bin/python" ]; then
    echo "❌ Erreur: L'environnement virtuel n'existe pas."
    echo "   Exécutez 'uv sync' pour l'installer."
    exit 1
fi

# Vérifier que le serveur existe
if [ ! -f "garmin_mcp_server.py" ]; then
    echo "❌ Erreur: Le serveur MCP n'existe pas."
    exit 1
fi

# Vérifier le fichier .env
if [ ! -f ".env" ]; then
    echo "❌ Erreur: Le fichier .env n'existe pas."
    echo "   Copiez .env_template vers .env et configurez vos identifiants."
    exit 1
fi

echo "✅ Fichiers requis présents"
echo ""
echo "🔧 Test de l'environnement Python..."

# Tester l'importation des modules
if .venv/bin/python -c "from garminconnect import Garmin; from mcp.server.fastmcp import FastMCP; print('✅ Modules importés avec succès')"; then
    echo "✅ Environnement Python configuré correctement"
else
    echo "❌ Erreur: Problème avec l'environnement Python"
    echo "   Exécutez 'uv sync' pour réinstaller les dépendances."
    exit 1
fi

echo ""
echo "🔌 Test de connexion Garmin..."

# Tester la connexion (timeout de 30 secondes)
if timeout 30 .venv/bin/python -c "from garmin_mcp_server import init_api; import os; from dotenv import load_dotenv; load_dotenv(); api = init_api(os.getenv('GARMIN_EMAIL'), os.getenv('GARMIN_PASSWORD')); print('✅ Connexion Garmin réussie' if api else '❌ Connexion Garmin échouée')"; then
    echo "✅ Test de connexion terminé"
else
    echo "⚠️ Test de connexion interrompu (timeout ou erreur)"
fi

echo ""
echo "🚀 Test du serveur MCP..."
echo "   Démarrage du serveur en mode test (Ctrl+C pour arrêter)..."
echo ""

# Démarrer le serveur en mode test
.venv/bin/python garmin_mcp_server.py

echo ""
echo "✅ Test terminé"