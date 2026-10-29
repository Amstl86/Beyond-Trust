
# messenger.rpy


# ============================================================
# ДАННЫЕ
# ============================================================

# История сообщений
default chat_messages = []


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

screen nansy_look_viewer():

    modal True

    add Solid("#000000")

    imagebutton:
        idle "images/nansy/nansy_look.png"
        hover "images/nansy/nansy_look.png"
        action Return()
        xalign 0.5
        yalign 0.5


# ============================================================
# ЭКРАН МЕССЕНДЖЕРА
# ============================================================

screen messenger_chat(messages, contact_name, contact_sender, back_to_inbox=False):

    modal True
    zorder 200

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

                # Прокрутка колёсиком мыши
                mousewheel True

                # Возможность перетаскивать область мышью
                draggable True

                # Полоса вертикальной прокрутки
                scrollbars "vertical"

                vbox:
                    xfill True
                    spacing 18

                    for msg in messages:

                        if msg["sender"] == contact_sender:

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
                                            action Return("show_nansy_look")
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

                textbutton ("Назад к чатам" if back_to_inbox else "Продолжить  →"):
                    xalign 0.5
                    yalign 0.5
                    text_size 25
                    if back_to_inbox:
                        action Return("inbox")
                    else:
                        action Return()

    # Пробел выполняет то же действие, что и кнопка
    key "K_SPACE" action Return("inbox" if back_to_inbox else None)


screen greg_phone_home_screen():

    modal True
    zorder 200

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
        idle Transform("images/icons/bubble.png", xysize=(62, 62))
        hover Transform("images/icons/bubble.png", xysize=(62, 62))
        focus_mask True
        xpos 927
        ypos 255
        action Return("messenger")

    textbutton "Убрать телефон":
        xpos 840
        ypos 845
        xsize 240
        text_size 22
        text_color "#ffffff"
        action Return("close")


screen greg_photogram_screen():

    modal True
    zorder 200

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
                background Solid("#86345f")
                padding (20, 12)

                text "Photogram":
                    size 32
                    color "#ffffff"
                    yalign 0.5

            null height 1 xfill True

            vbox:
                xfill True
                yfill True
                xalign 0.5
                yalign 0.5
                spacing 18

                text "Приложение пока недоступно":
                    xalign 0.5
                    size 28
                    color "#ffffff"
                    text_align 0.5

                text "Здесь появится продолжение позже.":
                    xalign 0.5
                    size 22
                    color "#c5c5c5"
                    text_align 0.5

            frame:
                xfill True
                ysize 120
                background Solid("#86345f")
                padding (12, 12)

                textbutton "На главный экран":
                    xalign 0.5
                    yalign 0.5
                    text_size 25
                    action Return()


screen greg_messenger_inbox_screen():

    modal True
    zorder 200

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

            vbox:
                xfill True
                yfill True
                spacing 18

                button:
                    xfill True
                    ysize 125
                    background Solid("#45494b")
                    hover_background Solid("#565b5d")
                    action Return("Cindy")

                    hbox:
                        xfill True
                        spacing 18
                        yalign 0.5

                        add "messenger_cindy_avatar":
                            xysize (64, 64)
                            yalign 0.5

                        vbox:
                            yalign 0.5
                            spacing 8
                            text "Синди":
                                size 28
                                color "#ffffff"
                            text "Ты права. Я сейчас напишу ему.":
                                size 19
                                color "#c5c5c5"

                button:
                    xfill True
                    ysize 125
                    background Solid("#45494b")
                    hover_background Solid("#565b5d")
                    action Return("Frank")

                    hbox:
                        xfill True
                        spacing 18
                        yalign 0.5

                        add "messenger_frank_avatar":
                            xysize (64, 64)
                            yalign 0.5

                        vbox:
                            yalign 0.5
                            spacing 8
                            text "Френк":
                                size 28
                                color "#ffffff"
                            text "До скорого, друг.":
                                size 19
                                color "#c5c5c5"

                button:
                    xfill True
                    ysize 125
                    background Solid("#45494b")
                    hover_background Solid("#565b5d")
                    action Return("Stan")

                    hbox:
                        xfill True
                        spacing 18
                        yalign 0.5

                        frame:
                            xysize (64, 64)
                            yalign 0.5
                            background Solid("#59616b")

                            text "С":
                                xalign 0.5
                                yalign 0.5
                                size 32
                                color "#ffffff"

                        vbox:
                            yalign 0.5
                            spacing 8
                            text "Стэн":
                                size 28
                                color "#ffffff"
                            text "Нет сообщений":
                                size 19
                                color "#c5c5c5"

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
