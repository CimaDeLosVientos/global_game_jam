label sc_004_within_forest:
    window hide
    scene bg text forest 1 with fade
    nvl_narrator "{enf}Así, la joven y la Naira se internaron en el Bosque Marchito{/enf}"
    nvl_narrator "{enf}Caminaron entre los oscuros árboles de desnudas ramas y suelo cubierto de vegetación seca{/enf}"
    nvl_narrator "{enf}Estaba bastante oscuro, pero la luz que emitía Sairina les permitía ver lo suficiente como para poder seguir avanzando{/enf}"
    nvl_narrator "{enf}El lugar era intranquilamente silencioso, lóbrego a pesar de ser pleno día{/enf}"
    nvl_narrator "{enf}Pero Éstel avanzaba convencida intentando que su entusiasmo no venciera a su preocupación{/enf}"
    nvl_narrator "{enf}Entonces, al poco de llevar caminando, el Naira y la joven observaron algo muy curioso{/enf}"
    nvl_narrator "{enf}Los primeros brotes de hierba verde, las primeras solitarias hojas en alguna rama de un árbol{/enf}"
    nvl_narrator "{enf}Poco a poco. Muy poco a poco, comenzaban a ver algún signo de vida, aunque muy leve aún{/enf}"
    nvl_narrator "{enf}La joven estaba entusiasmada con el hallazgo, la convencía para seguir adelante y aumentaba su entusiasmo{/enf}"
    nvl_narrator "{enf}Quizá demasiado{/enf}"
    scene bg forest dark with fade
    call playerTOfairy from _call_playerTOfairy_40
    girl "¿Has visto eso? ¡Verde!"
    girl "Ahí hay unos brotes en el suelo, y ahí un pequeño arbusto"
    girl "¡Y ahí hay más!"
    call playerFROMfairy from _call_playerFROMfairy_37
    fairy "Sí, lo veo."
    fairy "¿No te resulta... Curioso?"
    call NOplayer_fairy from _call_NOplayer_fairy_4
    "{i}La niña paró un momento y se quedó pensando. Miró a su alrededor, dio un par de pasos y volvió a mirar a Sairina.{\i}"
    call playerTOfairy from _call_playerTOfairy_41
    girl "¿Cómo es posible que aquí en el interior, que hay todavía menos luz, haya más plantas que afuera?"
    call playerFROMfairy from _call_playerFROMfairy_38
    fairy "Eso mismo me estaba preguntando yo."
    call playerTOfairy from _call_playerTOfairy_42
    girl "Bueno, seguro que si seguimos avanzando, terminaremos descubriéndolo."
    "..."
    call NOplayer_fairy from _call_NOplayer_fairy_5
    "{i}Éstel siguió avanzando con paso firme, pero entonces, sólo unos instantes después, Sairina se colocó rápidamente delante de ella"
    call playerFROMfairy from _call_playerFROMfairy_39
    fairy "¡Detente! Creo que he visto algo."
    fairy "No, no. No digas nada. Sígueme."
    call NOplayer_fairy from _call_NOplayer_fairy_6
    "{i}Ella miró a Sairina con los ojos muy abiertos y asintió con la cabeza siguiéndola hasta acercarse hasta el tronco de un grueso árbol que había cerca{\i}"
    call playerFROMfairy from _call_playerFROMfairy_40
    fairy "Mira allí. Con cuidado. Hay algo."
    call playerTOfairy from _call_playerTOfairy_43
    girl "¿Crees que nos ha visto?"
    call playerFROMfairy from _call_playerFROMfairy_41
    fairy "No, creo que no. Parece que camina de un lado a otro."
    call playerTOfairy from _call_playerTOfairy_44
    girl "¿Y ahora que hacemos?"
    call playerFROMfairy from _call_playerFROMfairy_42
    fairy "Yo me elevaré un poco y buscaré un lugar seguro sobre el que pasar."
    fairy "Después tendrás que venir hacia mí."
    fairy "Cuando vengas hacia mi, sé precavida. Da un pasa cada vez, y espera a ver que hace la criatura."
    fairy "Entonces da otro paso y vuelve a esperar."
    fairy "Los árboles pueden ayudarte a llegar."
    fairy "Intenta no acercarte demasiado a la criatura."
    call playerTOfairy from _call_playerTOfairy_45
    girl "Va... Vale."
    girl "Ir pasito a pasito y no acercarme mucho a la criatura. ¡Hecho!"
    
    jump minigame_1
