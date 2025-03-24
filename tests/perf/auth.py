import requests
from tests.perf.config import KEYCLOAK_URL, REALM, CLIENT_ID, USERNAME, PASSWORD


def get_token():
    resp = requests.post(
        f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token",
        data={
            "client_id": CLIENT_ID,
            "username": USERNAME,
            "password": PASSWORD,
            "grant_type": "password",
            "scope": "openid profile email",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return resp.json()["access_token"]


if __name__ == "__main__":
    token = get_token()
    print(token)
