# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Grage = Character('Грег', color="#c8ffc8")
define Cindy = Character('Синди', color="#dcaa21")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


transform bg_home_outside:
    xysize (1920, 1080)
transform bg_home:
    xysize (1920, 1080)

image one_hour_letter = "images/other/one_hour_letter.png"

screen one_hour_later_wait():
    modal True

    timer 2.0 action Return()
    key "mouseup_1" action Return()
    key "K_SPACE" action Return()

screen story_route_choice():
    modal True

    add Solid("#000000")

    text "Выберите, чью историю продолжить":
        xalign 0.5
        yalign 0.08

    imagebutton:
        idle "images/sprites/greg_phone_skin.png"
        hover "images/sprites/greg_phone_skin.png"
        action Return("greg")
        xalign 0.25
        yalign 0.5
        at phone_choice_image

    imagebutton:
        idle "images/sprites/cindy_phone_skin.png"
        hover "images/sprites/cindy_phone_skin.png"
        action Return("cindy")
        xalign 0.75
        yalign 0.5
        at phone_choice_image

transform phone_choice_image:
    zoom 0.58

# Игра начинается здесь:

label splashscreen:
    scene black with fade
    pause 1.0
    show logo_hg:
        zoom 0.25
        xalign 0.5
        yalign 0.5
    with fade
    pause 3
    scene black with fade
    return


label start:

    scene bg_home_outside at bg_home_outside with fade

    Grage "Ещё один день позади."

    Grage "Три встречи, два срочных отчёта и клиент, который, кажется, считает, что у меня нет ничего важнее его проблем."

    Grage "По крайней мере, сегодня я успел закончить всё до вечера."

    Grage "Почти всё."

    scene bg_home at bg_home with fade

    Cindy "— Грег, это ты?"

    Grage "— Нет, почтальон. Решил остаться на ужин."

    show wife_home:
        zoom 0.5
        xalign 0.0
        yalign 1.0
    with fade

    Cindy "— Очень смешно. Тогда почтальон, помой руки. Ужин почти готов."

    Grage "— О я очень голоден! Кстати, милая, на десерт я полагаю у меня будешь ты?"

    Cindy "— Ох, Грег, я помню, что обещала тебе сегодня секс. Тебе лучше поторопиться, уже поздно и я хочу спать. Дети не дождались тебя и уже спят."

    Grage "— Прости, дорогая... Снова пришлось задержаться на работе... конец месяца, сама понимаешь, нужно сдать все отчеты."

    Cindy "— Не парся, я уже привыкла, так каждый месяц. Я подумываю, не устроиться ли мне наработу. Осточертело сидеть в четырех стенах... Ладно, поторопись, буду ждать тебя в спальне и постараюсь не уснуть."

    Grage "— Милая, я молнией поем, затем в душ и к тебе!"

    call messenger_test

    scene one_hour_later with fade
    call screen one_hour_later_wait

    $ renpy.movie_cutscene("videos/w_greg_1.webm")

    call screen story_route_choice

    if _return == "greg":
        jump greg_story_line
    else:
        jump cindy_story_line

    return

label greg_story_line:
    $ chat_messages = []

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Привет, Френк! Как жизнь?"
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "Здорово, Грег. Да помаленьку."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Черт! Чувак, у меня вчера был обалденный секс с Синди! Мне нужно было с кем-то этим поделиться, а ты же мой лучший друг!"
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "О, мужик, это круто! Самец! Рад за вас с Синди, вы кажетесь идеальной парой, наверное, так оно и есть..."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Дружище, ты как будто чем-то опечален. У тебя все в порядке? Как Нэнси?"
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "Я не знаю, Грег. Я не хочу вдаваться в подробности, но у нас с Нэнси сейчас непростые времена. Я не хочу тебя грузить своими проблемами, но мне нужно с кем-то поговорить."
    })

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Френк, ты мой лучший друг. Я всегда готов тебя выслушать. Ты можешь мне доверять. Я не осужу тебя и не скажу никому о твоих проблемах. Рассказывай что случилось."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "У нас с Нэнси секса уже небыло несколько месяцев. Я не знаю, что делать. Я пытался поговорить с ней, но она постоянно отмахивается от меня и говорит, что у неё нет настроения. Я подозреваю, что у неё кто-то появился. Я не знаю, что делать. Я люблю её и не хочу терять. Я не хочу, чтобы она ушла от меня."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Чувак у меня с Синди тоже секс случается не часто, видимо это последствия долгого брака. Не думаю, что это это повод для измены. Я думаю, что тебе нужно поговорить с Нэнси и выяснить, что происходит. Может быть, она просто устала или у неё стресс на работе. Попробуй быть терпеливым и поддерживающим. Я уверен, что вы сможете решить ваши проблемы вместе."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "У нас с Нэнси секса уже небыло несколько месяцев. Я не знаю, что делать. Я пытался поговорить с ней, но она постоянно отмахивается от меня и говорит, что у неё нет настроения. Я подозреваю, что у неё кто-то появился. Я не знаю, что делать. Я люблю её и не хочу терять. Я не хочу, чтобы она ушла от меня."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "Ты не понимаешь, Грег. Нэнси в последнее время изменилась, ведет себя странно. Часто задерживается на работе. Стала одеваться по-другому, раньше она так не одевалась даже в те времена, когда мы только начали встречаться."
    })

    $ chat_messages.append({
        "sender": "Frank",
        "text": "nanasy_look.png",
        "image_link": True
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    if _return == "show_nansy_look":
        call screen nansy_look_viewer

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Нэнси выглядит шикарно!"
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    return

label cindy_story_line:
    return

# TODO: сделать так, чтобы после окончания видео сразу начинался следующий диалог, без необходимости нажимать на экран.