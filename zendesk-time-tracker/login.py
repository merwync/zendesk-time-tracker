import requests
import base64


def encode_credentials(username: str, password: str):
    return base64.b64encode(f"{username}:{password}".encode()).decode()


def org_names(zd_tenant: str, username: str, auth: str):
    base_url = f"https://{zd_tenant}.zendesk.com"
    search_url = f"{base_url}/api/v2/search.json"

    headers = {"Authorization": f"Basic {auth}"}
    params = {"query": f"assignee:{username} status:open"}
    with requests.Session() as session:
        response = session.get(search_url, headers=headers, params=params)
        org_ids = {ticket['organization_id'] for ticket in response.json()['results']}

        names = []
        for org_id in org_ids:
            if not org_id:
                continue
            org_url = f"{base_url}/api/v2/organizations/{org_id}.json"
            result = session.get(org_url, headers=headers)
            names.append(result.json()['organization']['name'])
    return names


def login(zd_tenant, username, password):
    credentials = encode_credentials(username, password)
    names = org_names(zd_tenant, username, auth=credentials)


if __name__ == '__main__':
    _tenant = "mkc-labs"

    login(_tenant, _username, _password)
