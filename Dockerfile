FROM python:3.10.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /local;
ADD /enviroalert /local
RUN mkdir /config
ADD /config/requirements.txt /config
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.txt
# RUN apt-get update && apt-get install -y gettext
EXPOSE 8888
CMD bash -c "python manage.py makemigrations && python manage.py migrate && gunicorn enviroalert.wsgi --reload -b 0.0.0.0:8888"
WORKDIR /local