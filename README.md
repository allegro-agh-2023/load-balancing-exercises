# Load balancing exercises

## Running all instances

```bash
docker compose build && docker compose up
```

## Build and run single app instance

1. Build docker image.

```bash
docker build -t flask-app ./app
```

2. Run docker container.

```bash
docker run -p 8080:5000 flask-app
```

3. Call your app from a browser or http client.

```http request
GET localhost:8080
```


## TODO

- java loadbalancer template
- instances with different sleep times (POST /job endpoint)
- benchmark
