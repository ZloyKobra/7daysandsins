define gg = Character("[gg_name]", color="#49df7b") # , callback=name_callback, cb_name="gg"
define e = Character('Эйлин', color="#c8ffc8")
define noname = Character("...", color="#ffac68")
define laziness = Character("Лень", color="#dd7be6")
define hunger = Character("Голод", color="#fa8a2e")
define greed = Character("Жадность", color="#5153e9")
define lust = Character("Похоть", color="#ff488e")
define envy = Character("Зависть", color="#67edf1")
define pride = Character("Гордыня", color="#fcff32")
define anger = Character("Гнев", color="#d30000")

image gg calm1 = At("gg stand", sprite_highlight("gg"))
image gg angry_ = At("gg angry", sprite_highlight("gg"))
image gg facepalm_  = At("gg facepalm", sprite_highlight("gg"))
image gg speak_ = At("gg speak", sprite_highlight("gg"))
image gg calm2 = At("gg stand1", sprite_highlight("gg"))
image gg think_ = At("gg think", sprite_highlight("gg"))
image gg shock_ = At("gg shock", sprite_highlight("gg"))
image gg talktophone_ = At("gg talkphone", sprite_highlight("gg"))
image gg looktophone_ = At("gg lookphone", sprite_highlight("gg"))
image gg sleep_ = At("gg sleep", sprite_highlight("gg"))
image gg sleep_phone = At("sleep_phone gg", sprite_highlight("gg"))


image laziness calm1 = At("laziness stand1", sprite_highlight("laziness"))
image laziness calm2 = At("laziness stand2", sprite_highlight("laziness"))
image laziness speak_ = At("laziness speak", sprite_highlight("laziness"))
image laziness angry_ = At("laziness angry", sprite_highlight("laziness"))
image laziness down_ = At("laziness sleep", sprite_highlight("laziness"))

image greed calm1 = At("greed stand1", sprite_highlight("greed"))
image greed calm2 = At("greed stand2", sprite_highlight("greed"))
image greed angry_1 = At("greed angry1", sprite_highlight("greed"))
image greed angry_2 = At("greed angry2", sprite_highlight("greed"))
image greed question_1 = At("greed question1", sprite_highlight("greed"))
image greed question_1 = At("greed question1", sprite_highlight("greed"))
image greed facepalm_ = At("greed facepalm", sprite_highlight("greed"))

image anger angry_ = At("anger angry", sprite_highlight("anger"))
image anger fun_ = At("anger fun", sprite_highlight("anger"))
image anger speak_ = At("anger speak", sprite_highlight("anger"))
image anger calm1 = At("anger stand1", sprite_highlight("anger"))
image anger calm2 = At("anger stand2", sprite_highlight("anger"))
image anger calm3 = At("anger stand3", sprite_highlight("anger"))


define gg_phone = Character("[gg_name]", kind=nvl, image="gg stand")
define gendir_phone = Character("Гендир", kind=nvl)

# image laziness calm1 = At("laziness stand", sprite_highlight("laziness"))
# и т.д.


