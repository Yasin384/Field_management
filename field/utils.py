import requests
from rest_framework.exceptions import AuthenticationFailed

USER_SERVICE_API = "https://manageuser.up.railway.app/api"

def get_user_from_token(token):
    """
    Получает данные пользователя по токену из User Management Service
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{USER_SERVICE_API}/users/me/", headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise AuthenticationFailed("Invalid or expired token.")
    else:
        raise Exception(f"Failed to connect to User Management Service: {response.status_code}")
