label sc_009_panic_moment:
    scene text forest 3 with fade
    call girlTOfairy
    girl "¡HADA! ¡HADA!"
    call girlFROMfairy
    fairy "¿Qué ocurre?"
    fairy "¡Termina la historia de una vez!"
    fairy "Nos va a alcanzar. ¡Deprisa!"
    call girlTOfairy
    girl "Pero..."
    girl "Es que... ¡No puedo!"
    call girlFROMfairy
    fairy "¿Por qué? Si ya no queda nada."
    fairy "Si no terminamos no sabremos si esa es la forma de acabar con esto."
    call girlTOfairy
    girl "Pero es que la historia..."
    girl "¡No tiene final!"
    call girlFROMfairy
    fairy "¿¡Queeeeé!?"
    call girlTOfairy
    girl "No, no está escrito."
    girl "¡Está en blanco!"
    call girlFROMfairy
    fairy "¡Oh, no!"
    fairy "Estamos perdidas."
    fairy "Vamos a acabar como la maga."
    call girlTOfairy
    girl "No, no digas eso."
    girl "Tenemos que pensar en algo."
    girl "La historia no puede acabar así. No hemos venido aquí para eso."
    call girlFROMfairy
    fairy "¡Ya viene!"
    call girlTOfairy
    girl "¿Qué hacemos?"
    call girlFROMfairy
    fairy "¿¡No lo sé!?"
    fairy "Tendremos que inventarnos un final."
    call girlTOfairy
    girl "Mmmmm..."
    girl "¡No se me ocurre nada!"
    call girlFROMfairy
    fairy "¡Cuidado!"
    window hide
    scene text normal with fade
    nvl_narrator "La criatura les alcanzó"
    nvl_narrator "Y con un rugido aterrador anunció que se acercaba el final"
    nvl_narrator "La criatura les atacó, pero HADA consiguió con su luz cegar momentáneamente a la criatura"
    nvl_narrator "GIRL sujetaba el libro con fuerza y miraba entre sus páginas como si buscara un milagro"
    nvl_narrator "Pero no había nada"
    nvl_narrator "GIRL, aturdida por la situación, se pregunta si habrían ido hasta allí sólo para repetir la misma historia"
    nvl_narrator "Pero ahora no podía pensar en su error. Debía juntarse con HADA y tratar de salir del bosque"
    nvl_narrator "Pero la criatura pareció adivinar sus pensamientos, pues de un salto se acercó a HADA consiguió golpearla"
    nvl_narrator "HADA cayó al suelo y GIRL gritó"
    nvl_narrator "GIRL corrió hacía su amiga olvidándose de la presencia de la criatura por un momento"
    nvl_narrator "Por suerte, el ataque no había sido tan grave como podía haber sido y HADA intentaba incorporarse"
    nvl_narrator "Pero aquella terrible bestia no parecía dispuesta a dejar que eso sucediera"
    nvl_narrator "GIRL se colocó entre ésta y HADA"
    nvl_narrator "Miró de nuevo el libro como si aún quisiera tener fe en aquella poderosa maga que pensó que su magia sería suficiente para calmar aquel lugar maldito"
    nvl_narrator "Mientras contemplaba de nuevo las vacías páginas del libro, sintió a aquella criatura abalanzándose sobre ella"
    nvl_narrator "Instintivamente usó el libro abierto como escudo, aunque pudiera parecer la más ridícula de las ideas"
    nvl_narrator "GIRL cerró los ojos con fuerza esperando el choque final"
    nvl_narrator "Sintió una inmensa fuerza que la empujó hacía atrás, un último gruñido del oscuro ser y después silencio"
    scene text forest 3 with fade
    fairy "¡Despierta, despierta!"
    fairy "¿Estás bien?"
    call girlTOfairy
    girl "¿Qué... qué ha pasado?"
    call girlFROMfairy
    fairy "¡Lo has conseguido!"
    call girlTOfairy
    girl "¿Qué?"
    girl "Espera, ¿dónde está?"
    girl "Oh, ¿se ha ido?"
    girl "¿Y tú, cómo estás? ¿Te ha hecho daño?"
    call girlFROMfairy
    fairy "Tranquila, estoy bien"
    fairy "Gracias a ti, las dos estamos bien."
    call girlTOfairy
    girl "Lo siento, pero..."
    girl "Al final cerré los ojos."
    girl "No sé lo que ha pasado."
    call girlFROMfairy
    fairy "El libro, lo usaste para defenderte."
    call girlTOfairy
    girl "Ya..."
    call girlFROMfairy
    fairy "Míralo."
    call NOgirl_fairy
    "{i}GIRL cogió el libro confusa y comenzó a ojearlo{/i}"
    call girlTOfairy
    girl "Está... ¡Está aquí! ¡En el libro!"
    call girlFROMfairy
    fairy "Sí, así es."
    call girlTOfairy
    girl "Entonces... ¿el libro se lo ha tragado?"
    call girlFROMfairy
    fairy "Eso parece."
    fairy "Tenías razón."
    fairy "El libro era lo suficientemente poderoso, pero no sabíamos como usarlo."
    call girlTOfairy
    girl "La maga... la maga tenía razón, pero quizá no tuvo tiempo."
    girl "Así que en realidad... es gracias a ti."
    call girlFROMfairy
    fairy "¿Qué?"
    fairy "¿Qué quieres decir?"
    call girlTOfairy
    girl "Que la diferencia entre esta vez y aquella es que yo no estoy sola, porque tú has venido conmigo."
    call girlFROMfairy
    fairy "No, GIRL, en realidad eres tú la que ha venido conmigo porque yo ya estuve aquí una vez."
    fairy "Hace muchos, muchos años."
    fairy "Pensé que podría hacerlo sola, pero no fue así."
    fairy "Ha tenido que pasar mucho tiempo, tanto, que ya ni siquiera lo recordaba."
    call girlTOfairy
    girl "Entonces... tú eres la gran maga."
    call girlFROMfairy
    fairy "Bueno, en realidad ahora la gran maga eres tú. Yo soy sólo un SER."
    # TRANSICION AL VIEJO
    elder "¡Así que aquí estabais!"
    hide fairy with dissolve
    show player left at ccleft with dissolve
    show fairy left at ccleft with dissolve
    show elder right at cright with dissolve
    pause
    call player_fairy_ELDER
    elder "Me teníais ya muy preocupado."
    elder "Pensé que se os habría ocurrido internaros en un bosque maldito y oscuro lleno de criaturas peligrosas"
    elder "en busca de un objeto que podría no existir, para vencer a un mal invencible."
    elder "Pero ya veo que estáis bien."
    elder "Y este sitio está más bonito que nunca."
    call PLAYER_fairy_elder
    girl "¡Gran Sabio!"
    girl "Tenemos una historia increíble que contarte."
    call player_fairy_ELDER
    elder "Lo sé. Pero creo que ya hemos tenido suficientes historias por hoy."
    elder "De momento."
    elder "Volvamos a casa."
    hide player left at ccleft with dissolve
    hide fairy left at ccleft with dissolve
    hide elder right at cright with dissolve
    scene text forest 3 with fade
    call girlFROMfairy
    fairy "GIRL"
    call girlTOfairy
    girl "¿Si, HADA?"
    call girlFROMfairy
    fairy "Hay algo más."
    fairy "Quería darte las gracias por creer en mi historia."
    fairy "Por no conformarte."
    fairy "Y por venir a luchar contra la oscuridad como quise hacer yo en su día."
    call girlTOfairy
    girl "¡Gracias a ti por acompañarme!"
    girl "Todo empezó contigo. Aunque fuera hace mucho tiempo."
    girl "Y ahora, hemos conseguido resolverlo."
    girl "¡Juntas!"
    girl "Así sí que puede ser la historia."
    girl "Gracias a nuestro esfuerzo, tú, yo, el bosque... ¡todos!"
    girl "Hemos conseguido que haya otro final."
    jump credits
    #jump basic_end