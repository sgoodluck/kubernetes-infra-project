# Seth Martin 


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
