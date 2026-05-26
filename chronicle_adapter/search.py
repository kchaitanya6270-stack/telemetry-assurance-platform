import requests

from chronicle_adapter.auth import (
    get_access_token
)

PROJECT_ID = "touchstone-chron"

CHRONICLE_URL = (
    "https://us-chronicle.googleapis.com"
)

def run_query(query):

    print("GETTING TOKEN")

    token = get_access_token()

    print("TOKEN SUCCESS")

    url = (
        f"{CHRONICLE_URL}"
        "/v1alpha/projects/"
        f"{PROJECT_ID}"
        "/locations/us/instances/default/search"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": query
    }

    print("\nURL:")
    print(url)

    print("\nSENDING REQUEST")

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("\nSTATUS CODE:")
    print(response.status_code)

    print("\nRAW RESPONSE:")
    print(response.text)

    return response.text