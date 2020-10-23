#!/usr/bin/env bash

# Generate requirements.txt file
echo "Generating requirements.txt..."
poetry export --format requirements.txt > requirements.txt

# Check existence of file with environment variables
ENV_YAML_FILE=".env.yaml"
if [ ! -f "$ENV_YAML_FILE" ]; then
  echo "Missing $ENV_YAML_FILE file - please create one from template before trying again"
  exit 1
fi

# Upload source code to the GCP
echo "Deploying to GCP..."
gcloud functions deploy \
  {{ cookiecutter.gcp_cloud_function_name }} \
  --project {{ cookiecutter.gcp_project }} \
  --region {{ cookiecutter.gcp_function_region }} \
  --entry-point={{ cookiecutter.code_entry_point }} \
  --runtime={{ cookiecutter.runtime }} \
  --memory={{ cookiecutter.memory }} \
  --timeout={{ cookiecutter.timeout }} \
  --env-vars-file=$ENV_YAML_FILE \
  {%- if cookiecutter.allow_unauthenticated == "y" %}
  --allow-unauthenticated \
  {%- endif %}
  --trigger-http


