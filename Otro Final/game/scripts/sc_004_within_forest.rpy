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
    call playerTOfairy
    girl "¿Has visto eso? ¡Verde!"
    girl "Ahí hay unos brotes en el suelo, y ahí un pequeño arbusto"
    girl "¡Y ahí hay más!"
    call playerFROMfairy
    fairy "Sí, lo veo."
    fairy "¿No te resulta... Curioso?"
    call NOplayer_fairy
    "{i}La niña paró un momento y se quedó pensando. Miró a su alrededor, dio un par de pasos y volvió a mirar a Sairina.{\i}"
    call playerTOfairy
    girl "¿Cómo es posible que aquí en el interior, que hay todavía menos luz, haya más plantas que afuera?"
    call playerFROMfairy
    fairy "Eso mismo me estaba preguntando yo."
    call playerTOfairy
    girl "Bueno, seguro que si seguimos avanzando, terminaremos descubriéndolo."
    "..."
    call NOplayer_fairy
    "{i}Éstel siguió avanzando con paso firme, pero entonces, sólo unos instantes después, Sairina se colocó rápidamente delante de ella"
    call playerFROMfairy
    fairy "¡Detente! Creo que he visto algo."
    fairy "No, no. No digas nada. Sígueme."
    call NOplayer_fairy
    "{i}Ella miró a Sairina con los ojos muy abiertos y asintió con la cabeza siguiéndola hasta acercarse hasta el tronco de un grueso árbol que había cerca{\i}"
    call playerFROMfairy
    fairy "Mira allí. Con cuidado. Hay algo."
    call playerTOfairy
    girl "¿Crees que nos ha visto?"
    call playerFROMfairy
    fairy "No, creo que no. Parece que camina de un lado a otro."
    call playerTOfairy
    girl "¿Y ahora que hacemos?"
    call playerFROMfairy
    fairy "Yo me elevaré un poco y buscaré un lugar seguro sobre el que pasar."
    fairy "Después tendrás que venir hacia mí."
    fairy "Cuando vengas hacia mi, sé precavida. Da un pasa cada vez, y espera a ver que hace la criatura."
    fairy "Entonces da otro paso y vuelve a esperar."
    fairy "Los árboles pueden ayudarte a llegar."
    fairy "Intenta no acercarte demasiado a la criatura."
    call playerTOfairy
    girl "Va... Vale."
    girl "Ir pasito a pasito y no acercarme mucho a la criatura. ¡Hecho!"
    
    jump minigame_1
