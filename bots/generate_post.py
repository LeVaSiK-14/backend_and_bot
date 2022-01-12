import random
import string

from config import MAX_POSTS, posts_amount
from get_user_token import get_user_token
from api_urls import user_create_post, end_post_url


class GeneratePost:
    def __init__(self, users, amount_posts, max_posts):
        self.users = users
        self.amount_posts = amount_posts
        self.max_posts = max_posts

    def generate_post(self):
        posts = []
        if self.amount_posts > self.max_posts:
            raise ValueError(
                {"Error": f"You can generate max {self.max_posts} posts!"})
        else:
            for user in self.users:
                url = f"{user_create_post}{user['id']}{end_post_url}"
                access_token = user['access']
                for post in range(self.amount_posts):
                    post = {}
                    title = "".join(
                        [random.choice(string.ascii_letters)
                         for _ in range(10)]
                    )
                    description = "".join(
                        [random.choice(string.ascii_letters)
                         for _ in range(30)]
                    )
                    post["title"] = title
                    post["description"] = description
                    post['url'] = url
                    post['token'] = access_token
                    posts.append(post)
            return posts


create_posts = GeneratePost(get_user_token, posts_amount, MAX_POSTS).generate_post()
