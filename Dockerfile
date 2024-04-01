FROM python:3.11.8
COPY . .
RUN pip install django \
    && pip install pymongo
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]