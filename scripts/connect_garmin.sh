#!/bin/bash

# Script d'aide pour la connexion Garmin MCP
# Usage: ./connect_garmin.sh

echo "🔗 Script de connexion Garmin MCP"
echo "=================================="

PROJECT_DIR="/Users/andre/Documents/_dev/garmin_mcp-master"
cd "$PROJECT_DIR"

# Vérifier le fichier .env
if ! grep -q "votre-email@example.com" .env 2>/dev/null; then
    echo "✅ Fichier .env configuré avec vos identifiants"
else
    echo "❌ ERREUR: Vous devez modifier le fichier .env avec vos vrais identifiants Garmin"
    echo "   Ouvrez: $PROJECT_DIR/.env"
    echo "   Remplacez 'votre-email@example.com' et 'votre-mot-de-passe'"
    exit 1
fi

echo ""
echo "🕒 Attente de 30 secondes pour éviter les limitations de débit Garmin..."
sleep 30

echo ""
echo "🔐 Tentative de connexion à Garmin Connect..."

# Essayer de générer les tokens
if timeout 60 .venv/bin/python example.py; then
    echo ""
    echo "✅ Connexion réussie ! Les tokens ont été générés."
    echo ""
    echo "📋 Configuration Claude Desktop terminée."
    echo "🔄 Redémarrez Claude Desktop pour activer le serveur MCP Garmin."
    echo ""
    echo "🎯 Fonctionnalités disponibles dans Claude:"
    echo "   • fetch_sleep_data - données de sommeil"
    echo "   • fetch_steps_data - données de pas"  
    echo "   • fetch_activities_data - données d'activités"
    echo "   • fetch_heart_rate_data - fréquence cardiaque"
    echo "   • fetch_stress_data - données de stress"
    echo "   • fetch_body_battery_data - batterie corporelle"
else
    echo ""
    echo "❌ Connexion échouée. Causes possibles:"
    echo "   • Identifiants incorrects dans le fichier .env"
    echo "   • Limitation de débit Garmin (attendre plus longtemps)"
    echo "   • Authentification à deux facteurs requise"
    echo "   • Problème de connexion internet"
    echo ""
    echo "💡 Solutions:"
    echo "   1. Vérifiez vos identifiants dans .env"
    echo "   2. Attendez 15-30 minutes supplémentaires"
    echo "   3. Réessayez plus tard"
fi