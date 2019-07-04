import os
from datetime import timedelta


class GeneralConfig(object):
    """
    Las variables aquí puestas están definidas en la documentación oficial
    de Flask.

    Las variables explicadas en la documentación estan configuradas con su
    valor predeterminado, si necesitas darle un valor en especifico, lo único
    que requieres es crear la variable de entorno en tu sistema operativo o
    entorno de trabajo.

    http://flask.pocoo.org/docs/1.0/config/#builtin-configuration-values
    """
    ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('FLASK_DEBUG', 'False')
    TESTING = os.getenv('FLASK_TESTING', 'False')
    PROPAGATE_EXCEPTIONS = os.getenv('FLASK_PROP_EXCEPTIONS', None)
    PRESERVE_CONTEXT_ON_EXCEPTION = os.getenv(
        'FLASK_PRESERVE_CONTEXT_ON_EXCEPTION', None
    )
    TRAP_HTTP_EXCEPTIONS = os.getenv(
        'FLASK_TRAP_HTTP_EXCEPTIONS', False
    )
    TRAP_BAD_REQUEST_ERRORS = os.getenv(
        'FLASK_TRAP_BAD_REQUEST_ERRORS', None
    )
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', None)
    SESSION_COOKIE_NAME = os.getenv('FLASK_SESSION_COOKIE_NAME', 'session')
    SESSION_COOKIE_DOMAIN = os.getenv('FLASK_SESSION_COOKIE_DOMAIN', None)
    SESSION_COOKIE_PATH = os.getenv('FLASK_SESSION_COOKIE_PATH', None)
    SESSION_COOKIE_HTTPONLY = os.getenv('FLASK_SESSION_COOKIE_HTTPONLY', True)
    SESSION_COOKIE_SECURE = os.getenv('FLASK_SESSION_COOKIE_SECURE', False)
    SESSION_COOKIE_SAMESITE = os.getenv('FLASK_SESSION_COOKIE_SAMESITE', None)
    PERMANENT_SESSION_LIFETIME = os.getenv(
        'FLASK_PERMANENT_SESSION_LIFETIME', timedelta(days=31)
    )
    SESSION_REFRESH_EACH_REQUEST = os.getenv(
        'FLASK_SESSION_REFRESH_EACH_REQUEST', True
    )
    USE_X_SENDFILE = os.getenv('FLASK_USE_X_SENDFILE', False)
    SEND_FILE_MAX_AGE_DEFAULT = os.getenv(
        'FLASK_SEND_FILE_MAX_AGE_DEFAULT', timedelta(hours=12)
    )
    SERVER_NAME = os.getenv('FLASK_SERVER_NAME', None)
    APPLICATION_ROOT = os.getenv('FLASK_APPLICATION_ROOT', '/')
    PREFERRED_URL_SCHEME = os.getenv('FLASK_PREFERRED_URL_SCHEME', 'http')
    MAX_CONTENT_LENGTH = os.getenv('FLASK_MAX_CONTENT_LENGTH', None)
    JSON_AS_ASCII = os.getenv('FLASK_JSON_AS_ASCII', True)
    JSON_SORT_KEYS = os.getenv('FLASK_JSON_SORT_KEYS', True)
    JSONIFY_PRETTYPRINT_REGULAR = os.getenv(
        'FLASK_JSONIFY_PRETTYPRINT_REGULAR', False
    )
    JSONIFY_MIMETYPE = os.getenv('FLASK_JSONIFY_MIMETYPE', 'application/json')
    TEMPLATES_AUTO_RELOAD = os.getenv('FLASK_TEMPLATES_AUTO_RELOAD', None)
    EXPLAIN_TEMPLATE_LOADING = os.getenv(
        'FLASK_EXPLAIN_TEMPLATE_LOADING', False
    )
    MAX_COOKIE_SIZE = os.getenv('FLASK_MAX_COOKIE_SIZE', 4093)


class ConfigApplication(GeneralConfig):
    """
    http://flask-sqlalchemy.pocoo.org/2.3/config/
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_SQLALCHEMY_DATABASE_URI', None)
