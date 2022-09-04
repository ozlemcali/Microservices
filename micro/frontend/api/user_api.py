import requests
from flask import session
from . import USER_API_URL


class UserClient:
    @staticmethod
    def login(form):
        api_key = None
        payload = {
            'username': form.username.data,
            'password': form.password.data
        }

        url = USER_API_URL + '/api/user/login'

        response = requests.post(url, data=payload)
        if response:
            api_key = response.json().get('api_key')

        return api_key

    @staticmethod
    def get_user():
        headers = {
            'Authorization': session['user_api_key']
        }

        url = USER_API_URL + '/api/user'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def create_user(form):
        user = None
        payload = {
            'password': form.password.data,
            'username': form.username.data
        }
        url = USER_API_URL + '/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def user_exists(username):
        url = USER_API_URL + '/api/user/' + username + '/exists'

        response = requests.get(url)
        return response.status_code == 200
