#!/bin/bash

# Deploy MQTT broker
kubectl apply -f kubernetes/broker-app-deployment.yml
kubectl apply -f kubernetes/broker-app-service.yml

# Wait for broker deployment to be ready
kubectl rollout status deployment/broker-app

# Deploy broadcast-app and receive-app
kubectl apply -f kubernetes/broadcast-app-deployment.yml
kubectl apply -f kubernetes/receive-app-deployment.yml
