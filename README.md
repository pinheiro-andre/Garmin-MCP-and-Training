# Garmin MCP and Training

A comprehensive Model Context Protocol (MCP) server for interacting with the Garmin Connect API, enhanced with training examples and workout templates for strength training programs.

## Overview

This project provides a server for interacting with the Garmin Connect API, allowing users to manage their Garmin data, including workouts, health metrics, and more. It includes practical examples of strength training workouts and a correspondence table to facilitate training creation.

## Features

- **MCP Server Integration**: Full Model Context Protocol server for seamless integration with Claude Desktop
- **Garmin Connect API**: Direct interaction with Garmin Connect using the python-garminconnect package
- **Training Examples**: Pre-built workout templates for strength training programs
- **Exercise Database**: Comprehensive exercise library with Garmin-compatible formatting
- **Workout Templates**: Ready-to-use training sessions for various muscle groups

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (install via `uv sync`)
- A Garmin Connect account
- Uses [Python Garmin Connect Package](https://github.com/cyberjunky/python-garminconnect) to interact with Garmin Connect API

### Environment Setup

1. Create a `.env` file in the root directory from the `.env_template` file with the following variables:
   ```
   GARMIN_EMAIL=your_email@example.com
   GARMIN_PASSWORD=your_password
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Generate token for Garmin Connect:
   ```bash
   python example.py
   ```

### Running the Server

#### Use MCP Inspector
```bash
mcp dev garmin_mcp_server.py
```

#### Register MCP Server in Claude Desktop
```bash
mcp install garmin_mcp_server.py
```

## Training Examples

This repository includes several pre-built training sessions designed for strength training programs:

### Available Workouts

1. **🏋️ Push Complete** (`push_complete_final.py`)
   - Complete push day workout
   - Targets: Chest, Shoulders, Triceps
   - Includes compound and isolation exercises

2. **🏋️ Push Sculpt Format** (`push_sculpt_format.py`)
   - Push workout formatted for Sculpt program
   - Based on Alan Ritchson's training structure
   - Optimized for muscle building

3. **🎯 Reacher - Back & Biceps** (`reacher_dos_biceps.py`)
   - Pull-focused workout session
   - Targets: Back, Biceps, Rear Delts
   - Comprehensive pulling movements

4. **🦵 Legs & Abs - Ritchson** (`legs_abs_ritchson.py`)
   - Lower body and core training
   - Targets: Legs, Glutes, Abs
   - High-intensity leg training

5. **🏗️ Complete Push Workout Creator** (`create_complete_push_workout.py`)
   - Automated push workout generator
   - Customizable rep ranges and rest periods
   - Military press, bench press, and accessories

## Exercise Library & Correspondence Table

The repository includes a comprehensive exercise database with Garmin-compatible formatting. Each exercise includes:

- Exercise name and description
- Target muscle groups
- Rep ranges and rest periods
- Proper progression schemes
- Garmin Connect API formatting

### Exercise Categories

- **Push Movements**: Bench press, shoulder press, tricep exercises
- **Pull Movements**: Rows, pull-ups, bicep exercises  
- **Leg Movements**: Squats, lunges, leg press variations
- **Core & Abs**: Planks, crunches, rotational movements
- **Cardio Integration**: HIIT protocols and conditioning

## File Structure

```
garmin_mcp/
├── garmin_mcp_server.py          # Main MCP server
├── garmin_mcp_server_fixed.py    # Enhanced server version
├── garmin_mcp_server_safe.py     # Safe mode server
├── example.py                    # Basic usage example
├── training_examples/
│   ├── push_complete_final.py    # Complete push workout
│   ├── push_sculpt_format.py     # Sculpt-formatted push
│   ├── reacher_dos_biceps.py     # Back & biceps session
│   ├── legs_abs_ritchson.py      # Legs & abs workout
│   └── create_complete_push_workout.py # Push generator
├── examples_garmin_data/         # Sample Garmin data
├── scripts/
│   ├── connect_garmin.sh         # Connection script
│   ├── install_mcp.sh            # MCP installation
│   ├── test_server.sh            # Server testing
│   └── workout_tools_guide.sh    # Workout tools guide
└── python-garminconnect/        # Garmin Connect API library
```

## Usage Examples

### Creating a Custom Workout

```python
from garmin_mcp_server import GarminMCPServer

# Initialize server
server = GarminMCPServer()

# Create custom workout
workout = server.create_workout({
    'name': 'Custom Push Day',
    'exercises': [
        {'name': 'Bench Press', 'sets': 4, 'reps': '8-12'},
        {'name': 'Shoulder Press', 'sets': 3, 'reps': '10-15'},
        {'name': 'Tricep Dips', 'sets': 3, 'reps': '12-15'}
    ]
})

# Push to Garmin Connect
server.upload_workout(workout)
```

### Retrieving Training Data

```python
# Get recent activities
activities = server.get_activities(limit=10)

# Get body composition
body_data = server.get_body_composition()

# Get heart rate data
hr_data = server.get_heart_rate_data('2024-01-01')
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

- Built with [python-garminconnect](https://github.com/cyberjunky/python-garminconnect)
- Inspired by [garmin_mcp](https://github.com/dshvadskiy/garmin_mcp)
- Training programs based on proven strength training methodologies

## Support

For issues and questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Include your environment setup and error messages

---

*Ready to take your Garmin training to the next level!* 🏋️‍♂️💪
