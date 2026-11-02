screen greg_photogram_screen():

    modal True
    zorder 200
    default page = "feed"
    default current_post = None
    default current_story = None
    default current_profile = photogram_nancy_profile
    default story_return_page = "feed"
    default post_return_page = "feed"
    default profile_return_page = "feed"

    add Solid("#000000")

    frame:
        xsize 540
        ysize 1000
        xalign 0.5
        yalign 0.5
        background Solid("#34383a")
        padding (8, 8)

        vbox:
            xfill True
            yfill True
            spacing 0

            frame:
                xfill True
                ysize 78
                background Solid("#86345f")
                padding (18, 8)

                hbox:
                    xfill True
                    yalign 0.5

                    text "Photogram":
                        size 30
                        color "#ffffff"
                        yalign 0.5

                    null width 1 xfill True

                    textbutton "♡":
                        text_size 30
                        text_color "#ffffff"
                        action [
                            SetScreenVariable("page", "notifications"),
                            SetVariable("photogram_notification_unread", False),
                        ]

                    if photogram_notification_unread:
                        text "•":
                            size 28
                            color "#ffd24a"
                            xoffset -14
                            yoffset -10

            if page == "feed" or page == "explore":
                frame:
                    xfill True
                    ysize 98
                    background Solid("#292d2f")
                    padding (12, 8)

                    hbox:
                        spacing 18
                        yalign 0.5

                        if current_day >= 2:
                            for story in photogram_nancy_stories:
                                button:
                                    background None
                                    hover_background Solid("#45494b")
                                    action [
                                        SetScreenVariable("current_story", story),
                                        SetScreenVariable("story_return_page", page),
                                        SetScreenVariable("page", "story"),
                                    ]

                                    vbox:
                                        spacing 4
                                        xalign 0.5

                                        add Transform(story.image, xysize=(54, 54), fit="cover"):
                                            xalign 0.5

                                        text story.author:
                                            size 15
                                            color "#ffffff"
                                            xalign 0.5

                        if page == "explore":
                            for profile in photogram_profiles:
                                button:
                                    background None
                                    hover_background Solid("#45494b")
                                    action [
                                        SetScreenVariable("current_profile", profile),
                                        SetScreenVariable("profile_return_page", "explore"),
                                        SetScreenVariable("page", "profile"),
                                    ]

                                    vbox:
                                        spacing 4
                                        xalign 0.5

                                        add Transform(profile.avatar, xysize=(54, 54), fit="cover"):
                                            xalign 0.5

                                        text profile.name:
                                            size 15
                                            color "#ffffff"
                                            xalign 0.5

                viewport:
                    xfill True
                    ysize 680
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    vbox:
                        xfill True
                        spacing 14

                        for post in photogram_posts:
                            if (post.post_id not in ("nancy_corporate", "cindy_interview") or current_day >= 2) and (page == "explore" or post.profile.followed):
                                frame:
                                    xfill True
                                    background Solid("#292d2f")
                                    padding (10, 10)

                                    vbox:
                                        xfill True
                                        spacing 8

                                        textbutton post.author:
                                            text_size 22
                                            text_color "#ffffff"
                                            action [
                                                SetScreenVariable("current_profile", post.profile),
                                                SetScreenVariable("profile_return_page", page),
                                                SetScreenVariable("page", "profile"),
                                            ]

                                        button:
                                            xfill True
                                            background None
                                            hover_background None
                                            action [
                                                SetScreenVariable("current_post", post),
                                                SetScreenVariable("post_return_page", page),
                                                SetScreenVariable("page", "post"),
                                            ]

                                            add Transform(post.image, xysize=(460, 470), fit="cover"):
                                                xalign 0.5

                                        hbox:
                                            spacing 12

                                            textbutton ("♥" if post.liked else "♡"):
                                                text_size 28
                                                text_color "#f0718b"
                                                action Function(toggle_photogram_like, post)

                                            text "[post.likes]":
                                                size 20
                                                color "#ffffff"
                                                yalign 0.5

                                            textbutton "Комментарии ([len(post.comments)])":
                                                text_size 18
                                                text_color "#d7d7d7"
                                                action [
                                                    SetScreenVariable("current_post", post),
                                                    SetScreenVariable("post_return_page", page),
                                                    SetScreenVariable("page", "post"),
                                                ]

                                        text post.caption:
                                            size 18
                                            color "#ffffff"
                                            xmaximum 460

            elif page == "profile":
                viewport:
                    xfill True
                    ysize 778
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    vbox:
                        xfill True
                        spacing 18

                        textbutton "← Назад":
                            text_size 20
                            action SetScreenVariable("page", profile_return_page)

                        hbox:
                            spacing 18
                            yalign 0.5

                            add Transform(current_profile.avatar, xysize=(100, 100), fit="cover")

                            vbox:
                                spacing 8

                                text current_profile.name:
                                    size 25
                                    color "#ffffff"

                                text "[len([post for post in photogram_posts if post.profile == current_profile and (post.post_id != 'cindy_interview' or current_day >= 2)])] публикации":
                                    size 17
                                    color "#c5c5c5"

                                text "[current_profile.followers] подписчиков":
                                    size 17
                                    color "#c5c5c5"

                                textbutton ("Вы подписаны" if current_profile.followed else "Подписаться"):
                                    text_size 18
                                    action Function(toggle_photogram_follow, current_profile)

                        text current_profile.biography:
                            size 18
                            color "#d7d7d7"

                        for post in photogram_posts:
                            if post.profile == current_profile and (post.post_id not in ("nancy_corporate", "cindy_interview") or current_day >= 2):
                                button:
                                    xfill True
                                    background Solid("#292d2f")
                                    hover_background Solid("#45494b")
                                    padding (8, 8)
                                    action [
                                        SetScreenVariable("current_post", post),
                                        SetScreenVariable("post_return_page", "profile"),
                                        SetScreenVariable("page", "post"),
                                    ]

                                    hbox:
                                        spacing 12

                                        add Transform(post.image, xysize=(90, 90), fit="cover")

                                        vbox:
                                            spacing 6
                                            text post.caption:
                                                size 16
                                                color "#ffffff"
                                                xmaximum 365
                                            text "♥ [post.likes]":
                                                size 16
                                                color "#f0718b"

            elif page == "notifications":
                vbox:
                    xfill True
                    yfill True
                    spacing 18

                    text "Уведомления":
                        size 25
                        color "#ffffff"

                    if current_day >= 2:
                        button:
                            xfill True
                            background Solid("#292d2f")
                            hover_background Solid("#45494b")
                            padding (12, 12)
                            action [
                                SetScreenVariable("current_post", photogram_nancy_posts[0]),
                                SetScreenVariable("post_return_page", "notifications"),
                                SetScreenVariable("page", "post"),
                            ]

                            text "[photogram_nancy_profile.name] опубликовала новую фотографию":
                                size 18
                                color "#ffffff"
                                xmaximum 470
                    else:
                        text "Пока нет новых уведомлений.":
                            size 18
                            color "#c5c5c5"

            elif page == "post" and current_post:
                viewport:
                    xfill True
                    ysize 778
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    vbox:
                        xfill True
                        spacing 14

                        textbutton "← Назад":
                            text_size 20
                            action SetScreenVariable("page", post_return_page)

                        text current_post.author:
                            size 22
                            color "#ffffff"

                        add Transform(current_post.image, xysize=(480, 500), fit="cover"):
                            xalign 0.5

                        hbox:
                            spacing 12

                            textbutton ("♥" if current_post.liked else "♡"):
                                text_size 28
                                text_color "#f0718b"
                                action Function(toggle_photogram_like, current_post)

                            text "[current_post.likes]":
                                size 20
                                color "#ffffff"
                                yalign 0.5

                        text current_post.caption:
                            size 18
                            color "#ffffff"
                            xmaximum 480

                        text "Комментарии":
                            size 20
                            color "#ffffff"

                        for comment in current_post.comments:
                            frame:
                                xfill True
                                background Solid("#292d2f")
                                padding (12, 8)

                                text "[comment.author]: [comment.text]":
                                    size 17
                                    color "#e5e5e5"
                                    xmaximum 460

            elif page == "story" and current_story:
                vbox:
                    xfill True
                    yfill True
                    spacing 12

                    hbox:
                        xfill True

                        text "[current_story.author] — история":
                            size 20
                            color "#ffffff"
                            yalign 0.5

                        null width 1 xfill True

                        textbutton "×":
                            text_size 30
                            action SetScreenVariable("page", story_return_page)

                    add Transform(current_story.image, xysize=(480, 650), fit="contain"):
                        xalign 0.5
                        yalign 0.5

                    text current_story.caption:
                        size 18
                        color "#ffffff"
                        xalign 0.5

            frame:
                xfill True
                ysize 76
                background Solid("#86345f")
                padding (8, 6)

                hbox:
                    xfill True
                    yalign 0.5
                    spacing 4

                    textbutton "Главная":
                        text_size 17
                        text_color "#ffffff"
                        action SetScreenVariable("page", "feed")

                    textbutton "Поиск":
                        text_size 17
                        text_color "#ffffff"
                        action SetScreenVariable("page", "explore")

                    textbutton "Профиль":
                        text_size 17
                        text_color "#ffffff"
                        action [
                            SetScreenVariable("current_profile", photogram_nancy_profile),
                            SetScreenVariable("profile_return_page", "feed"),
                            SetScreenVariable("page", "profile"),
                        ]

                    null width 1 xfill True

                    textbutton "Выход":
                        text_size 17
                        text_color "#ffffff"
                        action Return()

    key "K_ESCAPE" action Return()
