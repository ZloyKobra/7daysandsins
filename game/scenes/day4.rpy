label day4_begin:
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_4
    pause 5.0
    jump day4


label day4:
    scene bg ggroom_light
    show gg calm1
    with fade
    gg "Фух... Вроде пока работа не плохо идет, и пока ничего не отвлекает"
    play sound "audio/sounds/message sound.mp3"
    # звук уведомления на телефон
    show gg looktophone_
    gg "Оуу, кто мне пишет? Какая-то Диана интересно. Может ей сейчас ответить"
    menu:
        "Ну девчонки мне редко сами пишут, надо брать пока есть такая возможность":
            jump day4_choice_left_1
        "Не, попозже, сейчас я работаю":
            gg "На чем я остановился? А. точно, нужно написать новый метод..."
            # звук уведомления 5 раз
            play sound "audio/sounds/5_message_sound.mp3"
            menu:
                "Ну девчонки мне редко сами пишут, надо брать пока есть такая возможность":
                    jump day4_choice_left_1
                "Не, она через чур настырная, пожалуй кину ее в чс":
                    "Ты кидаешь её в чс, и продолжаешь работать"
                    jump day5_begin
         

label day4_choice_left_1:
    gg "Вау, а она симпатичная."
    # демонтрация экрана телефона
    lust "Привет, а ты симпатичный мальчик, не хочешь познакомиться?"
    gg 'Да, хочу, может сходим прогуляться в следующие выходные'
    lust "Ммммммм, до них еще ждать и ждать, это целая вечность"
    gg 'Хорошо, и когда ты хочешь встретиться?'
    lust "Давай сейчас, судя по твоему профилю, я нахожусь в километре от тебя. Давай встретиться, я очень хочу {cps=5}...{/cps} познакомиться."
    menu:
        "Ладно, ну и куда ты хочешь пойти?":
            jump day4_choice_left_2
        "Прости, но раньше следующей недели я не могу":
            lust "Уууааааа, за что ты так со мной, я так хочу тебя увидеть, может быть, это любовь с первого взгляда?"
            lust "Не рушь моё и так многострадальное сердце, меня столько парней бросало, а теперь и ты, не хочешь просто встретиться и погулять часик со мной. Я НИКОМУ НЕ НРАВЛЮСЬ :("
            menu:
                "Ладно, прости, куда пойдём?":
                    jump day4_choice_left_2
                "Прости, я занят, если я тебе не подхожу, ищи другого ухажера, боюсь я слишком погружен в работу, поэтому не смогу встретиться сегодня. Только через неделю":
                    jump day4_choice_right_1_phone

label day4_choice_left_2:
    lust "Нууу, не знаю может ты что-нибудь предложишь?"
    gg 'Хмммм ... ладно, знаешь кофешку на углу улицы Универа 12'
    lust "Да, буду там через 30 минут, до встречи 😘"
    gg "До встречи"
    jump day4_choice_left_3


label day4_choice_left_3:
    scene black
    # звук из спанчбоба. спустя/прошло 2 часа
    "Ты пришел на место встречи. Прошло 2 часа"
    scene bg coffeeroom with fade
    show gg calm1
    gg "Блин, где ее носит?"
    play sound "audio/sounds/advent sin.mp3"
    lust "Привет, потерял меня милый?"
    gg "Оууууу"
    lust "Нравлюсь?"
    menu:
        "Очень":
            lust "Хочешь потрогать мои ... руки, солнышко"
        "Какие у тебя большие ... и красивые глаза":
            lust "Хочешь потрогать мои ... руки, солнышко"
    menu:
        "Да":
            lust "А ощутить вкус моих клубничных губ"
        "Нет":
            lust "А ощутить вкус моих клубничных губ"
    menu:
        "Очень, сладкая":
            lust "А почувствовать мое тепло"
        "Прости, я по малине":
            lust "А почувствовать мое тепло"
    menu:
        "Очень, моя милая":
            lust "Поехали ко мне"
            menu: 
                "Поехали":
                    jump day4_choice_left_4
                "Прости, но мы договаривались на один ча...":
                    lust "Неужели ты не хочешь продолжения?"
                    menu:
                        "Хочу":
                            jump day4_choice_left_4
                        "Нет, прости, мое время вышло, я пошел работать":
                            jump day4_choice_right_2
        "Ты на что мне намекаешь?":
            lust "Разве ты до сих пор не понял, дурашка. Ха-ха-ха"
            gg 'Нет, и знаешь что, мое свободное время вышло, ине пора домой'
            jump day4_choice_right_2

label day4_choice_left_4:
    gg "Поехали"
    "Ты уезжаешь с ней"
    $ difficult += 1
    jump day5_begin



label day4_choice_right_1_phone:
    lust "Ну и пошел ты на ***, поршивый *********, найду себе более *********, чем ты, а твоя внешность..."
    # выключение телефона
    show gg facepalm_
    gg "Мда, сильно я ее расстроил, сразу свое истинное лицо показала"
    gg "Если уж искать девушку, то явно не такую. Так, добавить в чс... Прекрасно, так на чем я остановился. А точно..."
    "Ты кидаешь её в чс, и продолжаешь работать"
    jump day5_begin

label day4_choice_right_1:
    # show lust_angry
    lust "Ну и пошел ты на ***, поршивый *********, найду себе более *********, чем ты, а твоя внешность..."
    show gg facepalm_
    gg "Мда, сильно я ее расстроил, сразу свое истинное лицо показала"
    gg "Столько времени из-за этой пошлятины убил, в следующий раз найду нормальную девушку"
    "Ты возвращаешься домой, и продолжаешь работать"
    jump day5_begin


label day4_choice_right_2:
    lust "Ты даже не знаешь, что упускаешь, поехали со мной, прошу, мне одной одиноко"
    gg "Нет, всего хорошего"
    jump day4_choice_right_1