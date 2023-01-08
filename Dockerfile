FROM python:3.8.10
COPY ./ ./
RUN python3 -m pip install django \
    djangorestframework \
    tensorflow \
    keras \
    pandas
CMD python3 manage.py runserver 0.0.0.0:8000
