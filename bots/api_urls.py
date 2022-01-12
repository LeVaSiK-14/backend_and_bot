
# USER REGISTRATION {"username": "username", "password": "password"}
user_registration_url = 'http://0.0.0.0:8000/api/registration/'  # POST

# USER GET TOKEN {"username": "username", "password": "password"}
user_get_token = 'http://0.0.0.0:8000/api/token/'  # POST

# USER CREATE POST {"title": "12345", "description": "qwertyu"}
user_create_post = 'http://0.0.0.0:8000/api/users/'  # POST
end_post_url = '/add_post/'

# POST SET LIKE OR DISLIKE
set_like_or_dislike = "http://0.0.0.0:8000/api/posts/"  # POST

end_like_url = '/set_like/'
end_dislike_url = '/set_dislike/'
