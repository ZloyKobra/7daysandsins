label day1_begin:
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_1
    pause 5.0
    jump day1


label day1:
    with fade
    scene bg ggroom_bright
    "{bt=100}10:26 утра☠️{/bt}"
    show gg calm2

    gg "Нуууу... Так, вроде я составил не плохой план на мои ближайшие 7 дней. Если я не буду ни на что лишнее отвлекаться, то могу закончить свой проект вовремя и получить 5"
    gg "Я молодец!!! Сколько время? 10:26..."
    gg "Нууу в моем плане нет точного времени, когда начать, да и я люблю точность, так что могу отдохнуть ровно до 11, а потом начну"
    gg "эти 34 минуты все равно ничего не решат\n{cps=5}...{/cps}"
    gg "А может мне все же сейчас начать работу? Быстрей начну, быстрей закончу."
    noname "А ты знаешь, что отдых в работе тоже важен?"
    gg "Кто здесь?!"

    show gg calm1:
        xalign 0.15
        yalign 1.0
    with move
    # show laziness calm1 at right

    laziness "Не бойся, я твой друг и защитник – Лень, не хочу, чтобы ты перетрудился"
    # laziness "Бу, испугался, не бойся это я твой друг!"
    gg "Защитник?"
    laziness "Конечно, кто-то же должен защищать людей от труда. Это обязанность лежит на моих хрупких плечах."

    menu:
        "Мда, мне бы не помешала такая защита":
            jump day1_choice_left_1
        "Спасибо, но не стоит, я буквально решил немножко отдохнуть перед началом":
            jump day1_choice_right_1


label day1_choice_left_1:
    laziness "Тогда давай я тебе помогу! Расслабься, ляг удобнее на подушку, включи телефон посмотри новостную ленту."
    laziness "Нравиться?"
    menu:
        "Очень. О, у “Милых котиков” новая запись!!! А NV выпустил новый трек!":
            jump day1_choice_left_2
        "Не особо, да и время близиться к 11, надо вставать и начинать работу.":
            laziness "Полежи еще немного"
            menu:
                "Ладно":
                    jump day1_choice_left_2
                "Я отдохнул, пора за дело":
                    jump day1_choice_right_2


label day1_choice_left_2:
    laziness "Это хорошо, тебя в сон не тянет?"
    gg "Есть немного..."
    laziness "Тогда давай я тебе включу колыбельную и ты отоспишься, на свежую голову всегда приятней работать."
    menu:
        "Давай":
            "Лень начинает играть на какой-то шарманке..."
            # сюды музыку
            "Ты засыпаешь, Лень расстворяется..."
        "Нет, время к 11 подходит пора вставать.":
            jump day1_choice_right_2


label day1_choice_right_1:
    laziness "Немножко можно превратить и во множко, почему бы тебе так и не сделать."
    gg "Мне нужно закончить все вовремя, я хочу получить 5 и спокойно уйти на каникулы."
    laziness "Но отдых тоже ведь не помешает? Согласись с этим."
    menu:
        "Согласен, пожалуй мне стоит отдохнуть.":
            jump day1_choice_left_1
        "Согласен, но отдых должен быть умеренным.":
            laziness "А твой отдых сейчас умеренный?"
            gg "Нет, пожалуй я все таки начну работать сейчас."
            jump day1_choice_right_2


label day1_choice_right_2:
    laziness "Ты не знаешь, что теряешь. Не надо останся на кровати."
    gg "Нет, мне есть чем заняться уходи."
    laziness "Неееееееет!!!"
    "Лень рассыпается, а ты садишься за работу."
    jump day2_begin