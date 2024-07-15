# Seth Martin | machina-infrastructure-hw

This repository completes the desired infrastructure assignment using `mqtt` to facilitate messages between a `broadcast-app` and a `receive-app` in the context of a minikube kubernetes environment. 

### Running via minikube

This repository contains two convenience scripts (`deploy.sh` and `build-images.sh`) for building and deploying the MQTT application. It is recommended to use them for simplicity.

_As with all shell scripts, feel free to inspect them before executing!_ 

#### Pre-Requisites

- Ensure that you have minikube installed and running 

  `minikube start`

- Make the convenience scripts located at the root of this project executable:

  `chmod +x deploy.sh`
  
  `chmod +x build-images.sh`

#### Running the program

1. Build the images: `./build-images.sh`

2. Deploy to minikube and port forward: `./deploy.sh`

Alternatively simply run `./build-images.sh && ./deploy.sh` in one line

Open a browser and navigage to: [http://localhost:5000](http://localhost:5000)

You should now be able to observe real time messages on the browser including a client-side calculated time difference between message receipts. 

To exit from the terminal where you are forwarding ports, simply hit `Enter`

### Project Organization 

The project makes use of MQTT to facilitate messages between a `receive-app` and `broadcast-app` through a Mosquitto broker (`broker-app`). The intention with this setup was to represent a real-world scenario where there may be many instances of `broadcast-app` (each representing a machine, for example).

Each application contains its own `Dockerfile` as they are intended to be deployed via Kubernetes (minikube) as standalone services that can be scaled as needed.

#### Project Directories 

`broadcast-app`: A standalone python application that sends messages via mqtt 

`receive-app`: A standalone flask application that subscribes to messages via mqtt and displays them in a browser 

`broker-app`: Simple dockerized mosquitto image to facilitate messaging 

`kubernetes`: Kubernetes deployment and service configuration files 


## Final Thoughts

I ran right up to about 4 hours of total time on this project over the weekend but had a pretty fun time putting this together and learning more about working with kubernetes. 

I believe the chosen technologies were good ones and make for a good representation of doing this in a real world context. I would not change too much on my approach save for the parts I didn't get together.

Overall, I enjoyed this assignment. It was a good balance of tightly scoped, entertainingly challenging, and relatively unconstrained in terms of how I could approach the problem.

### Note on Git History

Normally, I squash my commits when merging. I forgot to do that early on and kept the same pattern as I figured it would let you see the order I took if you were bored.

### What is missing

While this is complete from an initial requirements standard, there are a number of changes that we could make to improve things. I did not pursue these because (A) I'm nearly at the 4-hr limit and (B) the added complexity did not seem necessary given the original ask

- **Security** 

This is a simple illustrative example. In the real world, we would want to configure certificates and SSL to ensure that data is encryped and that only intended recepients can subscribe to messages. 

- **Better webapp UI**

The UI is obviously simplistic -- we don't have even have a CSS file! In the real world, we may want some niceties for filtering data or potentially even sending messages the other way.

- **A production server**

We are using Flask in a development manner. In the real world, we would probably want to use uvicorn or some other setup

- **Persistent data**

Right now, as soon as you refresh the browser we lose time deltas on messages since these are being calcuated on the client. We could move this to the server or store messages in a more persistent way 

- **Use of environment variables**

Things like "BROKER_ADDRESS" are hardcoded in the scripts. In the real world, it would make sense to probably pull these kinds of things out into an environment file.


## Initial Thoughts

Sounds like a fun project. I'll be making use of the following technologies: 

- `Python` (enjoyable, well-known language)

- `Poetry` package manager (easy and clean)

- `Ruff` code formatter (fast code formatting)

- `MQTT` via Mosquito (machine-to-machine protocol to facilitate broadcasting and reception)

- `Minikube` as that is requrested 

The approach I will take will be to setup `mqtt` as it is the gold standard for machine-to-machine communication and I'm guessing it or a similar service is in use at Machina. 
I'll have a broker as one service, a broadcasting client as another, and potentially one more as a subscriber that feeds into a simple webapp. 

There are some fun flourishes I could put in (like broadcasting hello world with a random color and displaiyng that) but we will save those for the end if there is time. 

# infrastructure-hw

## Your mission

For this assignment, you're going to create the infrastructure for an application with a small set of services.

- One service needs to broadcast `Hello world` at random intervals. Make the interval anywhere from 1 to 10 seconds, with each the time until the next broadcast each chosen randomly.

- Another service needs to receive the `Hello world` broadcasts.

- Then a user should be able to view the `Hello world` broadcasts, as they arrive, from a web browser.

### Other requirements

- Use whatever languages and frameworks you want to create the services.
- We're aiming to just run this application on an engineer's local machine, not the cloud; design your solution for `minikube`
- Your solution should have the minimum number of manual setup steps necessary.
- Use any adjacent infrastructure tools you think make for a more elegant solution.

## Submission

- Fork this repository on GitHub. Develop a solution on your fork. Extra points for good git hygiene.
- Include specific instructions in your README about pre-requisites and setup steps. Another engineer should be able to go from zero to running your solution on their local machine.
- Either send us the link to your repository (if you make it public) or email us a zipped-up folder.
