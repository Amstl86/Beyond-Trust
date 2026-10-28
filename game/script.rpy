# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Grage = Character('Грег', color="#c8ffc8")
define Cindy = Character('Синди', color="#dcaa21")
define MrJackson = Character('Мистер Джексон', color="#b7d7ff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


transform bg_home_outside:
    xysize (1920, 1080)
transform bg_home:
    xysize (1920, 1080)

image one_hour_letter = "images/other/one_hour_letter.png"
image next_day = "images/other/next_day.png"
image dismissal_office = "images/office_dismissal.png"
image mr_jackson = "images/sprites/mr_jackson.png"

screen one_hour_later_wait():
    modal True

    timer 2.0 action Return()
    key "mouseup_1" action Return()
    key "K_SPACE" action Return()

screen greg_phone_video():
    modal True

    add "greg_phone_skin":
        zoom 0.58
        xalign 0.5
        yalign 0.5

    add Solid("#000"):
        xpos 761
        ypos 138
        xsize 397
        ysize 813

    add Movie(play="videos/what_cuckold.webm", size=(397, 223), loop=False):
        xpos 761
        ypos 433

    timer 127.0 action Return()
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

    # call messenger_test

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

    $ chat_messages.append({
        "sender": "Frank",
        "text": "В этом и дело! Она раньше так не наряжалась и не красилась. Даже для меня..."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Друг, я считаю ты себя накручиваешь. Нэнси просто хочет хорошо выглядеть, это свойственно каждой женщине."
    })

    call screen messenger_chat(chat_messages, "Френк", "Frank")

    $ chat_messages.append({
        "sender": "Frank",
        "text": "Ладно... может ты и прав. Просто я не хочу ее потерять, но и куколдом быть тоже не желаю."
    })

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Кем? Куколдом?"
    })

    $ chat_messages.append({
        "sender": "Frank",
        "text": "Ты не знаешь кто такие куколды? Это года жена заводит себе трахаря, а муж смиренно это терпит. Там, конечно, сложнее определение, но суть такова. Ладно мне нужно вернуться к работе, Спасибо, что выслушал."
    })

    $ chat_messages.append({
        "sender": "Greg",
        "text": "Удачи чувак и не переживай, все будет хорошо. Если что, я всегда готов тебя выслушать."
    })

    $ greg_frank_messages = list(chat_messages)

    scene black
    show greg_phone_skin:
        zoom 0.58
        xalign 0.5
        yalign 0.5
    with fade

    Grage "Что за куколд? Может погуглить..."

    Grage "Так... вот какое-то видео... глянем."

    call screen greg_phone_video

    Grage "Ну нет! Это слишком унизительно для мужика... Хотя женщины выглядят очень довольными."

    Grage "Я никогда бы не согласился на такое унижение."

    Grage "Чёрт, у меня что, стояк? Надо подумать о чём-то, чтобы остыть."

    Grage "Эти женщины меня возбудили, а не то, что они делали с мужьями..."

    Grage "Ладно, надо браться за работу."

    scene next_day with fade
    pause 2.0
    scene bg_work with fade

    Grage "Хорошо. Что происходит? Почему собраны мои вещи?"

    show boss:
        zoom 1.2
        xalign 0.88
        yalign 1.0
    with dissolve

    MrJackson "Грег, спасибо, что пришёл. Я сразу перейду к делу. Компания пересматривает структуру отдела."

    MrJackson "Это не связано с проектом или результатами твоей работы. Мы упраздняем несколько должностей, включая твою."

    Grage "Подожди. Что значит «упраздняем»? Я здесь семь лет."

    MrJackson "Мы понимаем, что это неожиданно. Сегодня мы передадим тебе документы по выходному пособию, страховке и окончательному расчёту."

    Grage "То есть решение уже принято?"

    MrJackson "Да. Мне жаль, Грег."

    Grage "И вы решили сообщить мне об этом сегодня? Без единого разговора до этого?"

    MrJackson "Решение принято на уровне компании. Я не могу изменить его."

    call greg_cindy_chat

    call greg_phone_scene

    return

label greg_cindy_chat:
    $ chat_messages = []
    $ greg_cindy_messages = [
        {"sender": "Greg", "text": "Привет, милая. Как дела?"},
        {"sender": "Cindy", "text": "Привет, Грег. Просто бездельничаю дома."},
        {"sender": "Cindy", "text": "Что-то случилось?"},
        {"sender": "Greg", "text": "Сегодня меня уволили с работы."},
        {"sender": "Cindy", "text": "О боже! Я так сожалею, Грег. Ты в порядке?"},
        {"sender": "Greg", "text": "Да. Просто… не ожидал такого."},
        {"sender": "Cindy", "text": "Тебе дали выходное пособие?"},
        {"sender": "Greg", "text": "Да. Но это не значит, что мы можем спокойно сидеть и ждать. Ипотека, счета, расходы на детей… Нужно будет быстро найти что-то новое."},
        {"sender": "Cindy", "text": "Конечно. Мы разберёмся."},
        {"sender": "Greg", "text": "Я разберусь."},
        {"sender": "Cindy", "text": "Я знаю, что ты хочешь всё решить сам. Но я сказала «мы», а не «ты»."},
        {"sender": "Greg", "text": "Я не это имел в виду."},
        {"sender": "Cindy", "text": "Хорошо."},
        {"sender": "Cindy", "text": "Я думаю, мне тоже стоит поискать работу."},
        {"sender": "Greg", "text": "Зачем? Я же сказал, что буду искать."},
        {"sender": "Cindy", "text": "Я слышала. Но поиски работы могут затянуться. А так у нас будет хотя бы ещё один источник дохода."},
        {"sender": "Greg", "text": "Ты и так занята детьми и домом."},
        {"sender": "Cindy", "text": "Дети ходят в школу. И я не предлагаю работать по двенадцать часов в день."},
        {"sender": "Greg", "text": "Я не говорю, что ты не справишься."},
        {"sender": "Cindy", "text": "Тогда в чём проблема?"},
        {"sender": "Greg", "text": "Хорошо. Посмотрим, что можно найти."},
        {"sender": "Cindy", "text": "Я уже кое о чём подумала."},
        {"sender": "Cindy", "text": "Мне уже давно надоело сидеть дома одной."},
        {"sender": "Greg", "text": "У тебя уже есть варианты на примете?"},
        {"sender": "Cindy", "text": "Помнишь Беллу? Она как-то говорила, что может предложить мне подработку."},
        {"sender": "Greg", "text": "Белла? Та самая Белла?"},
        {"sender": "Cindy", "text": "Да, та самая."},
        {"sender": "Greg", "text": "И что за работа?"},
        {"sender": "Cindy", "text": "Вот в этом и дело. Она сказала, что платят хорошо, но толком не объяснила, чем именно нужно заниматься."},
        {"sender": "Greg", "text": "И ты собираешься соглашаться на работу, о которой ничего не знаешь?"},
        {"sender": "Cindy", "text": "Я собираюсь спросить. Это разные вещи."},
        {"sender": "Greg", "text": "Она всегда была… скажем так, не самым надёжным человеком."},
        {"sender": "Cindy", "text": "Ты никогда её не любил."},
        {"sender": "Greg", "text": "Мне не нравится, что она постоянно что-то затевает, а потом остальные должны разбираться с последствиями."},
        {"sender": "Cindy", "text": "Возможно. Но ты не знаешь, что она предлагает сейчас."},
        {"sender": "Cindy", "text": "Я не собираюсь соглашаться вслепую. Сначала выясню условия, обязанности и график. Если предложение окажется странным — откажусь."},
        {"sender": "Greg", "text": "Ладно. Только будь осторожна."},
        {"sender": "Cindy", "text": "Я умею задавать вопросы, Грег."},
        {"sender": "Cindy", "text": "В любом случае Белла сейчас в отпуске и приедет только через три недели. Может, тебе стоит спросить у Стэна насчёт работы?"},
        {"sender": "Greg", "text": "Работать в автосервисе?"},
        {"sender": "Cindy", "text": "В нашем положении это не худший вариант. Он твой брат и, возможно, найдёт тебе не грязную работу."},
        {"sender": "Greg", "text": "Ты права. Я сейчас напишу ему."},
    ]

    python:
        for message in greg_cindy_messages:
            chat_messages.append(message)
            renpy.call_screen("messenger_chat", chat_messages, "Синди", "Cindy")

    return

label greg_phone_scene:
label greg_phone_home:
    call screen greg_phone_home_screen

    if _return == "messenger":
        jump greg_messenger_inbox
    elif _return == "photogram":
        call screen greg_photogram_screen
        jump greg_phone_home
    elif _return == "close":
        return
    else:
        jump greg_phone_home

label greg_messenger_inbox:
    call screen greg_messenger_inbox_screen

    if _return == "home":
        jump greg_phone_home
    elif _return == "Cindy":
        call screen messenger_chat(greg_cindy_messages, "Синди", "Cindy", True)
        jump greg_messenger_inbox
    elif _return == "Frank":
        call screen messenger_chat(greg_frank_messages, "Френк", "Frank", True)
        if _return == "show_nansy_look":
            call screen nansy_look_viewer
        jump greg_messenger_inbox
    elif _return == "Stan":
        call screen messenger_chat([], "Стэн", "Stan", True)
        jump greg_messenger_inbox
    else:
        jump greg_messenger_inbox

label cindy_story_line:
    return

# TODO: сделать так, чтобы после окончания видео сразу начинался следующий диалог, без необходимости нажимать на экран.