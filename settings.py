from os import environ


SESSION_CONFIGS = [
    dict(
        name='informality_experiment_A1',
        display_name='INFORMALITY_EXPERIMENT_A1',
        num_demo_participants=1,
        app_sequence=['informality_experiment_A1'],
    ),
    dict(
        name='informality_experiment_B1',
        display_name='INFORMALITY_EXPERIMENT_B1',
        num_demo_participants=1,
        app_sequence=['informality_experiment_B1'],
    ),    
    dict(
        name='informality_experiment_C1',
        display_name='INFORMALITY_EXPERIMENT_C1',
        num_demo_participants=1,
        app_sequence=['informality_experiment_C1'],
    ),
    dict(
        name='informality_experiment_D1',
        display_name='INFORMALITY_EXPERIMENT_D1',
        num_demo_participants=1,
        app_sequence=['informality_experiment_D1'],
    ),
    dict(
        name='informality_experiment_E1',
        display_name='INFORMALITY_EXPERIMENT_E1',
        num_demo_participants=1,
        app_sequence=['informality_experiment_E1'],
    ),
    dict(
        name='informality_experiment_F1',
        display_name='INFORMALITY_EXPERIMENT_F1',
        num_demo_participants=1,
        app_sequence=['informality_experiment_F1'],
    ),
    dict(
        name='informality_experiment_A2',
        display_name='INFORMALITY_EXPERIMENT_A2',
        num_demo_participants=1,
        app_sequence=['informality_experiment_A2'],
    ),
    dict(
        name='informality_experiment_B2',
        display_name='INFORMALITY_EXPERIMENT_B2',
        num_demo_participants=1,
        app_sequence=['informality_experiment_B2'],
    ),
    dict(
        name='informality_experiment_C2',
        display_name='INFORMALITY_EXPERIMENT_C2',
        num_demo_participants=1,
        app_sequence=['informality_experiment_C2'],
    ),      
    dict(
        name='informality_experiment_D2',
        display_name='INFORMALITY_EXPERIMENT_D2',
        num_demo_participants=1,
        app_sequence=['informality_experiment_D2'],
    ),
    dict(
        name='informality_experiment_E2',
        display_name='INFORMALITY_EXPERIMENT_E2',
        num_demo_participants=1,
        app_sequence=['informality_experiment_E2'],
    ),
    dict(
        name='informality_experiment_F2',
        display_name='INFORMALITY_EXPERIMENT_F2',
        num_demo_participants=1,
        app_sequence=['informality_experiment_F2'],
    ),    
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '6f7*&08=q8da_rg57h22d&$@v=kt$ywqe2-lt&cfiv+)7s0(%9'

INSTALLED_APPS = ['otree']
