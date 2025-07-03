# Python: Garmin Connect

```bash
$ ./example.py
*** Garmin Connect API Demo by cyberjunky ***

Trying to login to Garmin Connect using token data from directory '~/.garminconnect'...

1 -- Get full name
2 -- Get unit system
3 -- Get activity data for '2024-11-10'
4 -- Get activity data for '2024-11-10' (compatible with garminconnect-ha)
5 -- Get body composition data for '2024-11-10' (compatible with garminconnect-ha)
6 -- Get body composition data for from '2024-11-03' to '2024-11-10' (to be compatible with garminconnect-ha)
7 -- Get stats and body composition data for '2024-11-10'
8 -- Get steps data for '2024-11-10'
9 -- Get heart rate data for '2024-11-10'
0 -- Get training readiness data for '2024-11-10'
- -- Get daily step data for '2024-11-03' to '2024-11-10'
/ -- Get body battery data for '2024-11-03' to '2024-11-10'
! -- Get floors data for '2024-11-03'
? -- Get blood pressure data for '2024-11-03' to '2024-11-10'
. -- Get training status data for '2024-11-10'
a -- Get resting heart rate data for '2024-11-10'
b -- Get hydration data for '2024-11-10'
c -- Get sleep data for '2024-11-10'
d -- Get stress data for '2024-11-10'
e -- Get respiration data for '2024-11-10'
f -- Get SpO2 data for '2024-11-10'
g -- Get max metric data (like vo2MaxValue and fitnessAge) for '2024-11-10'
```

## Python 3 API wrapper for Garmin Connect

This is a Python 3 API wrapper for Garmin Connect to get your statistics.

## Installation

```bash
pip install garminconnect
```

## Usage

```python
from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

# Initialize Garmin API
api = Garmin(email, password)
api.login()

# Get full name
print(api.get_full_name())

# Get unit system
print(api.get_unit_system())

# Get activity data
print(api.get_stats_and_body('2024-01-01'))

# Get steps data
print(api.get_steps_data('2024-01-01', '2024-01-31'))

# Get heart rate data
print(api.get_heart_rate('2024-01-01'))

# Get sleep data
print(api.get_sleep_data('2024-01-01'))

# Get stress data
print(api.get_stress_data('2024-01-01'))

# Get body battery data
print(api.get_body_battery('2024-01-01', '2024-01-31'))

# Get activities
print(api.get_activities(0, 10))
```

## Available Methods

### Authentication
- `login()` - Login to Garmin Connect
- `logout()` - Logout from Garmin Connect

### Profile Information
- `get_full_name()` - Get full name
- `get_unit_system()` - Get unit system
- `get_user_profile()` - Get user profile
- `get_user_settings()` - Get user settings

### Activity Data
- `get_activities(start, limit)` - Get activity data
- `get_activity_data(activity_id)` - Get specific activity data
- `get_activity_splits(activity_id)` - Get activity splits
- `get_activity_details(activity_id)` - Get activity details

### Health Metrics
- `get_stats_and_body(date)` - Get stats and body composition
- `get_steps_data(start_date, end_date)` - Get steps data
- `get_heart_rate(date)` - Get heart rate data
- `get_sleep_data(date)` - Get sleep data
- `get_stress_data(date)` - Get stress data
- `get_body_battery(start_date, end_date)` - Get body battery data
- `get_training_readiness(date)` - Get training readiness
- `get_training_status(date)` - Get training status
- `get_respiration_data(date)` - Get respiration data
- `get_spo2_data(date)` - Get SpO2 data
- `get_max_metrics(date)` - Get max metrics

### Device Information
- `get_devices()` - Get devices
- `get_device_settings()` - Get device settings
- `get_primary_device()` - Get primary device

### Workouts
- `get_workouts()` - Get workouts
- `upload_workout(workout_data)` - Upload workout
- `delete_workout(workout_id)` - Delete workout

## Error Handling

The library includes custom exceptions:
- `GarminConnectAuthenticationError` - Authentication failed
- `GarminConnectConnectionError` - Connection issues
- `GarminConnectTooManyRequestsError` - Rate limiting

## Credits

This library was created by [cyberjunky](https://github.com/cyberjunky) and is maintained by the community.

## License

MIT License
