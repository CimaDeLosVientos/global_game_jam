label sc_004_within_forest:
    window hide
    scene bg text forest 1 with fade
    nvl_narrator "{enf}Así, la joven y la naira se internaron en el Bosque Marchito.{/enf}"
    nvl_narrator "{enf}Caminaron entre los oscuros árboles de desnudas ramas y sobre el suelo cubierto de vegetación seca.{/enf}"
    nvl_narrator "{enf}Estaba bastante oscuro, pero la luz que emitía Sairina les permitía ver lo suficiente como para poder seguir avanzando.{/enf}"
    nvl_narrator "{enf}El lugar era intranquilamente silencioso, lóbrego a pesar de ser pleno día.{/enf}"
    nvl_narrator "{enf}Pero Éstel avanzaba convencida, intentando que su preocupación no venciera a su entusiasmo.{/enf}"
    nvl_narrator "{enf}Entonces, al poco de llevar caminando, la naira y la joven observaron algo muy curioso.{/enf}"
    nvl_narrator "{enf}Los primeros brotes de hierba verde,\nlas primeras solitarias hojas en alguna rama de un árbol...{/enf}"
    nvl_narrator "{enf}Poco a poco... Muy poco a poco...\ncomenzaban a ver algún signo de vida, aunque muy leve aún.{/enf}"
    nvl_narrator "{enf}La joven estaba entusiasmada con el hallazgo, pues la convencía para seguir adelante y aumentaba su optimismo.{/enf}"
    nvl_narrator "{enf}Quizá demasiado...{/enf}"
    scene bg forest dark with fade
    call playerTOfairy from _call_playerTOfairy_40
    girl "¿Has visto eso? ¡Verde!"
    girl "Ahí hay unos brotes en el suelo...{w} y ahí un pequeño arbusto"
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
    call playerFROMfairy
    fairy "..."
    call NOplayer_fairy from _call_NOplayer_fairy_5
    "{i}Éstel siguió avanzando con paso firme, pero entonces, sólo unos instantes después, Sairina se colocó rápidamente delante de ella."
    call playerFROMfairy from _call_playerFROMfairy_39
    fairy "¡Detente!{w} Creo que he visto algo."
    fairy "No, no.{w} No digas nada.{w} Sígueme."
    call NOplayer_fairy from _call_NOplayer_fairy_6
    "{i}Ella miró a Sairina con los ojos muy abiertos y asintió con la cabeza, siguiéndola hasta el tronco de un grueso árbol que había cerca.{\i}"
    call playerFROMfairy from _call_playerFROMfairy_40
    fairy "Mira allí.{w} Con cuidado.{w} Hay algo."
    call playerTOfairy from _call_playerTOfairy_43
    girl "¿Crees que nos ha visto?"
    call playerFROMfairy from _call_playerFROMfairy_41
    fairy "No, creo que no.{w} Parece que deambula de un lado a otro."
    call playerTOfairy from _call_playerTOfairy_44
    girl "¿Y ahora qué hacemos?"
    call playerFROMfairy from _call_playerFROMfairy_42
    fairy "Yo me elevaré un poco y buscaré un lugar seguro por el que pasar."
    fairy "Después tendrás que venir hacia mí."
    fairy "Cuando vengas hacia mi, sé precavida. Da un paso cada vez y observa lo que hace la criatura."
    fairy "Entonces da otro paso y vuelve a observar."
    fairy "Los árboles pueden ayudarte a llegar."
    fairy "Intenta no acercarte demasiado a la criatura."
    call playerTOfairy from _call_playerTOfairy_45
    girl "Va... Vale."
    girl "Ir pasito a pasito y no acercarme mucho a la criatura... ¡Hecho!"
    
    jump minigame_1
