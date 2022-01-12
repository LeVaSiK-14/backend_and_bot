from api_urls import user_registration_url
from generate_user import generate_users
from send_request import SendRequest


class UserRegistrationApi(SendRequest):
    def __init__(self, users, method=None):
        super().__init__(method)
        self.users = users

    def send_request(self):
        send_users = []
        for user in self.users:
            response = self.send_url(data=user, url=user_registration_url)
            user['id'] = response['user']['id']
            send_users.append(user)
        return send_users


user_registration_api = UserRegistrationApi(
    method='POST'.upper(), users=generate_users).send_request()
