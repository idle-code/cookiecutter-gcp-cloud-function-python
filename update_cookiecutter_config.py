#!/usr/bin/env python

import json
import os
from collections import OrderedDict
from typing import List


COOKIECUTTER_CONFIG_PATH="cookiecutter.json"

def list_function_regions() -> List[str]:
    LIST_FUNCTION_REGIONS_COMMAND="gcloud functions regions list --format json"
    gcloud_output_json = os.popen(LIST_FUNCTION_REGIONS_COMMAND).read()
    region_list = json.loads(gcloud_output_json)
    return sorted(list(map(lambda r: r["locationId"], region_list)))

def list_function_runtimes() -> List[str]:
    LIST_FUNCTION_RUNTIMES_COMMAND="gcloud functions runtimes list --format json"
    gcloud_output_json = os.popen(LIST_FUNCTION_RUNTIMES_COMMAND).read()
    runtime_list = json.loads(gcloud_output_json)
    active_runtimes = filter(lambda r: r["stage"] != "DEPRECATED", runtime_list)
    python_runtimes = filter(lambda r: r["name"].startswith("python"), active_runtimes)
    return sorted(list(map(lambda r: r["name"], python_runtimes)))

if __name__ == "__main__":
    cookiecutter_config = json.load(open(COOKIECUTTER_CONFIG_PATH), object_pairs_hook=OrderedDict)

    function_regions_list = list_function_regions()
    cookiecutter_config["gcp_function_region"] = function_regions_list

    function_runtimes_list = list_function_runtimes()
    cookiecutter_config["runtime"] = function_runtimes_list

    with open(COOKIECUTTER_CONFIG_PATH, 'w') as config_file:
        json.dump(cookiecutter_config, config_file, indent=2)
    

