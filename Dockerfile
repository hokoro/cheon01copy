FROM python:3.9.0

WORKDIR /home/
RUN echo 'secret'
RUN git clone https://github.com/hokoro/cheon01copy.git

WORKDIR /home/cheon01copy/



RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=cheon1copy.settings.deploy && python manage.py migrate --settings=cheon1copy.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=cheon1copy.settings.deploy cheon1copy.wsgi --bind 0.0.0.0:8000"]