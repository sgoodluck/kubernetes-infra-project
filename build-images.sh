#!/bin/bash

# Set some colors
GREEN='\033[0;32m'
CLEAR='\033[0m'

# Let everyone know
echo -e "\n${GREEN}Starting Build Process...${CLEAR}\n"

# Ensure we're using Minikube's Docker daemon
eval $(minikube docker-env)

# Build the broadcast-app image
docker build -t broadcast-app:latest ./broadcast-app

# Build the broker-app image
docker build -t broker-app:latest ./broker-app

# Build the receive-app image
docker build -t receive-app:latest ./receive-app

# Display images
docker images

# Bye now
echo -e "\n${GREEN}Images built successfully - deploy to see changes${CLEAR}\n"
