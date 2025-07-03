#!/usr/bin/env python3

from garminconnect import Garmin
from dotenv import load_dotenv
import os

load_dotenv()
tokenstore = '~/.garminconnect'

print('🎯 Création de la SÉANCE B - Reacher (Dos, Biceps, Arrière d\'épaule)...')

try:
    garmin = Garmin()
    garmin.login(tokenstore)
    
    # Exercices SÉANCE B - Reacher avec mapping Garmin validé
    reacher_exercises = [
        {
            'category': 'ROW',
            'exerciseName': 'BENT_OVER_ROW_WITH_BARBELL',  # Alternative au BARBELL_BENT_OVER_ROW
            'reps': 10,
            'rest': 180,  # 3 minutes
            'sets': 5,
            'description': 'Rowing barre - Mouvement principal lourd'
        },
        {
            'category': 'PULL_UP', 
            'exerciseName': 'WIDE_GRIP_LAT_PULLDOWN',
            'reps': 16,
            'rest': 90,  # 90 secondes
            'sets': 4,
            'description': 'Tirage vertical prise large - Volume Ritchson'
        },
        {
            'category': 'ROW',
            'exerciseName': 'SEATED_CABLE_ROW', 
            'reps': 20,
            'rest': 90,
            'sets': 4,
            'description': 'Tirage horizontal câble - Volume dos largeur'
        },
        {
            'category': 'ROW',
            'exerciseName': 'T_BAR_ROW',
            'reps': 18,
            'rest': 75,  # 75 secondes
            'sets': 4,
            'description': 'Rowing T-bar - Dos épaisseur'
        },
        {
            'category': 'SHRUG',
            'exerciseName': 'DUMBBELL_SHRUG',
            'reps': 22,
            'rest': 75,
            'sets': 4,
            'description': 'Shrugs haltères - Trapèzes'
        },
        {
            'category': 'CURL',
            'exerciseName': 'REVERSE_EZ_BAR_CURL',  # Plus proche de l'EZ bar curl
            'reps': 15,
            'rest': 60,  # Superset
            'sets': 4,
            'description': 'Curl barre EZ (Superset avec marteau)'
        },
        {
            'category': 'CURL', 
            'exerciseName': 'CABLE_HAMMER_CURL',  # Meilleure option que la version complexe
            'reps': 18,
            'rest': 60,
            'sets': 4,
            'description': 'Curl marteau haltères (Superset)'
        },
        {
            'category': 'PULL_UP',
            'exerciseName': 'BAND_ASSISTED_PULL_UP',
            'reps': 12,  # "Au max" mais on met une base
            'rest': 45,
            'sets': 3,
            'description': 'Finition Ritchson - Tractions assistées MAX REPS'
        },
        {
            'category': 'ROW',
            'exerciseName': 'FACE_PULL',
            'reps': 25,
            'rest': 60,
            'sets': 2,
            'description': 'Tirage face - Arrière d\'épaules'
        }
    ]
    
    # Construire les RepeatGroups selon la structure Sculpt (MÊME FORMAT QUE PUSH)
    workout_steps = []
    step_order = 1
    
    for i, exercise in enumerate(reacher_exercises):
        # Créer un RepeatGroup pour chaque exercice
        repeat_group = {
            'type': 'RepeatGroupDTO',
            'stepOrder': step_order,
            'stepType': {
                'stepTypeId': 6,
                'stepTypeKey': 'repeat'
            },
            'childStepId': i + 1,
            'numberOfIterations': exercise['sets'],
            'workoutSteps': [
                # Étape exercice
                {
                    'type': 'ExecutableStepDTO',
                    'stepOrder': step_order + 1,
                    'stepType': {
                        'stepTypeId': 3,
                        'stepTypeKey': 'interval'
                    },
                    'childStepId': i + 1,
                    'description': exercise['description'],
                    'endCondition': {
                        'conditionTypeId': 10,
                        'conditionTypeKey': 'reps'
                    },
                    'endConditionValue': float(exercise['reps']),
                    'targetType': {
                        'workoutTargetTypeId': 1,
                        'workoutTargetTypeKey': 'no.target'
                    },
                    'category': exercise['category'],
                    'exerciseName': exercise['exerciseName'],
                    'strokeType': {
                        'strokeTypeId': 0,
                        'strokeTypeKey': None
                    },
                    'equipmentType': {
                        'equipmentTypeId': 0,
                        'equipmentTypeKey': None
                    }
                },
                # Étape repos
                {
                    'type': 'ExecutableStepDTO',
                    'stepOrder': step_order + 2,
                    'stepType': {
                        'stepTypeId': 5,
                        'stepTypeKey': 'rest'
                    },
                    'childStepId': i + 1,
                    'endCondition': {
                        'conditionTypeId': 2,
                        'conditionTypeKey': 'time'
                    },
                    'endConditionValue': float(exercise['rest']),
                    'targetType': {
                        'workoutTargetTypeId': 1,
                        'workoutTargetTypeKey': 'no.target'
                    },
                    'strokeType': {
                        'strokeTypeId': 0,
                        'strokeTypeKey': None
                    },
                    'equipmentType': {
                        'equipmentTypeId': 0,
                        'equipmentTypeKey': None
                    }
                }
            ],
            'endConditionValue': float(exercise['sets']),
            'endCondition': {
                'conditionTypeId': 7,
                'conditionTypeKey': 'iterations'
            },
            'skipLastRestStep': False,
            'smartRepeat': False
        }
        
        workout_steps.append(repeat_group)
        step_order += 3  # Incrémenter pour le prochain groupe
    
    # Construire l'entraînement complet avec la structure Sculpt
    reacher_workout = {
        'workoutName': 'REACHER - Dos Biceps - Alan Ritchson',
        'description': 'Séance B - Dos, Biceps, Arrière d\'épaule - Style Alan Ritchson - Durée 60-75 min',
        'sportType': {
            'sportTypeId': 9,
            'sportTypeKey': 'hiit'  # Même type que Sculpt et PUSH
        },
        'estimatedDurationInSecs': 0,
        'estimatedDistanceInMeters': 0.0,
        'workoutSegments': [
            {
                'segmentOrder': 1,
                'sportType': {
                    'sportTypeId': 9,
                    'sportTypeKey': 'hiit'
                },
                'workoutSteps': workout_steps
            }
        ]
    }
    
    print(f'📊 Entraînement généré avec {len(workout_steps)} exercices')
    print('📤 Upload de la SÉANCE B - Reacher vers Garmin Connect...')
    
    result = garmin.upload_workout(reacher_workout)
    
    print('🎉 SÉANCE B - REACHER CRÉÉE AVEC SUCCÈS !')
    print('=' * 60)
    print(f'📋 Nom: REACHER - Dos Biceps - Alan Ritchson')
    print(f'🎯 Type: HIIT (format compatible montre)')
    print(f'💪 Focus: Dos, Biceps, Arrière d\'épaules')
    print(f'⏱️ Durée: 60-75 minutes')
    print()
    print('🏋️ Programme SÉANCE B détaillé:')
    print('   1. 💪 ROWING BARRE - 5×10 reps (3min repos)')
    print('   2. 📈 TIRAGE VERTICAL LARGE - 4×16 reps (90sec)')  
    print('   3. 🎯 TIRAGE HORIZONTAL CÂBLE - 4×20 reps (90sec)')
    print('   4. 🏆 ROWING T-BAR - 4×18 reps (75sec)')
    print('   5. 🔥 SHRUGS HALTÈRES - 4×22 reps (75sec)')
    print('   6. ⚡ CURL BARRE EZ - 4×15 reps (60sec superset)')
    print('   7. ⚡ CURL MARTEAU - 4×18 reps (60sec superset)')
    print('   8. 🎯 TRACTIONS ASSISTÉES - 3×12 reps MAX (45sec)')
    print('   9. 🎪 TIRAGE FACE - 2×25 reps (60sec)')
    print()
    print('✅ Compatible 100% avec votre montre Garmin !')
    print(f'🚀 Résultat API: {result}')
    print('📱 Synchronisez et cherchez "REACHER - Dos Biceps - Alan Ritchson"')

except Exception as e:
    print(f'❌ Erreur: {e}')
    import traceback
    traceback.print_exc()
