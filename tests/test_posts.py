from postschemas import PostSchema, PostsListSchema

def test_get_all_posts(api_client, base_url):
    response = api_client.get(f"{base_url}/posts")
    assert response.status_code == 200
    posts = PostsListSchema.validate_python(response.json())
    assert len(posts) > 0

def test_get_single_post(api_client, base_url):
    post_id = 4
    response = api_client.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    post = PostSchema.model_validate(response.json())
    assert post.id == post_id
    assert post.title is not None

def test_create_post(api_client, base_url):
    new_post = {
        "title": "New Post",
        "body": "This is a new post.",
        "userId": 1
    }
    response = api_client.post(f"{base_url}/posts", json=new_post)
    assert response.status_code == 201
    post = PostSchema.model_validate(response.json())
    assert post.title == new_post["title"]
    assert post.body == new_post["body"]
    assert post.userId == new_post["userId"]

def test_update_post(api_client, base_url):
    post_id = 1
    payload={
        "title": "Updated Post",
        "body": "This is an updated post.",
        "userId": 1,
        "id":1
    }
    response = api_client.put(f"{base_url}/posts/{post_id}", json=payload)
    assert response.status_code == 200
    post = PostSchema.model_validate(response.json())
    assert post.title == payload["title"]

def test_delete_post(api_client, base_url):
    post_id = 4
    response = api_client.delete(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200