#!/usr/bin/env bash
set -euo pipefail

# Generate openapi.json
cp tests/test_config.yml config.yml
poetry run example openapi

# Create a fake container to share data with openapi generator
docker create -v /local --name shared alpine:3.4 /bin/true
docker cp generator-config.yml shared:/local/generator-config.yml
docker cp openapi.json shared:/local/openapi.json

# Generate the new client
docker run --rm --volumes-from shared \
  openapitools/openapi-generator-cli generate \
  -i /local/openapi.json \
  -g typescript-angular \
  -c /local/generator-config.yml \
  -o /local/angular-client

# Copy the client back to the main machine
docker cp shared:/local/angular-client angular-client

# Build and publish
cd angular-client
echo "//npm.fury.io/my-org//:_authToken=$GEMFURY_PUSH_TOKEN" > .npmrc
npm install
npm run build
npm publish dist
