from generate_post import create_posts
from send_request import SendRequest


class SendPost(SendRequest):
    def __init__(self, posts, method=''):
        super().__init__(method=method)
        self.posts = posts

    def send_post(self):
        send_posts = []
        for post in self.posts:
            data = {'title': post['title'], 'description': post['description']}
            response = self.send_url(url=post['url'], data=data, headers={
                'Authorization': f"Token {post['token']}"})
            data['id'] = response['id']
            send_posts.append(data)
        return send_posts


send_posts = SendPost(create_posts, 'POST'.upper()).send_post()
