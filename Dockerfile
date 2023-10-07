FROM python:3.10.12



RUN mkdir /local;
ADD /enviroalert /local
RUN mkdir /config
ADD /config/requirements.txt /config
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.txt
# RUN apt-get update && apt-get install -y gettext
EXPOSE 8000
WORKDIR /local
CMD bash -c "python manage.py makemigrations && python manage.py migrate"
CMD ["gunicorn", "enviroalert.wsgi",  "-b 0.0.0.0:8000"]
