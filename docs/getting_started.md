# Guide de démarrage - Garmin MCP and Training

Ce guide vous aidera à configurer et utiliser le serveur MCP Garmin avec vos entraînements.

## 🚀 Installation rapide

### Prérequis
- Python 3.11 ou supérieur
- Compte Garmin Connect
- Claude Desktop (pour l'intégration MCP)
- UV (gestionnaire de paquets Python)

### 1. Cloner le repository
```bash
git clone https://github.com/pinheiro-andre/Garmin-MCP-and-Training.git
cd Garmin-MCP-and-Training
```

### 2. Installer les dépendances
```bash
uv sync
```

### 3. Configuration des identifiants
```bash
cp .env_template .env
```

Éditez le fichier `.env` avec vos identifiants Garmin :
```env
GARMIN_EMAIL='votre-email@example.com'
GARMIN_PASSWORD='votre-mot-de-passe'
GARMIN_TOKEN_STORE='~/.garminconnect'
GARMIN_TOKEN_STORE_BASE64='~/.garminconnect_base64'
```

### 4. Générer les tokens d'authentification
```bash
python example.py
```

### 5. Tester la connexion
```bash
./scripts/test_server.sh
```

## 🏋️ Utilisation des entraînements

### Entraînements disponibles

#### 1. PUSH Complet
```bash
python training_examples/push_complete_final.py
```
- **Durée**: 75-90 minutes
- **Muscles**: Pectoraux, épaules, triceps
- **Niveau**: Intermédiaire à avancé

#### 2. PUSH Sculpt Format
```bash
python training_examples/push_sculpt_format.py
```
- **Durée**: 60-75 minutes
- **Muscles**: Pectoraux, épaules, triceps
- **Niveau**: Tous niveaux
- **Spécial**: Optimisé pour montres Garmin

#### 3. REACHER - Dos & Biceps
```bash
python training_examples/reacher_dos_biceps.py
```
- **Durée**: 60-75 minutes
- **Muscles**: Dos, biceps, arrière d'épaules
- **Niveau**: Intermédiaire

#### 4. LEGS + ABS Ritchson
```bash
python training_examples/legs_abs_ritchson.py
```
- **Durée**: 70-80 minutes
- **Muscles**: Jambes, fessiers, abdos
- **Niveau**: Avancé
- **Spécial**: 300+ répétitions abdos

#### 5. Créateur Push Complet
```bash
python training_examples/create_complete_push_workout.py
```
- **Durée**: 75-90 minutes
- **Muscles**: Pectoraux, épaules, triceps
- **Niveau**: Personnalisable

## 🔧 Configuration Claude Desktop

### Installation du serveur MCP
```bash
./scripts/install_mcp.sh
```

### Configuration manuelle
Ajoutez dans votre fichier `claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "garmin": {
      "command": "/path/to/your/project/.venv/bin/python",
      "args": ["/path/to/your/project/garmin_mcp_server.py"],
      "env": {
        "PATH": "/path/to/your/project/.venv/bin:$PATH"
      }
    }
  }
}
```

### Redémarrer Claude Desktop
Après avoir ajouté la configuration, redémarrez Claude Desktop.

## 📱 Utilisation sur votre montre Garmin

### 1. Synchronisation
- Ouvrez l'application Garmin Connect
- Synchronisez votre montre
- Les entraînements apparaîtront dans "Entraînements"

### 2. Lancement d'un entraînement
- Sur votre montre : **Menu > Entraînements > Mes entraînements**
- Sélectionnez l'entraînement créé
- Appuyez sur **Démarrer**

### 3. Pendant l'entraînement
- **Navigation** : Boutons haut/bas
- **Validation** : Bouton start/stop
- **Pause** : Bouton back
- **Repos** : Décompte automatique

## 🎯 Fonctionnalités MCP dans Claude

### Commandes disponibles

#### Données de santé
```
- fetch_sleep_data(date)
- fetch_steps_data(date_from, date_to)
- fetch_heart_rate_data(date)
- fetch_stress_data(date)
- fetch_body_battery_data(start_date, end_date)
```

#### Activités
```
- fetch_activities_data(num_activities)
- fetch_user_summary(date)
```

#### Connexion
```
- test_garmin_connection()
- get_connection_status()
```

### Exemples d'utilisation
```
# Dans Claude Desktop
"Montre-moi mes données de sommeil d'hier"
"Combien de pas ai-je fait cette semaine ?"
"Quel est mon niveau de stress aujourd'hui ?"
"Quelles sont mes dernières activités ?"
```

## 🛠️ Dépannage

### Problèmes courants

#### Erreur d'authentification
```bash
# Vérifiez vos identifiants
cat .env

# Régénérez les tokens
python example.py
```

#### Erreur de connexion
```bash
# Testez la connexion
./scripts/connect_garmin.sh

# Attendez 15-30 minutes entre les tentatives
```

#### Serveur MCP non détecté
```bash
# Vérifiez la configuration
./scripts/install_mcp.sh

# Redémarrez Claude Desktop
```

#### Entraînement non visible sur la montre
1. Vérifiez que l'upload s'est bien passé
2. Synchronisez manuellement la montre
3. Attendez 5-10 minutes
4. Redémarrez la montre si nécessaire

### Logs et débogage

#### Activer les logs détaillés
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Vérifier l'état du serveur
```bash
./scripts/test_server.sh
```

## 📊 Personnalisation des entraînements

### Modifier un entraînement existant
1. Copiez un fichier d'entraînement
2. Modifiez les exercices, séries, répétitions
3. Changez le nom de l'entraînement
4. Exécutez le script

### Créer un nouvel entraînement
```python
# Exemple de structure
exercises = [
    {
        'category': 'BENCH_PRESS',
        'exerciseName': 'BARBELL_BENCH_PRESS',
        'reps': 10,
        'rest': 120,
        'sets': 4,
        'description': 'Développé couché barre'
    }
]
```

### Conseils pour les débutants
- Commencez avec des RPE 6-7
- Augmentez progressivement les charges
- Respectez les temps de repos
- Écoutez votre corps

## 🆘 Support

### Ressources utiles
- [Documentation API Garmin](https://developer.garmin.com/)
- [Issues GitHub](https://github.com/pinheiro-andre/Garmin-MCP-and-Training/issues)
- [Claude Desktop](https://claude.ai/desktop)

### Obtenir de l'aide
1. Consultez la documentation
2. Vérifiez les issues existantes
3. Créez une nouvelle issue avec :
   - Description du problème
   - Logs d'erreur
   - Configuration système
   - Étapes pour reproduire

---

*Prêt à transformer vos entraînements avec Garmin MCP !* 🚀💪
