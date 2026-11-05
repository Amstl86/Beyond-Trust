default photogram_nancy_posts = [
    PhotogramPost(
        "nancy_corporate",
        photogram_nancy_profile,
        "images/nansy/corp.jpeg",
        "Корпоратив затянулся до позднего вечера. Иногда полезно задержаться и пообщаться с коллегами ✨",
        248,
        [
            PhotogramComment("Рик", "Рад был увидеть тебя вчера!"),
            PhotogramComment("Нэнси", "Спасибо за вечер 😊"),
        ]
    ),
    PhotogramPost(
        "nancy_archive",
        photogram_nancy_profile,
        "images/nansy/nansy_look.png",
        "Наконец-то выходной. Можно выдохнуть и никуда не спешить ☀️",
        192,
        [
            PhotogramComment("Нэнси", "Именно этого мне и не хватало!"),
        ]
    ),
]

default photogram_cindy_posts = [
    PhotogramPost(
        "cindy_interview",
        photogram_cindy_profile,
        "images/wife/posts/post_1.jpg",
        "Иду на собеседование, как думаете, возьмут? 😛",
        86,
        [
            PhotogramComment(
                random_photogram_comment_author(),
                "Я бы тебя принял!",
                photogram_cindy_profile.name
            ),
            PhotogramComment(
                random_photogram_comment_author(),
                "У тебя хорошие аргументы))",
                photogram_cindy_profile.name
            ),
            PhotogramComment(
                random_photogram_comment_author(),
                "Детка, надеюсь ты проглатываешь...",
                photogram_cindy_profile.name
            ),
            PhotogramComment(
                random_photogram_comment_author(),
                "О да ты бы хорошо поработала сидя на моих коленях",
                photogram_cindy_profile.name
            ),
        ]
    ),
]

default photogram_posts = photogram_cindy_posts + photogram_nancy_posts
