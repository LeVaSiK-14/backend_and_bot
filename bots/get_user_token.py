from register_user import user_registration_api
from api_urls import user_get_token
from send_request import SendRequest


class GetUserToken(SendRequest):
    def __init__(self, users, method=None):
        super().__init__(method)
        self.users = users

    def get_token(self):
        user_tokens = []
        for user in self.users:
            response = self.send_url(url=user_get_token, data=user)
            response['id'] = user['id']
            user_tokens.append(response)

        return user_tokens


get_user_token = GetUserToken(
    users=user_registration_api, method='POST'.upper()).get_token()
