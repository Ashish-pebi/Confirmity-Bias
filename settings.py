import os
from os import environ

# Don't share this with anybody.
SECRET_KEY = 'my_secret_key'

# The default is 8000, but you can change this to any port.
# Only used if you're running the oTree server directly.
# (not in a production setup with a reverse proxy)
BASE_DIR = os.path.dirname(os.path.abspath("C:/Users/Lap/Desktop/Python"))
#"C:\Users\Lap\Desktop\Python"
DEBUG = True

# The list of apps that are enabled in your project.
INSTALLED_APPS = [
    'otree' , 'app1'
    # Add other apps here
]

# Default language code for the project.
LANGUAGE_CODE = 'en'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Authentication and authorization
AUTH_PASSWORD_VALIDATORS = []

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '_static'),
]

# Minimum and maximum players per session
SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 1.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'app1',
        'display_name': "app1",
        'num_demo_participants': 3,
        'app_sequence': ['app1'],
    }
]

# Rooms
ROOMS = [
    {
        'name': 'my_room',
        'display_name': 'My Room',
        'participant_label_file': '_rooms/my_room.txt',
    },
]

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'password')

DEMO_PAGE_INTRO_HTML = """ """
