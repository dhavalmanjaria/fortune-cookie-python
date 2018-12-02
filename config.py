from logging.config import dictConfig
import os

flask_port = "5002"
flask_host = "0.0.0.0"

# postgres
postgres_username = 'postgres'
postgres_password = 'password'
db_name = "fortunes"
postgres_host = "127.0.0.1"
postgres_port = "5432"


# SQLALCHEMY
# sqlalchemy_database_uri = ("""
#     sqlite:///{path}\\\\fortunes.db""".format(
#         path=os.path.dirname(os.path.realpath(
#             __file__)).replace("\\", "\\\\")))

sqlalchemy_database_uri = "sqlite:///fortunes.db"

# Logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s',
        },
        'info': {
            'format': '[%(asctime)s]: %(message)s',
            'datefmt': '%H:%M:%S'
        }
    },
    'handlers': {
        'debugfilehandler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'default'
        },
        'consolehandler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'info'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['debugfilehandler', 'consolehandler'],
            'level': 'DEBUG',
            'propogate': True,
        },
        'console': {
            'handlers': ['consolehandler', 'debugfilehandler'],
            'level': 'INFO',
            'propogate': True
        }
    }
}

dictConfig(LOGGING_CONFIG)
