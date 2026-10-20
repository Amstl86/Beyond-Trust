
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


# ============================================================
# ЭКРАН МЕССЕНДЖЕРА
# ============================================================

screen messenger_chat(messages):

    modal True

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

                    text "Грег":
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

                        if msg["sender"] == "Cindy":

                            # --------------------------------
                            # СООБЩЕНИЕ СИНДИ — СЛЕВА
                            # --------------------------------

                            hbox:
                                xfill True
                                spacing 10

                                # Аватар Синди
                                add "messenger_cindy_avatar":
                                    xysize (48, 48)
                                    yalign 0.2

                                # Облачко сообщения
                                frame:
                                    xmaximum 390

                                    background Frame("images/other/chat_bubble_cindy.png", 18, 18, 18, 18)
                                    padding (16, 12)

                                    text msg["text"]:
                                        size 25
                                        color "#ffffff"

                        else:

                            # --------------------------------
                            # СООБЩЕНИЕ СТИВА — СПРАВА
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

                textbutton "Продолжить  →":
                    xalign 0.5
                    yalign 0.5

                    text_size 25

                    action Return()

    # Пробел выполняет то же действие, что и кнопка
    key "K_SPACE" action Return()


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

    call screen messenger_chat(chat_messages)

    # --------------------------------------------------------
    # СООБЩЕНИЕ 2
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Steve",
        "text": "Привет! Нет, как раз собирался заканчивать дела."
    })

    call screen messenger_chat(chat_messages)

    # --------------------------------------------------------
    # СООБЩЕНИЕ 3
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Cindy",
        "text": "Просто захотелось с кем-нибудь поговорить."
    })

    call screen messenger_chat(chat_messages)

    # --------------------------------------------------------
    # СООБЩЕНИЕ 4 — ПРОВЕРКА ДЛИННОГО ТЕКСТА
    # --------------------------------------------------------

    $ chat_messages.append({
        "sender": "Steve",
        "text": "Конечно, можешь написать мне. Я пока не собираюсь спать. Как прошёл твой день? Всё в порядке?"
    })

    call screen messenger_chat(chat_messages)

    # --------------------------------------------------------
    # ЗАВЕРШЕНИЕ ТЕСТА
    # --------------------------------------------------------

    "Конец тестовой переписки."

    return
