# Hello World API

## Install FASTAPI Framework to Build API

```sh
poetry add fastapi
```

```sh
poetry add "uvicorn[standard]"
```

## Run it 

```sh
uvicorn pyapi.main:app --reload
```

## Create Hello World API

```sh
from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
def hello_world():
    return {"message": "Hello World!"}
```

```sh
> curl http://localhost:8000/hello
{"message":"Hello World!"}%
```

Done! First API is Done!


## Restful API

- Get
- Post
- Delete
- PUT

```sh

```