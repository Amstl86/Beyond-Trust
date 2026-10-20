# Первый этап интерфейса визуальной новеллы.
# Поместите этот файл в папку game/ вашего проекта Ren'Py.
# Префикс z_ помогает загружать переопределение после стандартного screens.rpy.

init -2:
    style vn_menu_button is button:
        xsize 440
        ysize 62
        xalign 0.5
        padding (22, 12)
        background Solid("#191919")
        hover_background Solid("#C84A4A")
        insensitive_background Solid("#191919")

    style vn_menu_button_text is button_text:
        size 28
        color "#F0F0F0"
        hover_color "#FFFFFF"
        insensitive_color "#666666"
        xalign 0.5
        yalign 0.5

    style vn_menu_title is text:
        size 48
        color "#F0F0F0"
        bold True
        text_align 0.5
        xalign 0.5

    style vn_menu_subtitle is text:
        size 18
        color "#AAAAAA"
        text_align 0.5
        xalign 0.5

screen main_menu():
    tag menu

    # Временный фон. Позже заменим на иллюстрацию главного меню.
    add Solid("#111111")

    # Небольшая декоративная линия под заголовком.
    frame:
        background Solid("#C84A4A")
        xsize 100
        ysize 3
        xalign 0.5
        ypos 0.285

    vbox:
        xalign 0.5
        ypos 0.17
        spacing 16

        text "НАЗВАНИЕ ИГРЫ" style "vn_menu_title"
        text "Визуальная новелла" style "vn_menu_subtitle"

    vbox:
        xalign 0.5
        yalign 0.62
        spacing 12

        textbutton "Новая игра" action Start() style "vn_menu_button" text_style "vn_menu_button_text"
        textbutton "Продолжить" action Continue() style "vn_menu_button" text_style "vn_menu_button_text"
        textbutton "Загрузить" action ShowMenu("load") style "vn_menu_button" text_style "vn_menu_button_text"
        textbutton "Настройки" action ShowMenu("preferences") style "vn_menu_button" text_style "vn_menu_button_text"
        textbutton "История" action ShowMenu("history") style "vn_menu_button" text_style "vn_menu_button_text"
        textbutton "Выход" action Quit(confirm=True) style "vn_menu_button" text_style "vn_menu_button_text"

    text "Версия разработки":
        size 14
        color "#666666"
        xalign 0.98
        yalign 0.98
