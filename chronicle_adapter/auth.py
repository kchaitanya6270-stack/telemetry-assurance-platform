from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/cloud-platform"
]

SERVICE_ACCOUNT_FILE = (
    "credentials/secops-key.json"
)

def get_access_token():

    credentials = (
        service_account.Credentials
        .from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )
    )

    credentials.refresh(Request())

    return credentials.token