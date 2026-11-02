init python:
    class PhotogramProfile:
        def __init__(self, name, avatar, biography, followers, followed):
            self.name = name
            self.avatar = avatar
            self.biography = biography
            self.followers = followers
            self.followed = followed


    class PhotogramComment:
        def __init__(self, author, text):
            self.author = author
            self.text = text


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
