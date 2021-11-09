

SECRET_KEY = 'django-insecure-fa4#&htm_sxm3c*5x-me##4lrx=!jbsw8-mo#+!(%%h(1iryg+'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        'USER': 'root',
        'PASSWORD': 'patriots1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
