# Adapted GPT application for User Model

## Requirements

- Add your openai key in the config.ini file. 
- Docker

## Start the application

To start the application, first build the docker image:

```bash
docker build -t adaptedgpt .
```

Once built, start the application by running the following command:

```bash
docker run -p 8765:8765 -p 5000:5000 adaptedgpt
```


The application is now accessible at [http://localhost:5000](http://localhost:5000)

