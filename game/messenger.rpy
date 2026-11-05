
# messenger.rpy


# ============================================================
# ДАННЫЕ
# ============================================================

# История сообщений
default chat_messages = []
default greg_cindy_messages = []
default greg_frank_messages = []
default greg_stan_messages = []
default greg_cindy_unread = False
default greg_frank_unread = False
default greg_stan_unread = False
default greg_cindy_read = False
default greg_photogram_prompt_pending = False
default greg_photogram_prompt_shown = False
default current_day = 1
default day_two_messages_sent = False

init python:
    def scroll_chat_to_bottom(adjustment):
        adjustment.change(adjustment.range)

    def resolve_frank_help_choice(messages, message_index, should_help):
        choice_message = messages[message_index]
        choice_message["sender"] = "Greg"
        choice_message["text"] = "Да" if should_help else "Нет"
        choice_message["choice"] = False

        if should_help:
            messages.extend([
                {"sender": "Frank", "text": "Спасибо, друг! Сегодня я всё обдумаю и составлю план действий, а завтра поведаю его тебе."},
                {"sender": "Greg", "text": "Хорошо, до завтра!"},
            ])
        else:
            messages.extend([
                {"sender": "Greg", "text": "Друг, мне кажется, ты себя накручиваешь. Нэнси порядочная девушка, она любит тебя, а для корпоратива все одеваются красиво — это же как Новый год!"},
                {"sender": "Frank", "text": "Ты правда так думаешь? На самом деле она пришла весёлая, обнимала и целовала меня, а потом даже подрочила мне!"},
                {"sender": "Greg", "text": "Вот видишь, тебе не о чем переживать!"},
                {"sender": "Frank", "text": "Спасибо, Грег, ты меня успокоил! Увидимся!"},
            ])


# ============================================================
# АВАТАРЫ
# ============================================================

image avatar cindy = Transform(
    "images/avatars/cindy.png",
    xysize=(56, 56)
)

image avatar steve = Transform(
    "images/avatars/steve.png",
    xysize=(56, 56)
)

image messenger_cindy_avatar = AlphaMask(
    "ava_cindy",
    "images/other/avatar_circle_mask.png"
)

image messenger_greg_avatar = AlphaMask(
    "greg_avatar",
    "images/other/avatar_circle_mask.png"
)

image messenger_frank_avatar = AlphaMask(
    "images/sprites/ava_frank.png",
    "images/other/avatar_circle_mask.png"
)

image messenger_stan_avatar = AlphaMask(
    "images/sprites/ava_stan.png",
    "images/other/avatar_circle_mask.png"
)

screen nansy_look_viewer():

    modal True

    add Solid("#000000")

    imagebutton:
        idle "images/nansy/nansy_look.png"
        hover "images/nansy/nansy_look.png"
        action Return()
        xalign 0.5
        yalign 0.5


screen wife_look_viewer():

    modal True

    add Solid("#000000")

    imagebutton:
        idle "images/wife/wife_look.jpg"
        hover "images/wife/wife_look.jpg"
        action Return()
        xalign 0.5
        yalign 0.5


# ============================================================
# ЭКРАН МЕССЕНДЖЕРА
# ============================================================

screen messenger_chat(messages, contact_name, contact_sender, back_to_inbox=False, initial_message_index=0):

    modal True
    zorder 200
    default message_index = initial_message_index
    default last_scrolled_index = 0
    default chat_yadjustment = ui.adjustment()
    $ waiting_for_choice = (
        back_to_inbox
        and message_index < len(messages)
        and messages[message_index].get("choice", False)
    )

    # Фон за пределами смартфона
    add Solid("#000000")

    # Корпус смартфона
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

            # ------------------------------------------------
            # ШАПКА МЕССЕНДЖЕРА
            # ------------------------------------------------

            frame:
                xfill True
                ysize 100

                background Solid("#103b35")
                padding (20, 12)

                vbox:
                    spacing 4

                    text contact_name:
                        size 32
                        color "#ffffff"

                    text "● online":
                        size 18
                        color "#77e69b"

            # ------------------------------------------------
            # ОБЛАСТЬ ПЕРЕПИСКИ
            # ------------------------------------------------

            viewport:
                id "chat_viewport"

                xfill True
                ysize 760

                # Начинаем просмотр с последнего сообщения
                yinitial 1.0
                yadjustment chat_yadjustment

                # Прокрутка колёсиком мыши
                mousewheel True

                # Возможность перетаскивать область мышью
                draggable True

                # Полоса вертикальной прокрутки
                scrollbars "vertical"

                vbox:
                    xfill True
                    spacing 18

                    for msg in (messages[:message_index + 1] if back_to_inbox else messages):
                        if msg.get("choice", False):

                            frame:
                                xalign 0.5
                                xmaximum 420
                                background Solid("#45494b")
                                padding (18, 14)

                                vbox:
                                    xfill True
                                    spacing 12

                                    text msg["prompt"]:
                                        xalign 0.5
                                        size 25
                                        color "#ffffff"

                                    hbox:
                                        xalign 0.5
                                        spacing 24

                                        textbutton "Да":
                                            text_size 23
                                            action [
                                                Function(resolve_frank_help_choice, messages, message_index, True),
                                                SetScreenVariable("message_index", message_index + 1)
                                            ]

                                        textbutton "Нет":
                                            text_size 23
                                            action [
                                                Function(resolve_frank_help_choice, messages, message_index, False),
                                                SetScreenVariable("message_index", message_index + 1)
                                            ]

                        elif msg["sender"] == contact_sender:

                            # --------------------------------
                            # СООБЩЕНИЕ КОНТАКТА — СЛЕВА
                            # --------------------------------

                            hbox:
                                xfill True
                                spacing 10

                                if contact_sender == "Cindy":
                                    add "messenger_cindy_avatar":
                                        xysize (48, 48)
                                        yalign 0.2
                                elif contact_sender == "Frank":
                                    add "messenger_frank_avatar":
                                        xysize (48, 48)
                                        yalign 0.2
                                elif contact_sender == "Stan":
                                    add "messenger_stan_avatar":
                                        xysize (48, 48)
                                        yalign 0.2
                                else:
                                    frame:
                                        xysize (48, 48)
                                        yalign 0.2
                                        background Solid("#103b35")
                                        text contact_name[0]:
                                            xalign 0.5
                                            yalign 0.5
                                            size 26
                                            color "#ffffff"

                                # Облачко сообщения
                                frame:
                                    xmaximum 390

                                    background Frame("images/other/chat_bubble_cindy.png", 18, 18, 18, 18)
                                    padding (16, 12)

                                    if msg.get("image_link", False):
                                        textbutton msg["text"]:
                                            action If(
                                                back_to_inbox,
                                                Return((msg.get("image_action", "show_nansy_look"), message_index)),
                                                Return(msg.get("image_action", "show_nansy_look"))
                                            )
                                            text_size 25
                                            text_color "#a8d8ff"
                                            text_hover_color "#ffffff"
                                            text_underline True
                                    else:
                                        text msg["text"]:
                                            size 25
                                            color "#ffffff"

                        else:

                            # --------------------------------
                            # СООБЩЕНИЕ ГРЕГА — СПРАВА
                            # --------------------------------

                            hbox:
                                xfill True
                                spacing 10

                                # Свободное пространство слева
                                null width 1 xfill True

                                # Облачко сообщения
                                frame:
                                    xmaximum 390

                                    background Frame("images/other/chat_bubble_greg.png", 18, 18, 18, 18)
                                    padding (16, 12)

                                    text msg["text"]:
                                        size 25
                                        color "#ffffff"

                                # Аватар Грега
                                add "messenger_greg_avatar":
                                    xysize (48, 48)
                                    yalign 0.2

            # ------------------------------------------------
            # НИЖНЯЯ ПАНЕЛЬ СМАРТФОНА
            # ------------------------------------------------

            frame:
                xfill True
                ysize 120

                background Solid("#103b35")
                padding (12, 12)

                textbutton (
                    "Следующее сообщение  →"
                    if back_to_inbox and message_index < len(messages) - 1
                    else "Назад к чатам"
                    if back_to_inbox
                    else "Продолжить  →"
                ):
                    xalign 0.5
                    yalign 0.5
                    text_size 25
                    sensitive not waiting_for_choice
                    action If(
                        back_to_inbox and message_index < len(messages) - 1,
                        SetScreenVariable("message_index", message_index + 1),
                        Return("inbox") if back_to_inbox else Return()
                    )

    if back_to_inbox and last_scrolled_index != message_index:
        timer 0.01 action [
            Function(scroll_chat_to_bottom, chat_yadjustment),
            SetScreenVariable("last_scrolled_index", message_index)
        ]

    key "K_SPACE" action If(
        waiting_for_choice,
        NullAction(),
        If(
            back_to_inbox and message_index < len(messages) - 1,
            SetScreenVariable("message_index", message_index + 1),
            Return("inbox") if back_to_inbox else Return()
        )
    )
    key "K_ESCAPE" action Return("inbox" if back_to_inbox else None)


screen greg_phone_home_screen():

    modal True
    zorder 0

    add Solid("#000000")

    add Transform("images/sprites/fon.jpg", xysize=(397, 813), fit="cover"):
        xpos 761
        ypos 138

    imagebutton:
        idle Transform("images/icons/mf_icon.png", xysize=(62, 62))
        hover Transform("images/icons/mf_icon.png", xysize=(62, 62))
        focus_mask True
        xpos 844
        ypos 255
        action Return("photogram")

    imagebutton:
        idle Transform(
            "images/icons/new_messedge.png"
            if greg_cindy_unread or greg_frank_unread or greg_stan_unread or photogram_notification_unread
            else "images/icons/bubble.png",
            xysize=(62, 62)
        )
        hover Transform(
            "images/icons/new_messedge.png"
            if greg_cindy_unread or greg_frank_unread or greg_stan_unread or photogram_notification_unread
            else "images/icons/bubble.png",
            xysize=(62, 62)
        )
        focus_mask True
        xpos 927
        ypos 255
        action Return("messenger")

    textbutton "Закончить день":
        xpos 840
        ypos 890
        xsize 240
        text_size 22
        text_color "#ffffff"
        action Return("end_day")

    textbutton "Убрать телефон":
        xpos 840
        ypos 845
        xsize 240
        text_size 22
        text_color "#ffffff"
        action Return("close")

    key "K_ESCAPE" action Return("close")


screen greg_messenger_inbox_screen():

    modal True
    zorder 200
    default inbox_unread_only = False
    default inbox_search = ""

    $ inbox_chats = [
        {
            "id": "Cindy",
            "name": "Синди",
            "avatar": "messenger_cindy_avatar",
            "unread": greg_cindy_unread,
            "enabled": True,
        },
        {
            "id": "Frank",
            "name": "Френк",
            "avatar": "messenger_frank_avatar",
            "unread": greg_frank_unread,
            "enabled": True,
        },
        {
            "id": "Stan",
            "name": "Стэн",
            "avatar": "messenger_stan_avatar",
            "unread": greg_stan_unread,
            "enabled": greg_cindy_read,
        },
    ]

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
                ysize 100
                background Solid("#103b35")
                padding (20, 12)

                text "Сообщения":
                    size 32
                    color "#ffffff"
                    yalign 0.5

            hbox:
                xfill True
                ysize 54
                spacing 8

                textbutton "Все":
                    xsize 110
                    yfill True
                    text_size 20
                    text_color "#ffffff"
                    background Solid("#216b4a" if not inbox_unread_only else "#45494b")
                    hover_background Solid("#2d805a" if not inbox_unread_only else "#565b5d")
                    action SetScreenVariable("inbox_unread_only", False)

                textbutton "Непрочитанные":
                    xsize 190
                    yfill True
                    text_size 18
                    text_color "#ffffff"
                    background Solid("#216b4a" if inbox_unread_only else "#45494b")
                    hover_background Solid("#2d805a" if inbox_unread_only else "#565b5d")
                    action SetScreenVariable("inbox_unread_only", True)

                null width 1 xfill True

            frame:
                xfill True
                ysize 58
                background Solid("#45494b")
                padding (14, 8)

                hbox:
                    xfill True
                    yfill True
                    spacing 10

                    text "Поиск:":
                        size 18
                        color "#b8b8b8"
                        yalign 0.5

                    input:
                        value ScreenVariableInputValue("inbox_search")
                        length 40
                        size 20
                        color "#ffffff"
                        idle_color "#b8b8b8"
                        copypaste True
                        xfill True

            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"

                vbox:
                    xfill True
                    spacing 2

                    $ visible_chat_count = 0

                    for chat in inbox_chats:
                        $ matches_search = (
                            not inbox_search
                            or inbox_search.lower() in chat["name"].lower()
                        )
                        $ matches_filter = (
                            not inbox_unread_only
                            or (chat["unread"] and chat["enabled"])
                        )

                        if matches_search and matches_filter:
                            $ visible_chat_count += 1

                            button:
                                xfill True
                                ysize 88
                                padding (10, 8)
                                sensitive chat["enabled"]
                                background Solid("#174b3a" if chat["unread"] else "#34383a")
                                hover_background Solid("#2d805a" if chat["unread"] else "#45494b")
                                action Return(chat["id"])

                                hbox:
                                    xfill True
                                    yfill True
                                    spacing 14

                                    add chat["avatar"]:
                                        xysize (60, 60)
                                        yalign 0.5

                                    vbox:
                                        xfill True
                                        yalign 0.5

                                        hbox:
                                            xfill True
                                            text chat["name"]:
                                                size 25
                                                color "#ffffff"

                                            null width 1 xfill True

                                            if chat["unread"] and chat["enabled"]:
                                                text "НОВОЕ":
                                                    size 13
                                                    color "#77e69b"

                    if visible_chat_count == 0:
                        text "Чаты не найдены":
                            xalign 0.5
                            yoffset 24
                            size 20
                            color "#b8b8b8"

            frame:
                xfill True
                ysize 120
                background Solid("#103b35")
                padding (12, 12)

                textbutton "На главный экран":
                    xalign 0.5
                    yalign 0.5
                    text_size 25
                    action Return("home")

    key "K_SPACE" action Return("home")
    key "K_ESCAPE" action Return("home")


# ============================================================
# ТЕСТОВАЯ ПЕРЕПИСКА
# ============================================================

label messenger_test:

    # Очищаем историю перед началом теста
    $ chat_messages = []

    # --------------------------------------------------------
    # СООБЩЕНИЕ 1
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Cindy",
        "text": "Привет. Ты ещё не спишь?"
    })

    call screen messenger_chat(chat_messages, "Грег", "Cindy")

    # --------------------------------------------------------
    # СООБЩЕНИЕ 2
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Steve",
        "text": "Привет! Нет, как раз собирался заканчивать дела."
    })

    call screen messenger_chat(chat_messages, "Грег", "Cindy")

    # --------------------------------------------------------
    # СООБЩЕНИЕ 3
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Cindy",
        "text": "Просто захотелось с кем-нибудь поговорить."
    })

    call screen messenger_chat(chat_messages, "Грег", "Cindy")

    # --------------------------------------------------------
    # СООБЩЕНИЕ 4 — ПРОВЕРКА ДЛИННОГО ТЕКСТА
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Steve",
        "text": "Конечно, можешь написать мне. Я пока не собираюсь спать. Как прошёл твой день? Всё в порядке?"
    })

    call screen messenger_chat(chat_messages, "Грег", "Cindy")

    # --------------------------------------------------------
    # ЗАВЕРШЕНИЕ ТЕСТА
    # --------------------------------------------------------

    "Конец тестовой переписки."

    return
