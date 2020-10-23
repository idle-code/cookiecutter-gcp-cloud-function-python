#!/usr/bin/env python

import json
import os
from collections import OrderedDict
from typing import List

LIST_FUNCTION_REGIONS_COMMAND="gcloud functions regions list --format json"
COOKIECUTTER_CONFIG_PATH="cookiecutter.json"

def list_function_regions() -> List[str]:
    gcloud_output_json = os.popen(LIST_FUNCTION_REGIONS_COMMAND).read()
    region_list = json.loads(gcloud_output_json)
    return sorted(list(map(lambda r: r["locationId"], region_list)))

if __name__ == "__main__":
    function_regions_list = list_function_regions()
    cookiecutter_config = json.load(open(COOKIECUTTER_CONFIG_PATH), object_pairs_hook=OrderedDict)
    cookiecutter_config["gcp_function_region"] = function_regions_list

    with open(COOKIECUTTER_CONFIG_PATH, 'w') as config_file:
        json.dump(cookiecutter_config, config_file, indent=2)
    

