# Table de correspondance des exercices Garmin

Ce document répertorie les exercices disponibles dans l'API Garmin Connect et leur mapping pour créer des entraînements.

## Exercices Pectoraux (PUSH)

### Développé couché
```python
{
    'category': 'BENCH_PRESS',
    'exerciseName': 'BARBELL_BENCH_PRESS',
    'description': 'Développé couché barre'
}
```

### Développé incliné
```python
{
    'category': 'BENCH_PRESS',
    'exerciseName': 'INCLINE_DUMBBELL_BENCH_PRESS',
    'description': 'Développé incliné haltères'
}
```

### Écartés
```python
{
    'category': 'FLY',
    'exerciseName': 'INCLINE_CABLE_FLY',
    'description': 'Écarté câble incliné'
}
```

```python
{
    'category': 'FLY',
    'exerciseName': 'CABLE_FLY',
    'description': 'Écarté câble horizontal'
}
```

### Dips
```python
{
    'category': 'DIP',
    'exerciseName': 'ASSISTED_DIP',
    'description': 'Dips assistés'
}
```

## Exercices Épaules

### Développé militaire
```python
{
    'category': 'SHOULDER_PRESS',
    'exerciseName': 'DUMBBELL_SHOULDER_PRESS',
    'description': 'Développé militaire haltères'
}
```

### Élévations latérales
```python
{
    'category': 'LATERAL_RAISE',
    'exerciseName': 'DUMBBELL_LATERAL_RAISE',
    'description': 'Élévations latérales haltères'
}
```

### Tirage face (arrière d'épaules)
```python
{
    'category': 'ROW',
    'exerciseName': 'FACE_PULL',
    'description': 'Tirage face - arrière d\'épaules'
}
```

## Exercices Triceps

### Extensions triceps
```python
{
    'category': 'TRICEP_EXTENSION',
    'exerciseName': 'TRICEP_PUSH_DOWN',
    'description': 'Extension triceps câble'
}
```

### Dips pour triceps
```python
{
    'category': 'DIP',
    'exerciseName': 'ASSISTED_DIP',
    'description': 'Dips assistés - focus triceps'
}
```

## Exercices Dos (PULL)

### Rowing
```python
{
    'category': 'ROW',
    'exerciseName': 'BENT_OVER_ROW_WITH_BARBELL',
    'description': 'Rowing barre penché'
}
```

```python
{
    'category': 'ROW',
    'exerciseName': 'SEATED_CABLE_ROW',
    'description': 'Tirage horizontal câble assis'
}
```

```python
{
    'category': 'ROW',
    'exerciseName': 'T_BAR_ROW',
    'description': 'Rowing T-bar'
}
```

### Tirage vertical
```python
{
    'category': 'PULL_UP',
    'exerciseName': 'WIDE_GRIP_LAT_PULLDOWN',
    'description': 'Tirage vertical prise large'
}
```

### Tractions
```python
{
    'category': 'PULL_UP',
    'exerciseName': 'BAND_ASSISTED_PULL_UP',
    'description': 'Tractions assistées'
}
```

### Shrugs (trapèzes)
```python
{
    'category': 'SHRUG',
    'exerciseName': 'DUMBBELL_SHRUG',
    'description': 'Shrugs haltères'
}
```

## Exercices Biceps

### Curl barre
```python
{
    'category': 'CURL',
    'exerciseName': 'REVERSE_EZ_BAR_CURL',
    'description': 'Curl barre EZ'
}
```

### Curl marteau
```python
{
    'category': 'CURL',
    'exerciseName': 'CABLE_HAMMER_CURL',
    'description': 'Curl marteau câble'
}
```

## Exercices Jambes (LEGS)

### Squats
```python
{
    'category': 'SQUAT',
    'exerciseName': 'BARBELL_BACK_SQUAT',
    'description': 'Squat barre arrière'
}
```

```python
{
    'category': 'SQUAT',
    'exerciseName': 'LEG_PRESS',
    'description': 'Presse à cuisses'
}
```

### Fentes
```python
{
    'category': 'LUNGE',
    'exerciseName': 'BARBELL_BULGARIAN_SPLIT_SQUAT',
    'description': 'Fentes bulgares'
}
```

### Soulevé de terre
```python
{
    'category': 'DEADLIFT',
    'exerciseName': 'ROMANIAN_DEADLIFT',
    'description': 'Soulevé de terre roumain'
}
```

### Isolation jambes
```python
{
    'category': 'BANDED_EXERCISES',
    'exerciseName': 'LEG_EXTENSION',
    'description': 'Extension quadriceps'
}
```

```python
{
    'category': 'LEG_CURL',
    'exerciseName': 'GOOD_MORNING',
    'description': 'Good morning (alternative curl ischio)'
}
```

### Mollets
```python
{
    'category': 'CALF_RAISE',
    'exerciseName': 'STANDING_CALF_RAISE',
    'description': 'Mollets debout'
}
```

```python
{
    'category': 'CALF_RAISE',
    'exerciseName': 'SEATED_CALF_RAISE',
    'description': 'Mollets assis'
}
```

## Exercices Abdominaux (CORE)

### Relevés de jambes
```python
{
    'category': 'LEG_RAISE',
    'exerciseName': 'HANGING_LEG_RAISE',
    'description': 'Relevés de jambes suspendus'
}
```

### Crunchs
```python
{
    'category': 'CRUNCH',
    'exerciseName': 'CRUNCH',
    'description': 'Crunchs classiques'
}
```

### Rotations
```python
{
    'category': 'CORE',
    'exerciseName': 'RUSSIAN_TWIST',
    'description': 'Russian twists'
}
```

### Gainage
```python
{
    'category': 'PLANK',
    'exerciseName': 'PLANK',
    'description': 'Planche gainage'
}
```

### Stabilité
```python
{
    'category': 'HIP_STABILITY',
    'exerciseName': 'DEAD_BUG',
    'description': 'Dead bug - stabilité core'
}
```

## Structure des entraînements

### Format RepeatGroup (Style Sculpt)
```python
repeat_group = {
    'type': 'RepeatGroupDTO',
    'stepOrder': step_order,
    'stepType': {
        'stepTypeId': 6,
        'stepTypeKey': 'repeat'
    },
    'childStepId': exercise_id,
    'numberOfIterations': sets,
    'workoutSteps': [
        # Étape exercice
        {
            'type': 'ExecutableStepDTO',
            'stepOrder': step_order + 1,
            'stepType': {
                'stepTypeId': 3,
                'stepTypeKey': 'interval'
            },
            'description': exercise_description,
            'endCondition': {
                'conditionTypeId': 10,
                'conditionTypeKey': 'reps'
            },
            'endConditionValue': float(reps),
            'targetType': {
                'workoutTargetTypeId': 1,
                'workoutTargetTypeKey': 'no.target'
            },
            'category': exercise_category,
            'exerciseName': exercise_name
        },
        # Étape repos
        {
            'type': 'ExecutableStepDTO',
            'stepOrder': step_order + 2,
            'stepType': {
                'stepTypeId': 5,
                'stepTypeKey': 'rest'
            },
            'endCondition': {
                'conditionTypeId': 2,
                'conditionTypeKey': 'time'
            },
            'endConditionValue': float(rest_seconds)
        }
    ]
}
```

### Types d'entraînement
```python
# Pour entraînements HIIT (compatible montres)
'sportType': {
    'sportTypeId': 9,
    'sportTypeKey': 'hiit'
}

# Pour entraînements musculation
'sportType': {
    'sportTypeId': 13,
    'sportTypeKey': 'strength_training'
}
```

## Conseils d'utilisation

### Répétitions et séries
- **Hypertrophie**: 3-4 séries × 8-15 répétitions
- **Force**: 4-5 séries × 3-8 répétitions  
- **Endurance**: 2-3 séries × 15-25 répétitions

### Temps de repos
- **Exercices lourds**: 2-3 minutes
- **Exercices volume**: 60-90 secondes
- **Exercices isolation**: 45-60 secondes
- **Superset**: 30-45 secondes entre exercices

### Progression
- **Débutant**: RPE 6-7
- **Intermédiaire**: RPE 7-8
- **Avancé**: RPE 8-9

### Techniques d'intensité
- **Drop set**: Réduction du poids de 20-30%
- **Rest-pause**: Pause 10-15 secondes entre mini-séries
- **Superset**: Enchaînement de 2 exercices
- **Finition**: Dernière série à l'échec

## Correspondance avec les programmes

### Programme Alan Ritchson
- **PUSH**: Pectoraux, épaules, triceps
- **PULL**: Dos, biceps, arrière d'épaules
- **LEGS**: Jambes, fessiers, mollets, abdos

### Volume recommandé
- **PUSH**: 16-20 séries par semaine
- **PULL**: 14-18 séries par semaine
- **LEGS**: 20-24 séries par semaine
- **CORE**: 10-15 séries par semaine

---

*Cette table de correspondance est optimisée pour les montres Garmin et l'API Garmin Connect. Tous les exercices ont été testés et validés.*
