# cookiecutter-gcp-cloud-function-python
## Features
- Environment variables management by pydantic (support for `.env.yaml` file)
- Project dependency management via Poetry (`pyproject.toml`)
- Uses Flask development server for local testing
- (Re)Deployment script

## Requirements
- [Poetry](https://python-poetry.org/docs/#installation)
- [Google Cloud SDK (aka `gcloud` command)](https://cloud.google.com/sdk/docs/install)

## Usage
```console
$ cookiecutter gh:idle-code/cookiecutter-gcp-cloud-function-python
project_name [My GCP Cloud Function]: 
project_slug [my_gcp_cloud_function]: 
gcp_project []: # Your Google project ID goes here; if empty - your current gcloud configuration will define it
Select gcp_function_region:
1 - asia-east2
2 - asia-northeast1
3 - asia-northeast2
4 - asia-northeast3
5 - asia-south1
6 - asia-southeast2
7 - australia-southeast1
8 - europe-central2
9 - europe-west1
10 - europe-west2
11 - europe-west3
12 - europe-west6
13 - northamerica-northeast1
14 - southamerica-east1
15 - us-central1
16 - us-east1
17 - us-east4
18 - us-west2
19 - us-west3
20 - us-west4
Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 [1]:
gcp_cloud_function_name [my_gcp_cloud_function]: # This is how function will be named in GCP console
code_entry_point [on_request_received]:  # This is python function name as seen in the source
Select memory:
1 - 128MB
2 - 256MB
3 - 512MB
4 - 1024MB
5 - 2048MB
6 - 4096MB
7 - 8192MB
Choose from 1, 2, 3, 4, 5, 6, 7 [1]:
max_auto_scaling_instances [0]:
Select runtime:
1 - python38
2 - python37
Choose from 1, 2 [1]: 
Select timeout:
1 - default (1m)
2 - 30s
3 - 1m
4 - 2m
5 - 5m
6 - 9m
Choose from 1, 2, 3, 4, 5, 6 [1]: 
Select allow_unauthenticated:
1 - y
2 - n
Choose from 1, 2 [1]: 
full_name: Pawel Zukowski
email: p.z.idlecode@gmail.com
$ poetry shell
$ poetry update
```

## Local testing
Enter created directory and execute:
```console
$ poetry shell
$ poetry update
$ ./main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

## Deployment
You can use generated `deploy.sh` script but double check it for your use case!
