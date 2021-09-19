FROM python:3.9.0

WORKDIR /home/

RUN git clone https://www.github.com/choesam/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-=qx%uk)*1yoh$y!^@e+2wn11a=a6xep@xmt$fh7@@_)um56w!p" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]