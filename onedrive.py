import os
import msal
from office365.graph_client import GraphClient


TENANT_ID = "c78653c8-e2d0-43c9-bd26-bd52ea50dea6"
APPLICATION_CLIENT_ID = "821d722e-cfe1-4b58-8df1-a3b46d419383"


def read_env():
    with open(".env") as f:
        for line in f:
            key, value = line.strip().split("=")
            os.environ[key] = value


def acquire_token_func():
    authority_url = f"https://login.microsoftonline.com/{TENANT_ID}"
    app = msal.ConfidentialClientApplication(
        authority=authority_url,
        client_id=APPLICATION_CLIENT_ID,
        client_credential=os.environ["CLIENT_SECRET"],
    )
    token = app.acquire_token_for_client(
        scopes=["https://graph.microsoft.com/.default"]
    )
    return token


read_env()
client = GraphClient(acquire_token_func)
drives = client.drives.get().execute_query()
for drive in drives:
    print("Drive url: {0}".format(drive.web_url))

# currently doesnt work without an office 365 subscription
