label sc_005_before_book:
    scene bg forest dark with fade
    call playerTOfairy
    girl "Bien, lo he conseguido."
    call playerFROMfairy
    fairy "Sí, lo has hecho muy bien."
    fairy "Pero ahora y sabemos que sí hay criaturas en este bosque."
    fairy "Y se parecen bastante a lo que describía el Gran Sabio. Así que debemos ir gran cuidado."
    call playerTOfairy
    girl "Sí, sí. Tendremos mucho cuidado."
    girl "Pero creo que si sigues marcándome el camino no tendremos mucho problema."
    call playerFROMfairy
    fairy "Aún así, debemos ser precavidas, no sabemos que más hay en el bosque."
    window hide
    call NOplayer_fairy
    scene text forest with dissolve
    nvl_narrator "El SER y la joven siguieron avanzando encontrando a su paso cada vez más señales de vida"
    nvl_narrator "En algunas zonas del suelo crecía la hierba, algunos matojos ya no eran marrones y las ramas más bajas de los árboles comenzaban a tener hojas"
    nvl_narrator "Incluso más adelante, empezaba a haber ya plantas más grandes, incluos arbustos crecidos"
    nvl_narrator "A lo lejos, HADA de vez en cuando divisó alguna que otra criatura, pero como no estaban realmente cerca d esu camino, no quiso alarmar a la joven"
    nvl_narrator "Y así fue hasta que en su camino volvió a encontrarse una de aquellas grises y extrañas criaturas"
    call playerTOfairy
    girl "¿Otra más?"
    call playerFROMfairy
    fairy "Sí. Está ahí delante, ten cuidado."
    call playerTOfairy
    girl "Si vuelves a marcarme el camino, no habrá problema."
    call playerFROMfairy
    fairy "Aún así, he visto alguna que otra criatura, y es posible que ésta no esté sola."
    call playerTOfairy
    girl "¿Y qué podemos hacer?"
    call playerFROMfairy
    fairy "Yo volveré a buscar el lugar más seguro y tú tendrás que venir hasta mí."
    fairy "Ahora que hay más vegetación, puedes usar los arbustos para esconderte."
    fairy "Seguro que eso despista a las criaturas."
    fairy "No olvides avanzar poco a poco y observar que hacen las criaturas antes de vovler a moverte."
    fairy "Y ya verás como antes de que te des cuenta volvemos a estar juntas."
    call playerTOfairy
    girl "Vale, trataré de esconderme si hace falta."
    girl "Nos vemos al otro lado."

    jump minigame_2