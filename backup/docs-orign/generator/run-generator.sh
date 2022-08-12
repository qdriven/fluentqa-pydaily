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
#          