from .common import *

DEBUG = True

ES_INDEXES = {'default': 'notes_index_dev'}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
    }
}
