label day6_begin:
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_6
    pause 5.0
    jump day6


label day6:
    scene bg ggroom_light
    show gg calm1
    with fade
    gg "Так, ну давай, посмотрим, как ты работаешь ... старт ..."
    gg "ЮХУ!!! УРА!!! ОН РАБОТАЕТ!!!! РАБОТАЕТ!!!"
    gg "Какой же я молодец, осталось только защитить все"
    # звук уведомления на телефоне
    gg "Ой кто-то пишет"
    # демонстрация экрана телефона
    noname "“Привет, я знаю,что ты уже почти закончил свою работу, можешь мне помочь, я просто еще ничего не успел сделать”"
    gg "Еееее мое, а паренек влип, оно это быстро не сделает ... может ему скинуть часть своей рабо ..."
    noname "А почему ты ему должен что- то кидать, ты молодец, такой большой проект и всего а несколько дней, браво, но не уже ли ты с кем то им поделишься"
    gg "Кто ты?"
    pride "Я твоя гордыня, пришла уберечь тебя от этой ошибки"
    gg "Какой?"
    pride "Ты хочешь поделиться с ним своей работой?"
    menu:
        "Нет конечно, он ничего не делал целый сем, тут я ни чем не помогу":
            jump day6_choice_left_1
        "Да, а что такого, не обязательно поделиться, можно что-то подсказать":
            pride "Да уж, свой великий труд ты ценить не умеешь, зачем оно тебе?"
            menu:
                "Ты прав, я как-то слишком по-доброму к этмому отнесся":
                    jump day6_choice_left_1
                "Да ничего не случиться, я просто подскажу ему пару моментов, и все":
                    gg "Так, он готов созвониться сейчас, позже полежу"
                    pride "Ты хорошо подумал, сейчас под него прогнешься, он потом не отстанет,  код твой попросит и прочее"
                    menu:
                        "Ты прав, я как-то слишком по-доброму к этому отнесся":
                            jump day6_choice_left_1
                        "Ой, уйди уже от сюда, только мешаешь":
                            "Гордыня распадается. Ты помогаешь челику с работой"
                            jump day7_begin


label day6_choice_left_1:
    pride "Вот, правильная позиция, теперь напиши ему об этом"
    # сообщение в телефон
    gg "Привет, прости, но я тебе не смогу помочь"
    pride "Слишком мягко, он требует твою идеальную работу, и ты так отказываешь?"
    gg 'Да, а что?'
    pride "Добавь что-нибудь из серии, надо было в начале делать или то, что он дурак, и твоя работа не для него"
    menu:
        "Добавлю последние, звучит не плохо":
            jump day6_choice_left_2
        "Нет, это перебор, такое я писать не буду":
            pride "Почему? Мне кажется самое то"
            gg "Мне нет, мы все работаем над одним и тем же, не стоит ставить себя выше других, поэтому вали от сюда"
            "Гордыня распадается. Ты ложишься отдыхать"
            jump day7_begin

        

label day6_choice_left_2:
    # сообщение в телефон
    gg "... моей помощи ты не заслуживаешь, и вообще моя работа не для тебя"
    pride "Молодец! А теперь раз твоя работа идеальна, сделаешь ее еще раз"
    gg "Что?! Что ты сделал?! Где часть моего проекта?!"
    pride "Упс, вопросы не ко мне, но можешь обратиться к знающему"
    gg "К кому?"
    pride "К тому, кого ты сейчас отверг, а мне пора удачи"
    "Гордыня распадается"
    gg "Черт и что мне делать?"
    menu:
        "Может попробовать написать ему":
            gg "Привет, можешь пожалуйста помочь ..."
            gg "Он меня послал, ладно, заслуженно, пойду переделывать"
            "Ты садишься всё переделывать"
            $ difficult += 1
            jump day7_begin
        "Пойду все переделаю":
            $ difficult += 1
            jump day7_begin
