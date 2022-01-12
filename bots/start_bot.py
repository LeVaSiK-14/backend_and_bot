from set_like_or_dislike import AddLike
from send_posts import send_posts
from get_user_token import get_user_token


add_like = AddLike(send_posts, get_user_token,
                    method='POST'.upper()).add_like()
