from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/'+secret_name) #암호키가 있는 경로를 설정
    secret = file.read() #read 함수를 통해 파일 읽고
    secret = secret.rstrip().lstrip() #좌우 공백들 지우기
    file.close() #파일 닫기
    return secret
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #mysql 에서 분화 되어 나온게 mariadb 이다
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb', #네트워크 를 사용할때 container 에서 mariadb 를 도메인처럼 사용하기 위해서  즉 container name 이 들어간다.
        'PORT': '3306',
    }
}