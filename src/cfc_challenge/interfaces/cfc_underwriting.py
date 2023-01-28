import json
import os
from typing import Any

import requests

from sty import fg
from cfc_challenge.domain.cfc_underwriting import get_external_resources, get_hyperlinks, get_word_frequency_count

URL = "https://www.cfcunderwriting.com"


def get_cfc_data() -> int:
    """
    Scrapes URL and stores collected data in JSON files
    """
    response = requests.get(URL)

    if response.status_code != 200:
        print(fg.red + f"Error {response.status_code}: {response.reason}!" + fg.rs)
        return 1

    external_resources = get_external_resources(response)
    hyperlinks, privacy_policy = get_hyperlinks(response)
    privacy_policy_link = URL + privacy_policy

    if not privacy_policy_link:
        print(fg.red + "Error: Privacy Policy not found in response!" + fg.rs)
        return 1

    privacy_policy_response = requests.get(privacy_policy_link)

    if privacy_policy_response.status_code != 200:
        print(fg.red + f"Error {privacy_policy_response.status_code}: {privacy_policy_response.reason}!" + fg.rs)
        return 1

    word_frequency_count = get_word_frequency_count(privacy_policy_response)

    external_resources_dict = {"external_resources": [resource.dict() for resource in external_resources]}

    _save_dict_to_json(external_resources_dict, "resources.json")
    _save_dict_to_json(hyperlinks, "hyperlinks.json")
    _save_dict_to_json(word_frequency_count, "word_count.json")

    return 0


def _save_dict_to_json(data: dict[str, Any], file_name: str) -> None:
    if not os.path.exists("JSON"):
        os.makedirs("JSON")

    with open(f"JSON/{file_name}", "w") as json_file:
        json.dump(data, json_file, indent=4)
