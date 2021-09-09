from .base import *

env_list = dict() #secret key 를 담은 dictionary 생성

local_env = open(os.path.join(BASE_DIR,".env"))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n','')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #mysql 에서 분화 되어 나온게 mariadb 이다
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'fkaus132^^',
        'HOST': 'mariadb', #네트워크 를 사용할때 container 에서 mariadb 를 도메인처럼 사용하기 위해서  즉 container name 이 들어간다.
        'PORT': '3306',
    }
}