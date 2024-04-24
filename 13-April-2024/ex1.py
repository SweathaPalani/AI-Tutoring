import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def create_post(title, body, user_id):
    """Create a new post."""
    response = requests.post(BASE_URL, data={'title': title, 'body': body, 'userId': user_id})
    return response.json()

def get_posts():
    """Retrieve all posts."""
    response = requests.get(BASE_URL)
    return response.json()

def get_post(post_id):
    """Retrieve a single post by ID."""
    response = requests.get(f"{BASE_URL}/{post_id}")
    return response.json()

def update_post(post_id, title, body, user_id):
    """Update an existing post."""
    response = requests.put(f"{BASE_URL}/{post_id}", data={'title': title, 'body': body, 'userId': user_id})
    return response.json()

def delete_post(post_id):
    """Delete a post."""
    response = requests.delete(f"{BASE_URL}/{post_id}")
    return response.status_code

# Test the functions
# new_post = create_post("Sample Title", "This is a test post", 1)
# print("Created Post:", new_post)

# all_posts = get_posts()
# print("All Posts:", all_posts[:3])  # Display the first 3 posts

# single_post = get_post(1)
# print("Single Post:", single_post)

updated_post = update_post(1, "Updated Title", "Updated Content", 1)
print("Updated Post: Hello my name is sweatha", updated_post)

# delete_status = delete_post(101)  # Assuming post 101 exists
# print("Delete Status:", delete_status)
