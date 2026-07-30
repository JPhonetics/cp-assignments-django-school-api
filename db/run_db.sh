docker build -t school-db-img .

docker run -d --rm \
-p 5433:5432 \
--name school_db \
--network school-network \
school-db-img