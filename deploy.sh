#!/bin/bash

IMAGE_NAME="metrics_app_image"
CONTAINER_NAME="metrics_app_container"

echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
	echo "Stopping and removing the existing container..."
	docker stop $CONTAINER_NAME >/dev/null 2>&1
	docker rm $CONTAINER_NAME >/dev/null 2>&1
fi

echo "Starting a new container..."
docker run -d --name $CONTAINER_NAME -p 5000:5000 --restart unless-stopped $IMAGE_NAME >/dev/null 2>&1

echo "Deploy completed successfully!"
echo "The application is now running at http://localhost:5000"
