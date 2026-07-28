docker build -t school-django-img .

docker run --rm \
-v "$(pwd)/:/app/" \
-p 8000:8000 \
--name school-django \
--network school-network \
--user "$(id -u):$(id -g)" \
django-img