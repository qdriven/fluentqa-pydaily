# OpenAPI Generator 

Use OpenAPI to generate server code or client code for different purpose.

## Install OpenAPI Generator

```sh
npm install @openapitools/openapi-generator-cli -g
```

Set OpenAPI Version:

```sh
openapi-generator-cli version-manager set 5.3.0
``` 


## Generate Code

```
npx @openapitools/openapi-generator-cli generate -i petstore.yaml -g ruby -o /tmp/test/
```

Run:

```sh
> openapi-generator-cli -h
Download 5.4.0 ...
Downloaded 5.4.0
Did set selected version to 5.4.0
Usage: openapi-generator-cli <command> [<args>]

Options:
  --custom-generator <generator>  Custom generator jar

Commands:
  version-manager                 Manage used / installed generator version
  author                          Utilities for authoring generators or
                                  customizing templates.
  batch                           Generate code in batch via external configs.
  config-help                     Config help for chosen lang
  generate [options]              Generate code with the specified generator.
  help                            Display help information about
                                  openapi-generator
  list                            Lists the available generators
  meta                            MetaGenerator. Generator for creating a new
                                  template set and configuration for Codegen.
                                  The output will be based on the language you
                                  specify, and includes default templates to
                                  include.
  validate                        Validate specification
  version                         Show version information used in **tooling**
  ```

## Local Docker

```sh
# Start container at port 8888 and save the container id
CID=$(docker run -d -p 8888:8080 openapitools/openapi-generator-online)
# allow for startup
sleep 10
# Get the IP of the running container (optional)
GEN_IP=$(docker inspect --format '{{.NetworkSettings.IPAddress}}'  ${CID})
# Execute an HTTP request to generate a Ruby client
curl -X POST --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  -d '{"openAPIUrl": "https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml"}' \
  'http://localhost:8888/api/gen/clients/ruby'
# Example output:
# {"code":"c2d483.3.4672-40e9-91df-b9ffd18d22b8","link":"http://localhost:8888/api/gen/download/c2d483.3.4672-40e9-91df-b9ffd18d22b8"}
# Download the generated zip file  (using "code" provided from your output) 
wget http://localhost:8888/api/gen/download/c2d483.3.4672-40e9-91df-b9ffd18d22b8
# Unzip the file
unzip c2d483.3.4672-40e9-91df-b9ffd18d22b8
# Shutdown the openapi generator image
docker stop ${CID} && docker rm ${CID}
```

## Generate python-fastapi	codes

```sh
openapi-generator-cli generate -g python-fastapi -i reference/todo-v3.yaml
```