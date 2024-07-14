#!/bin/bash

# Function to check if image exists in Minikube
check_image() {
  image_name=$1
  if minikube ssh "docker image inspect $image_name" &> /dev/null; then
    echo "Image $image_name exists in Minikube"
  else
    echo "Image $image_name does not exist in Minikube"
    exit 1
  fi
}

# Delete existing deployments if they exist
kubectl delete deployment broker-app receive-app broadcast-app

# Check images before deploying
check_image "broadcast-app:latest"
check_image "broker-app:latest"
check_image "receive-app:latest"

# Deploy MQTT broker
kubectl apply -f kubernetes/broker-app-deployment.yml
kubectl apply -f kubernetes/broker-app-service.yml

# Wait for broker deployment to be ready
kubectl rollout status deployment/broker-app

# Deploy broadcast-app and receive-app
kubectl apply -f kubernetes/broadcast-app-deployment.yml
kubectl apply -f kubernetes/receive-app-deployment.yml
