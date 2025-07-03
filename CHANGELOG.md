# Changelog

Tous les changements notables de ce projet seront documentés dans ce fichier.

## [1.0.0] - 2025-07-03

### Ajouté
- **Serveur MCP Garmin** : Integration complète avec Claude Desktop
- **Entraînements prédéfinis** :
  - PUSH Complet - Alan Ritchson (75-90 min)
  - PUSH Sculpt Format (60-75 min)
  - REACHER - Dos & Biceps (60-75 min)
  - LEGS + ABS Ritchson (70-80 min)
  - Créateur Push Complet (personnalisable)
- **Table de correspondance exercices** : Mapping complet Garmin Connect
- **Scripts utilitaires** :
  - `connect_garmin.sh` : Test de connexion
  - `install_mcp.sh` : Installation MCP
  - `test_server.sh` : Test du serveur
  - `workout_tools_guide.sh` : Guide d'utilisation
- **Documentation complète** :
  - Guide de démarrage
  - Mapping des exercices
  - README détaillé
- **Bibliothèque python-garminconnect** : API wrapper intégré

### Fonctionnalités MCP
- `fetch_sleep_data()` : Données de sommeil
- `fetch_steps_data()` : Données de pas
- `fetch_activities_data()` : Activités récentes
- `fetch_heart_rate_data()` : Fréquence cardiaque
- `fetch_stress_data()` : Niveau de stress
- `fetch_body_battery_data()` : Batterie corporelle
- `fetch_user_summary()` : Résumé utilisateur
- `test_garmin_connection()` : Test de connexion
- `get_connection_status()` : État de la connexion

### Caractéristiques des entraînements
- **Format RepeatGroup** : Compatible montres Garmin
- **Guidage étape par étape** : Séries, répétitions, repos
- **Superset support** : Enchaînement d'exercices
- **Drop set** : Techniques d'intensité
- **RPE ciblé** : Intensité personnalisée
- **Exercices validés** : Mapping API Garmin testé

### Structure du projet
```
├── garmin_mcp_server.py          # Serveur MCP principal
├── training_examples/            # Entraînements prédéfinis
│   ├── push_complete_final.py
│   ├── push_sculpt_format.py
│   ├── reacher_dos_biceps.py
│   ├── legs_abs_ritchson.py
│   └── create_complete_push_workout.py
├── scripts/                      # Scripts utilitaires
│   ├── connect_garmin.sh
│   ├── install_mcp.sh
│   ├── test_server.sh
│   └── workout_tools_guide.sh
├── docs/                         # Documentation
│   ├── exercise_mapping.md
│   └── getting_started.md
├── python-garminconnect/        # Bibliothèque API
└── README.md                    # Documentation principale
```

### Programmes d'entraînement

#### PUSH Complet
- **Exercices** : 9 exercices + échauffement + cardio
- **Durée** : 75-90 minutes
- **Muscles** : Pectoraux, épaules, triceps
- **Spécial** : Superset triceps, drop set, finition Ritchson

#### PUSH Sculpt Format
- **Exercices** : 9 exercices optimisés
- **Durée** : 60-75 minutes
- **Muscles** : Pectoraux, épaules, triceps
- **Spécial** : Format RepeatGroup, compatible toutes montres

#### REACHER - Dos & Biceps
- **Exercices** : 9 exercices dos/biceps
- **Durée** : 60-75 minutes
- **Muscles** : Dos, biceps, arrière d'épaules
- **Spécial** : Superset biceps, tractions assistées

#### LEGS + ABS Ritchson
- **Exercices** : 14 exercices jambes/abdos
- **Durée** : 70-80 minutes
- **Muscles** : Jambes, fessiers, abdos
- **Spécial** : Core intensif 300+ répétitions

#### Créateur Push Complet
- **Exercices** : Générateur automatique
- **Durée** : 75-90 minutes
- **Muscles** : Pectoraux, épaules, triceps
- **Spécial** : Guidage détaillé, transitions

### Compatibilité
- **Montres Garmin** : Toutes avec support HIIT
- **Garmin Connect** : Application mobile/web
- **Claude Desktop** : Intégration MCP
- **Python** : 3.11+
- **Systèmes** : macOS, Linux, Windows

### Sécurité
- **Authentification** : Tokens OAuth sécurisés
- **Stockage local** : Pas de données cloud
- **Variables d'environnement** : Identifiants protégés
- **Rate limiting** : Respect des limites API

### Performance
- **Cache intelligent** : Tokens réutilisables
- **Optimisation API** : Appels minimisés
- **Gestion d'erreurs** : Retry automatique
- **Timeout** : Protection contre les blocages

### Tests
- **Script de test** : Validation complète
- **Connexion Garmin** : Test automatique
- **Serveur MCP** : Vérification fonctionnelle
- **Entraînements** : Validation format

### Dépendances
- `garminconnect>=0.2.25` : API Garmin Connect
- `mcp[cli]>=1.3.0` : Model Context Protocol
- `readchar>=4.2.1` : Interface utilisateur
- `python-dotenv` : Variables d'environnement
- `garth>=0.5.13` : Authentification Garmin

## Roadmap

### Version 1.1.0 (Planifiée)
- [ ] Entraînements cardio HIIT
- [ ] Programme full-body
- [ ] Exercices yoga/stretching
- [ ] Export données vers CSV
- [ ] Interface web de configuration

### Version 1.2.0 (Planifiée)
- [ ] Planification automatique
- [ ] Analyse performance
- [ ] Recommandations IA
- [ ] Synchronisation calendrier
- [ ] Support multi-utilisateurs

### Version 2.0.0 (Vision)
- [ ] Application mobile dédiée
- [ ] Communauté d'entraînements
- [ ] Coaching virtuel
- [ ] Intégration autres plateformes
- [ ] Marketplace d'entraînements

## Contributions

Contributions bienvenues ! Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les détails.

## Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- [cyberjunky](https://github.com/cyberjunky) pour python-garminconnect
- [dshvadskiy](https://github.com/dshvadskiy) pour l'inspiration garmin_mcp
- Alan Ritchson pour les programmes d'entraînement
- Communauté Garmin Connect
- Équipe Claude/Anthropic pour MCP

---

*Prêt à révolutionner vos entraînements !* 🏋️‍♂️💪🚀
