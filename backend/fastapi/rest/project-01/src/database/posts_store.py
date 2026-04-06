from validation import Post


def build_default_posts():
    default_posts = [
        {
            "id": 1,
            "title": "First Post",
            "content": "This is the first post and it now includes a much more complete narrative for testing constraints. It explains the scenario, gives context, and adds enough detail to make the body substantial. The goal is to ensure the content length falls within the required limits.",
        },
        {
            "id": 2,
            "title": "Second Post",
            "content": "This is the second post and it is intentionally verbose so validation rules can be verified in unit tests. It describes a practical example, highlights expected behavior, and adds extra explanation so the text comfortably passes the minimum content threshold requirement.",
        },
        {
            "id": 3,
            "title": "Third Post",
            "content": "This is the third post with extended content designed to satisfy boundary checks for API data quality. It includes descriptive language, test-friendly structure, and enough characters to remain valid while still being concise enough to stay below the maximum limit.",
        },
    ]

    for post in default_posts:
        Post.model_validate(post)

    return default_posts


posts = build_default_posts()


def reset_posts():
    posts.clear()
    posts.extend(build_default_posts())
