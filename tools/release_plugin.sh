INFRASTRUCTURE_NAME=$(echo "${INF}" | jq -r '.name' | tr -d '\n')
INFRASTRUCTURE_KEY=$(echo "${INF}" | jq -r '.key' | tr -d '\n')
echo "::add-mask::$INFRASTRUCTURE_KEY"
if [[ "${{ github.event.inputs.RELEASE_PROD_CLOUD_US }}" == "true" ]]; then
  docker login -u ${{ secrets.KOMAND_DOCKERHUB_USER }} -p ${{ secrets.KOMAND_DOCKERHUB_PASSWORD }}
  export INFRASTRUCTURE=$(echo "${INF}" | jq -r '.env' | tr -d '\n')
  echo "::add-mask::$INFRASTRUCTURE"
  export IAM_ROLE=$(echo "${INF}" | jq -r '.stsPluginS3Role' | tr -d '\n')
  echo "::add-mask::$IAM_ROLE"
  export IAM_ROLE_EXTERNAL_ID=$(echo "${INF}" | jq -r '.stsPluginS3ExternalId' | tr -d '\n')
  echo "::add-mask::$IAM_ROLE_EXTERNAL_ID"
  export IAM_SESSION_DURATION="${!IAM_SESSION_DURATION}"
  MARKET_TOKEN_NAME="${INFRASTRUCTURE_KEY}_MARKET_TOKEN"
  export MARKET_TOKEN="${!MARKET_TOKEN_NAME}"
  MARKET_USERNAME_NAME = "${INFRASTRUCTURE_KEY}_MARKET_USERNAME"
  export MARKET_TOKEN="${!MARKET_USERNAME_NAME}"
  MARKET_PASSWORD_NAME = "${INFRASTRUCTURE_KEY}_MARKET_PASSWORD"
  DOCKER_REGISTRY_USERNAME_NAME = "${INFRASTRUCTURE_KEY}_DOCKER_REGISTRY_USERNAME"
  export DOCKER_REGISTRY_USERNAME="${!DOCKER_REGISTRY_USERNAME_NAME}"
  DOCKER_REGISTRY_PASSWORD_NAME = "${INFRASTRUCTURE_KEY}_DOCKER_REGISTRY_PASSWORD"
  export DOCKER_REGISTRY_PASSWORD="${!DOCKER_REGISTRY_PASSWORD_NAME}"
  export MARKET_TOKEN="${{ secrets.PROD_CLOUD_US_MARKET_TOKEN }}"
  export MARKET_TOKEN="${{ secrets.PROD_CLOUD_US_MARKET_USERNAME }}"
  export MARKET_PASSWORD="${{ secrets.PROD_CLOUD_US_MARKET_PASSWORD }}"
  export DOCKER_REGISTRY_USERNAME="${{ secrets.PROD_CLOUD_US_DOCKER_REGISTRY_USERNAME }}"
  export DOCKER_REGISTRY_PASSWORD="${{ secrets.PROD_CLOUD_US_DOCKER_REGISTRY_PASSWORD }}"
  if [[ "$INFRASTRUCTURE_NAME" == "alliance_staging" || "$INFRASTRUCTURE_NAME" == "alliance_prod" ]]; then
    export PLUGINS_S3_BUCKET=$(echo "${INF}" | jq -r '.pluginsS3Bucket' | tr -d '\n')
  else
    export PLUGINS_S3_BUCKET=""
  fi
  echo "::add-mask::$PLUGINS_S3_BUCKET"
  export IAM_HOST="$IAM_HOST"
  chmod +x ./tools/retrieve_upload_credentials.sh
  . ./tools/retrieve_upload_credentials.sh
  cd plugins
  echo "INFO: Releasing $INFRASTRUCTURE_NAME!!!"
  KOMAND_SOURCE_BRANCH=${{ github.head_ref }} ../.ci_venv/bin/icon-ci release
else
  echo "INFO: Skipping $INFRASTRUCTURE_NAME!!!"
fi