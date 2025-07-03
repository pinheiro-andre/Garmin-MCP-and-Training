#!/usr/bin/env python3

from garminconnect import Garmin
from dotenv import load_dotenv
import os

load_dotenv()
tokenstore = '~/.garminconnect'

print('🏋️ Création du PUSH Alan Ritchson avec la structure EXACTE de Sculpt...')

try:
    garmin = Garmin()
    garmin.login(tokenstore)
    
    # Exercices PUSH Alan Ritchson avec mapping Garmin validé
    push_exercises = [
        {
            'category': 'BENCH_PRESS',
            'exerciseName': 'BARBELL_BENCH_PRESS',
            'reps': 10,
            'rest': 180,  # 3 minutes pour le mouvement principal
            'sets': 5,
            'description': 'Développé couché barre - Mouvement principal lourd'
        },
        {
            'category': 'BENCH_PRESS',
            'exerciseName': 'INCLINE_DUMBBELL_BENCH_PRESS',
            'reps': 16,
            'rest': 90,  # 90 secondes
            'sets': 4,
            'description': 'Développé incliné haltères - Volume Ritchson'
        },
        {
            'category': 'FLY',
            'exerciseName': 'INCLINE_CABLE_FLY',
            'reps': 20,
            'rest': 90,
            'sets': 4,
            'description': 'Écarté câble incliné - Volume pectoraux'
        },
        {
            'category': 'SHOULDER_PRESS',
            'exerciseName': 'DUMBBELL_SHOULDER_PRESS',
            'reps': 18,
            'rest': 75,  # 75 secondes
            'sets': 4,
            'description': 'Développé militaire haltères - Épaules'
        },
        {
            'category': 'LATERAL_RAISE',
            'exerciseName': 'DUMBBELL_LATERAL_RAISE',
            'reps': 22,
            'rest': 75,
            'sets': 4,
            'description': 'Élévations latérales - Drop set dernière série'
        },
        {
            'category': 'TRICEP_EXTENSION',
            'exerciseName': 'TRICEP_PUSH_DOWN',
            'reps': 15,
            'rest': 60,  # Superset
            'sets': 4,
            'description': 'Extension triceps câble (Superset avec dips)'
        },
        {
            'category': 'DIP',
            'exerciseName': 'ASSISTED_DIP',
            'reps': 12,
            'rest': 60,
            'sets': 4,
            'description': 'Dips assistés (Superset)'
        },
        {
            'category': 'FLY',
            'exerciseName': 'CABLE_FLY',
            'reps': 15,  # "Au max" mais on met une base
            'rest': 45,
            'sets': 3,
            'description': 'Finition Ritchson - Écarté câble MAX REPS'
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
    
    # Construire les RepeatGroups selon la structure Sculpt (MÊME FORMAT)
    workout_steps = []
    step_order = 1
    
    for i, exercise in enumerate(push_exercises):
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
    push_workout = {
        'workoutName': 'PUSH Alan Ritchson - Sculpt Format',
        'description': 'Séance A - Pectoraux, Épaules, Triceps - Style Alan Ritchson - Durée 60-75 min',
        'sportType': {
            'sportTypeId': 9,
            'sportTypeKey': 'hiit'  # Même type que Sculpt
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
    print('📤 Upload du PUSH Alan Ritchson vers Garmin Connect...')
    
    result = garmin.upload_workout(push_workout)
    
    print('🎉 PUSH ALAN RITCHSON CRÉÉ AVEC SUCCÈS !')
    print('=' * 60)
    print(f'📋 Nom: PUSH Alan Ritchson - Sculpt Format')
    print(f'🎯 Type: HIIT (format compatible montre)')
    print(f'💪 Focus: Pectoraux, Épaules, Triceps')
    print(f'⏱️ Durée: 60-75 minutes')
    print()
    print('🏋️ Programme PUSH détaillé:')
    print('   1. 💪 DÉVELOPPÉ COUCHÉ BARRE - 5×10 reps (3min repos)')
    print('   2. 📈 DÉVELOPPÉ INCLINÉ HALTÈRES - 4×16 reps (90sec)')  
    print('   3. 🎯 ÉCARTÉ CÂBLE INCLINÉ - 4×20 reps (90sec)')
    print('   4. 🏆 DÉVELOPPÉ MILITAIRE HALTÈRES - 4×18 reps (75sec)')
    print('   5. 🔥 ÉLÉVATIONS LATÉRALES - 4×22 reps (75sec)')
    print('   6. ⚡ EXTENSION TRICEPS CÂBLE - 4×15 reps (60sec superset)')
    print('   7. ⚡ DIPS ASSISTÉS - 4×12 reps (60sec superset)')
    print('   8. 🎯 ÉCARTÉ CÂBLE FINITION - 3×15 reps MAX (45sec)')
    print('   9. 🎪 TIRAGE FACE - 2×25 reps (60sec)')
    print()
    print('✅ Compatible 100% avec votre montre Garmin !')
    print(f'🚀 Résultat API: {result}')
    print('📱 Synchronisez et cherchez "PUSH Alan Ritchson - Sculpt Format"')

except Exception as e:
    print(f'❌ Erreur: {e}')
    import traceback
    traceback.print_exc()
