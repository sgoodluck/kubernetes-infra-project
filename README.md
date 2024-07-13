# Seth Martin | machina-infrastructure-hw

I have tried to update this README progressively so you can also see my thoughts as I was going.

## Running via minikube

TODO...

## Running Locally

To run this locally (without docker or minikube) you can do the following:

0. Ensure that you have [poetry](https://python-poetry.org/docs/) and [mosquitto](https://mosquitto.org/) installed on your machine

1. Open a terminal and start mosquitto in verbose mode: `mosquitto -v`

2. Open a second terminal and cd into the broadcast app to install dependencies and run the broadcast program:

    `cd broadcast-app && poetry install && poetry run python broadcast/broadcast.py`
    
    
3. Open a third terminal and cd into the receive app to isntall dependencies and run the receive program:

    `cd receive-app && poetry install && poetry run python receive/receive.py`

Congratulations -- you should be able to see the program functioning as expected locally! 

<img width="1462" alt="Capture d’écran 2024-07-13 à 15 22 21" src="https://github.com/user-attachments/assets/fb3acca3-96f1-4742-88c5-7e48f9ab4281">

# Thought Stream

## 1.5 Fixed some issues

Fixed some issues with how I setup MQTT. Need to take a lunch break. Back soon

## 1. Local MQTT is done -- onto minikube

Alright, we have the local project directories setup and can successfully run the `broadcast` and `receive` apps locally through mosquitto. Next step will be dockerizing and setting up for one stop execution via minikube. 

I'll save the webapp portion of things for last.

## 0. Initial Thoughts

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
