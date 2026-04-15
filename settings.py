import os
import platform
from pathlib import Path

# Get the current user's home directory in a cross-platform way
if platform.system() == "Windows":
    home = Path(os.environ['USERPROFILE'])
elif platform.system() == "Darwin":  # macOS
    home = Path(os.environ['HOME'])
else:  # Assuming Linux
    home = Path(os.environ['HOME'])

# Define the path for the settings file based on the platform
if platform.system() == "Windows":
    settings_path = home / 'AppData' / 'Local' / 'DigitalDetective' / 'settings.cfg'
elif platform.system() == "Darwin":  # macOS
    settings_path = home / 'Library' / 'Application Support' / 'DigitalDetective' / 'settings.cfg'
else:  # Assuming Linux
    settings_path = home / '.config' / 'DigitalDetective' / 'settings.cfg'

# Make sure the settings directory exists
settings_path.parent.mkdir(parents=True, exist_ok=True)

# Example settings
settings = {
    'api_key': 'your_api_key_here',
    'timeout': 30,
}

# Save settings to file
with settings_path.open('w') as f:
    for key, value in settings.items():
        f.write(f'{key}={value}\n')
