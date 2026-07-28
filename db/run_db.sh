docker build -t school-db-img .

docker run -d --rm --name school-db --network school-network db-img