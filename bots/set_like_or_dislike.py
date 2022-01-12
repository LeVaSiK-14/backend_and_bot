import random

from send_request import SendRequest
from api_urls import (
    set_like_or_dislike,
    end_dislike_url,
    end_like_url
)



class AddLike(SendRequest):
    def __init__(self, posts, users, method=''):
        super().__init__(method=method)
        self.posts = posts
        self.users = users

    def add_like(self):
        likes = []
        for user in self.users:
            access_token = user["access"]

            for post in self.posts:

                urls = [
                    f"{set_like_or_dislike}{post['id']}{end_like_url}",
                    f"{set_like_or_dislike}{post['id']}{end_dislike_url}",
                ]

                response = self.send_url(
                    url=random.choice(urls),
                    headers={"Authorization": f"Token {access_token}"},
                )
                response['post_id'] = post['id']
                likes.append(response)
        return likes
