label sc_005_before_book:
    stop music fadeout 3.0
    scene bg forest dark with fade
    play music "music/Chrome en GP.mp3" fadein 3.0
    #"[director]"
    #"[winner]"
    call playerTOfairy from _call_playerTOfairy_1
    girl "Bien, lo he conseguido."
    call playerFROMfairy from _call_playerFROMfairy_2
    fairy "Sí, lo has hecho muy bien."
    fairy "Pero ahora y sabemos que sí hay criaturas en este bosque."
    fairy "Y se parecen bastante a lo que describía el Gran Sabio.{w} Así que debemos ir con gran cuidado."
    call playerTOfairy from _call_playerTOfairy_2
    girl "Sí, sí.{w} Tendremos mucho cuidado."
    girl "Pero creo que si sigues marcándome el camino no tendremos mucho problema."
    call playerFROMfairy from _call_playerFROMfairy_3
    fairy "Aún así, debemos ser precavidas, no sabemos que más hay en el bosque."
    window hide
    scene bg text forest 2 with dissolve
    nvl_narrator "{enf}La naira y la joven siguieron avanzando, encontrando a su paso cada vez más señales de vida.{/enf}"
    nvl_narrator "{enf}En algunas zonas del suelo crecía la hierba, algunos matojos ya no eran marrones y las ramas más bajas de los árboles comenzaban a tener hojas.{/enf}"
    nvl_narrator "{enf}Incluso más adelante, empezaban a vislumbrar plantas más grandes, incluso arbustos crecidos.{/enf}"
    nvl_narrator "{enf}A lo lejos, Sairina, de vez en cuando divisaba a lo lejos alguna que otra criatura, pero como no estaban realmente cerca de su camino, no quiso alarmar a la joven.{/enf}"
    nvl_narrator "{enf}Y así continuaron hasta que en su camino volvió a encontrarse una de aquellas grises y extrañas criaturas.{/enf}"
    scene bg forest dark with fade
    call playerTOfairy from _call_playerTOfairy_3
    girl "¿Otra más?"
    call playerFROMfairy from _call_playerFROMfairy_4
    fairy "Sí. Está ahí delante, ten cuidado."
    call playerTOfairy from _call_playerTOfairy_4
    girl "Si vuelves a marcarme el camino, no habrá problema."
    call playerFROMfairy from _call_playerFROMfairy_5
    fairy "Aún así, ya he visto más criaturas, es posible que ésta no esté sola."
    call playerTOfairy from _call_playerTOfairy_5
    girl "¿Y qué podemos hacer?"
    call playerFROMfairy from _call_playerFROMfairy_6
    fairy "Yo volveré a buscar el lugar más seguro y tú tendrás que venir hasta mí."
    fairy "Ahora que hay más vegetación, puedes usar los arbustos para esconderte."
    fairy "Seguro que eso despista a las criaturas."
    fairy "No olvides avanzar poco a poco y observar qué hacen las criaturas antes de volver a moverte."
    fairy "Y ya verás como antes de que te des cuenta volvemos a estar juntas."
    call playerTOfairy from _call_playerTOfairy_6
    girl "Vale, trataré de esconderme si hace falta."
    girl "Nos vemos al otro lado."
    stop music fadeout 3.0
    play music "music/Kara Evanescent Slow Base.mp3" fadein 3.0
    jump minigame_2