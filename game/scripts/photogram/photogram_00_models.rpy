init python:
    class PhotogramProfile:
        def __init__(self, name, avatar, biography, followers, followed):
            self.name = name
            self.avatar = avatar
            self.biography = biography
            self.followers = followers
            self.followed = followed


    class PhotogramComment:
        def __init__(self, author, text, liked_by=None):
            self.author = author
            self.text = text
            self.liked_by = liked_by


    class PhotogramPost:
        def __init__(self, post_id, profile, image, caption, likes, comments):
            self.post_id = post_id
            self.profile = profile
            self.author = profile.name
            self.image = image
            self.caption = caption
            self.likes = likes
            self.liked = False
            self.comments = comments


    class PhotogramStory:
        def __init__(self, author, image, caption):
            self.author = author
            self.image = image
            self.caption = caption


    def toggle_photogram_like(post):
        post.liked = not post.liked
        post.likes = max(0, post.likes + (1 if post.liked else -1))


    def toggle_photogram_follow(profile):
        profile.followed = not profile.followed


    def random_photogram_comment_author():
        return renpy.random.choice([
            "Alex_R",
            "MaxPower",
            "Dima_87",
            "Mike",
            "HotGuy23",
            "Roman_K",
            "NightOwl",
            "Sergey",
        ])


    def ensure_photogram_cindy_workday_post():
        post = next(
            (post for post in photogram_cindy_posts if post.post_id == "cindy_workday"),
            None
        )
        created = post is None

        if post is None:
            post = PhotogramPost(
                "cindy_workday",
                photogram_cindy_profile,
                "images/wife/posts/w_photogram_1.jpg",
                "На работе я отдаюсь на 100%",
                0,
                [
                    PhotogramComment(
                        random_photogram_comment_author(),
                        "Отдайся мне!",
                        photogram_cindy_profile.name
                    ),
                    PhotogramComment(
                        random_photogram_comment_author(),
                        "Представляю, как ты под столом работаешь",
                        photogram_cindy_profile.name
                    ),
                    PhotogramComment(
                        random_photogram_comment_author(),
                        "Я бы заполнил твой рот на 100%",
                        photogram_cindy_profile.name
                    ),
                ]
            )
            photogram_cindy_posts.append(post)

        if not any(existing.post_id == "cindy_workday" for existing in photogram_posts):
            photogram_posts.append(post)

        return created
