# Introduction
The repository contains 3 services that has to be run in parallel:

1. gRPC server      - Implemented in Python 
2. gRPC client      - Implemented in Python using FastAPI
3. HTML client (UI) - Plain HTML file as specified

Docker is used to package the respective services, and Docker Compose enables
the three services to run on the same host with different ports.

# Steps to run the 3 microservices

1. Ensure docker is set up locally

2. Clone the repository

3. At the root of the repository, run `docker compose up`

4. Terminal
    - ![](./assets/docker_compose.png)

5. Visit [http://localhost:80/](http://localhost:80/)
    - ![](./assets/html.png)

# Rationale behind a few decisions 
1. FastAPI over Django/Flask
    - I needed something lightweight, as Django is heavy with many built-in modules that aren't necessary for this assignment.
    - I needed a framework with good documentation, and FastAPI's documentation is better than what Flask offers.

2. Usage of Pydantic (having a models folder which contains a custom data class)
    - gRPC allows us to define function parameters and types, which is great for
    consistentcy across different services on a network level, but it does not
    provide data validation that could be crucial and necessary for application
    logic and further processing. Pydantic helps with that.
    - IDE support for linting and navigating across definitions can be very
    important for developers.

3. Usage of Docker
    - Docker is the gold standard for running applications on various machines
    in the most convenient way possible. With Docker Hub, people can skip
    setting up specific environments, as they simply need to pull the images to
    run.
    - Using Docker Compose also allows you to run three different services on
    the same host without needing separate terminal windows or tmux sessions..
    
4. Usage of 'Single-Request-Stream-Response' function among the 4 type of gRPC methods
    - In our case, we have a CSV file containing numerous entries of the same
    data types (timestamp and float). This necessitates a function that can
    yield results as they are ready. Unlike a CSV file, a live system would have
    a meter continuously producing these values at a rapid pace. Therefore,
    there's a need for 'streaming' instead of sending values in bulk.
    
# Additional To-dos
1. Since the images are hosted on Docker Hub, it's possible to spin up a
container service on AWS, allowing us to have a live website without needing to
run anything locally.

2. We need better error handling when reading from the Excel sheet, as there
could be invalid values. Currently, I am skipping values that may be incorrect,
but this process could be improved.

3. Since gRPC is language-agnostic, I could have written the server in Go and
the client in Python. This approach would allow me to leverage Go's speed for
time and memory-intensive tasks while using Python for non-critical tasks.

4. I could have used `pytest` to write unit and integration tests.