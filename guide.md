1. Deactivate virtual environment
    a. deactivate

2. Create the Django Project folder
    a. mkdir school_proj
    b. cd school_proj

3. Create virtual environment (venv)
    a. python -m venv .venv
    b. source .venv/bin/activate  ||  . .venv/bin/activate
        i. You will see (.venv) before your username and directory in the terminal
    c. add .vent/ into .gitignore

4. Install Django & create Django project
    a. pip install django

5. Create Django Project
    a. django-admin startproject school_proj .  ||  django-admin startproject school_proj
        i. 1st command installs into the current directory. 2nd command installs into a new folder called school_proj (nesting). We are running the first because we are already inside the proj folder.
        ii. school_proj > school_proj vs school_proj

6. Install Psycopg 3
    a. pip install "psycopg[binary]"

7. Save Project dependencies
    a. pip freeze > requirements.txt
    b. pip install -r requirements.txt

8. Test Django
    a. python manage.py runserver
        i. You can access Django at http://127.0.0.1:8000

9. Create database folder
    a. cd ..
    b. mkdir db
    c. cd db

10. Create PostgreSQL Dockerfile
    a. touch Dockerfile
    b. 
FROM postgres:15

ENV POSTGRES_USER=student
ENV POSTGRES_PASSWORD=student
ENV POSTGRES_DB=school_db

EXPOSE 5432

CMD ["postgres"]

11. Create run_db.sh
    a. touch run_db.sh
    b.
docker build -t school-db-img .

docker run -d --rm \
--name school-db \
--network school-network \
school-db-img

    c. chmod +x run_db.sh
        i. Makes the file executable

12. Create Docker Network
    a. cd ..
    b. docker network create school-network
        i. Remove a docker network with = docker network rm school-network
    c. docker network inspect school-network
        i. We should see the db container

13. Update settings.py
    a. Edit school_proj/settings.py
    b. Update ALLOWED_HOSTS to:
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

    c. Update DATABASE to:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "school_db",
        "USER": "student",
        "PASSWORD": "student",
        "HOST": "school-db",
        "PORT": "5432",
    }
}

14. Start PostgreSQL
    a. cd db
    b. ./run_db.sh
    c. Verify the container is running
        i. docker ps
    d. Rename the terminal session to psql
        i. We will keep this open to have an active connection to psql


15. Enter the psql
    a. docker exec -it school-db bash
        i. Enters the container
    b. psql -d school_db -U student
        i. connects to PostgreSQL
    c. \c school_db
        i. should return You are now connected to database "school_db" as user "student".
    Notes: Do not execute, stay inside psql for this terminal session.
        i. Quit with \q
        II. exit to exit container

16. Configure Django Dockerfile. You should be inside school_proj
    a. Open a new Terminal Session name it running django
        i. This session will keep the django container running.
    a. touch Dockerfile
        i. Should still be in school_proj, not school_proj > school_proj
    b.
FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


17. Create run_server.sh
    a. touch run_server.sh
    b. 
docker build -t school-django-img .

docker run --rm \
-v "$(pwd)/:/app/" \
-p 8000:8000 \
--name school-django \
--network school-network \
--user "$(id -u):$(id -g)" \
django-img

18. Start Django
    a. ./run_server.sh
        i. You can access Django at http://127.0.0.1:8000
    b. Keep this terminal session open, it will keep our django container running.

19. Enter Django Container
    a. Open a new terminal
        i. we should have 3 open at this point, 1 is running the django container, the other is running the db container.
        ii. This one will be our active connection to inside the django container.
    b. docker network inspect school-network
        i. We should see the db and django containers
    c. docker exec -it school-django bash

20. Run the Initial Migrations (still inside django container)
    a. python manage.py migrate 
        i. This step does something????????
    
21. Verify migrate inside psql
    a. Go to the psql terminal
    b. \d
        i. You should see all the django tables. around 19 rows

22. Create app
    a. cd school_proj (not the nested one)
        i. make sure you're in the right virtual environment
    b. python manage.py startapp student_app
    c. add this line into settings.py under INSTALLED_APPS
'student_app',

23. create models inside models.py
    a. edit school_proj > school_proj > student_app > models.py
    b. python manage.py makemigrations
    c. python manage.py migrate 

24. Verify table creation
    a. Go to psql terminal
    b. \dt
        i. You should see student_app_student
    c. SELECT * FROM STUDENT_APP_STUDENT;