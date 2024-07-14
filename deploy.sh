#!/bin/bash


# helper to check if the image exists
check_image() {
  image_name=$1
  if minikube ssh "docker image inspect $image_name" &> /dev/null; then
    echo "Image $image_name exists in Minikube"
  else
    echo "Image $image_name does not exist in Minikube"
    exit 1
  fi
}

# Set some colors
GREEN='\033[0;32m'
CLEAR='\033[0m'

# Let everyone know
echo -e "\n${GREEN}Starting Deployment Process...${CLEAR}\n"

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
kubectl apply -f kubernetes/receive-app-service.yml

# Wait for receive-app deployment
kubectl rollout status deployment/receive-app

# Start port forwarding in the background and redirect output to null
echo -e "\nStarting port-forwarding..."
kubectl port-forward service/receive-app-service 5000:80 > /dev/null 2>&1 &

# Print out url
echo -e "\n${GREEN}Flask app is accessible at: http://localhost:5000\n${CLEAR}"

# Await user input to kill process
read -p $'Press Enter to stop port forwarding and exit...'

# Kill the port forwarding process
pkill -f "kubectl port-forward"

# Bye Now
echo -e "\n${GREEN}Exiting!${CLEAR}"
