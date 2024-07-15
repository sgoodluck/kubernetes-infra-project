#!/bin/bash

# Set some globals
GREEN='\033[0;32m'
CLEAR='\033[0m'
PORT_FORWARD_PID=""

# Function to check if the image exists
check_image() {
  image_name=$1
  if minikube ssh "docker image inspect $image_name" &> /dev/null; then
    echo "Image $image_name exists in Minikube"
  else
    echo "Image $image_name does not exist in Minikube"
    exit 1
  fi
}

# Function to wait for termination of a resource
wait_for_termination() {
  resource_type=$1
  resource_name=$2

  echo "Waiting for $resource_type/$resource_name to terminate..."

  # Loop until the resource is terminated
  while kubectl get $resource_type $resource_name &> /dev/null; do
    echo "$resource_type/$resource_name is still terminating..."
    sleep 5
  done

  echo "$resource_type/$resource_name has terminated."
}

# Function to start port forwarding
start_port_forwarding() {
  # Start port forwarding in the background and redirect output to null
  echo -e "\nStarting port-forwarding..."
  kubectl port-forward service/receive-app-service 5000:80 > /dev/null 2>&1 &
  # Store the process ID of the port forwarding
  PORT_FORWARD_PID=$!
  echo "Port forwarding process ID: $PORT_FORWARD_PID"
}

# Function to stop port forwarding
stop_port_forwarding() {
  if [ -n "$PORT_FORWARD_PID" ]; then
    echo "Stopping port forwarding process..."
    kill $PORT_FORWARD_PID
    wait $PORT_FORWARD_PID 2>/dev/null
    echo "Port forwarding process stopped."
  fi
}

# Let everyone know we are starting
echo -e "\n${GREEN}Starting Deployment Process...${CLEAR}\n"

# Delete existing deployments if they exist
kubectl delete deployment broker-app receive-app broadcast-app --ignore-not-found=true

# Wait for termination of deployments
wait_for_termination deployment broadcast-app
wait_for_termination deployment receive-app
wait_for_termination deployment broker-app

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

echo -e "\n${GREEN}Deployment complete!${CLEAR}"

echo -e "\nCurrent pods:"
kubectl get pods

echo -e "\nCurrent services:"
kubectl get services

# Start port forwarding
start_port_forwarding

# Print out url
echo -e "\n${GREEN}Flask app is accessible at: http://localhost:5000\n${CLEAR}"

# Await user input to stop port forwarding
read -p $'Press Enter to stop port forwarding and exit...'

# Stop port forwarding
stop_port_forwarding

# Bye Now
echo -e "\n${GREEN}Exiting!${CLEAR}"
