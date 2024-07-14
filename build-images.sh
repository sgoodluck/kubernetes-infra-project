#!/bin/bash

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
