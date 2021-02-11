label sc_009_panic_moment:
    stop music fadeout 3.0
    scene bg forest dark with fade
    play music "music/Oscuro Personajes.mp3" fadein 3.0
    call playerTOfairy
    girl "¡Sairina!{w} ¡Sairina!"
    call playerFROMfairy
    fairy "¿Qué ocurre?"
    fairy "¡Termina la historia de una vez!"
    fairy "¡Nos va a alcanzar!{w} ¡Deprisa!"
    call playerTOfairy
    girl "Pero..."
    girl "Es que...{w} ¡No puedo!"
    call playerFROMfairy
    fairy "¿Por qué?{w} Si ya no queda nada..."
    fairy "Si no terminamos no sabremos si esa es la forma de acabar con esto."
    call playerTOfairy
    girl "Pero es que la historia..."
    girl "¡No tiene final!"
    call playerFROMfairy
    fairy "¿¡Queeeeé!?"
    call playerTOfairy
    girl "No...{w} No está escrito."
    girl "¡Está en blanco!"
    call playerFROMfairy
    fairy "¡Oh, no!"
    fairy "Estamos perdidas..."
    fairy "Vamos a acabar como la maga..."
    call playerTOfairy
    girl "¡No!{w} No digas eso."
    girl "Tenemos que pensar en algo."
    girl "La historia no puede acabar así.{w} No hemos venido aquí para eso."
    call playerFROMfairy
    fairy "¡Ya viene!"
    scene bg forest monster
    call playerTOfairy
    girl "¿Qué hacemos?"
    call playerFROMfairy
    fairy "¡No lo sé!"
    fairy "Tendremos que inventarnos un final."
    call playerTOfairy
    girl "Umm..."
    girl "¡No se me ocurre nada!"
    call playerFROMfairy
    fairy "¡Cuidado!"
    stop music fadeout 3.0
    window hide
    play music "music/Peligro Narrador Slow.mp3" fadein 1.0
    scene text dark with fade
    nvl_narrator "{color=c8c8c8}{enf}La criatura las alcanzó.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Y con un rugido aterrador anunció que se acercaba el final.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}La criatura las atacó, pero Sairina consiguió con su luz cegarla momentáneamente.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Éstel sujetaba el libro con fuerza y miraba entre sus páginas como si buscara un milagro.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Pero no había nada.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Éstel, aturdida por la situación, se pregunta si habrían ido hasta allí sólo para repetir la misma historia.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Pero ahora no podía pensar en su error. Debía juntarse con Sairina y tratar de salir del bosque.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Pero la criatura pareció adivinar sus pensamientos, pues, de un salto, se acercó a Sairina y consiguió golpearla.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Éstel gritó asustada.\nSairina cayó al suelo tras chocar contra un árbol.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Éstel corrió hacía su amiga, olvidándose de la presencia de la criatura por un momento.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Por suerte, el ataque no había sido tan grave como parecía y Sairina se movía tratando de alzarse de nuevo.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Pero aquella terrible bestia no parecía dispuesta a dejar que eso sucediera.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Éstel se colocó entre ésta y Sairina tratando de proteger a la naira.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Miró de nuevo el libro, como si aún quisiera tener fe en aquella poderosa maga que pensó que su magia sería suficiente para calmar aquel lugar maldito.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Mientras contemplaba de nuevo las vacías páginas del libro, sintió a aquella criatura abalanzándose sobre ella.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Instintivamente usó el libro como escudo, abriéndolo de par en par para intentar cubrirse, aunque pudiera parecer la más ridícula de las ideas.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Éstel cerró los ojos con fuerza esperando el choque final.{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Sintió una inmensa fuerza que la empujó hacía atrás...{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Un último gruñido del oscuro ser...{/enf}{/color}"
    nvl_narrator "{color=c8c8c8}{enf}Y después...{/enf}{/color}"
    stop music fadeout 1.0
    nvl_narrator "{color=c8c8c8}{enf}{w=1}Silencio.{/enf}{/color}"
    scene bg forest clear with Fade(3.0, 0.5, 1.5)
    play music "music/Chrome en GP.mp3" fadein 3.0
    "¡Despierta, despierta!"
    "¿Estás bien?"
    show player right at cright
    girl "¿Qué... qué ha pasado?"
    call fairyTOplayer
    fairy "¡Lo has conseguido!"
    call fairyFROMplayer
    girl "¿Qué...?{w} Espera...{w} ¿Dónde está?"
    girl "Oh...{w} ¿Se ha ido?"
    girl "¿Y tú...{w} Cómo estás?{w} ¿Te ha hecho daño?"
    call fairyTOplayer
    fairy "Tranquila, estoy bien."
    fairy "Gracias a ti, las dos estamos bien."
    call fairyFROMplayer
    girl "Lo siento, pero..."
    girl "Al final cerré los ojos."
    girl "No sé lo que ha pasado."
    call fairyTOplayer
    fairy "El libro, lo usaste para cubrirte."
    call fairyFROMplayer
    girl "Ya..."
    call fairyTOplayer
    fairy "Míralo."
    call NOfairy_player
    "{i}Éstel, confusa, cogió el libro y comenzó a ojearlo.{/i}"
    call fairyFROMplayer
    girl "Está...{w} ¡Está aquí!{w} ¡En el libro!"
    call fairyTOplayer
    fairy "Sí, así es."
    call fairyFROMplayer
    girl "Entonces...{w} ¿El libro se lo ha tragado?"
    call fairyTOplayer
    fairy "Eso parece."
    fairy "Tenías razón."
    fairy "El libro era lo suficientemente poderoso, pero no sabíamos cómo usarlo."
    call fairyFROMplayer
    girl "La maga... la maga tenía razón, pero quizá no tuvo tiempo."
    girl "Así que, en realidad... Es gracias a ti."
    call fairyTOplayer
    fairy "¿Qué?{w} ¿Qué quieres decir?"
    call fairyFROMplayer
    girl "Que la diferencia entre aquella historia y la nuestra es que yo no estaba sola, porque tú estabas conmigo."
    call fairyTOplayer
    fairy "No, Éstel, en realidad eres tú la que ha venido conmigo..."
    fairy "Porque yo ya estuve aquí una vez."
    fairy "Hace muchos, muchos años."
    fairy "Pensé que podría hacerlo sola, pero no fue así."
    fairy "Ha tenido que pasar mucho tiempo, tanto, que ya ni siquiera lo recordaba."
    call fairyFROMplayer
    girl "Entonces...{w} Entonces...{w} ¡Tú eres la gran maga!"
    call fairyTOplayer
    fairy "Bueno, en realidad, ahora la gran maga eres tú."
    fairy "Yo me transforme en una naira."
    call NOfairy_player
    elder "¡Así que aquí estabais!"
    hide fairy with dissolve
    show player right at cright with dissolve
    show fairy right at ccright with dissolve
    show elder left at elderleft with dissolve
    pause
    call ELDER_fairy_player
    elder "Me teníais ya muy preocupado."
    elder "Pensé que se os habría ocurrido internaros en un bosque maldito y oscuro lleno de criaturas peligrosas,"
    elder "en busca de un objeto que podría no existir, para vencer a un mal invencible."
    elder "Pero ya veo que estáis bien."
    elder "Y este sitio está más bonito que nunca."
    call elder_fairy_PLAYER
    girl "¡Gran Sabio!"
    girl "Tenemos una historia increíble que contarte."
    call ELDER_fairy_player
    elder "Lo sé, pero creo que ya hemos tenido suficientes historias por hoy."
    elder "Ahora mejor volvamos a casa."
    hide player with dissolve
    hide fairy with dissolve
    hide elder with dissolve
    scene bg forest clear with fade
    show fairy right at cright
    fairy "Éstel."
    call playerTOfairy
    girl "¿Si, Sairina?"
    call playerFROMfairy
    fairy "Hay algo más."
    fairy "Quería darte las gracias por creer en mi historia."
    fairy "Por no conformarte."
    fairy "Y por venir a luchar contra la oscuridad como quise hacer yo en su día."
    call playerTOfairy
    girl "¡Gracias a ti por acompañarme!"
    girl "Todo empezó contigo.{w} Aunque fuera hace mucho tiempo."
    girl "Y ahora, hemos conseguido terminarlo.{w} ¡Juntas!"
    girl "Así sí que puede ser la historia."
    girl "Gracias a nuestro esfuerzo,{w} tú, yo, el bosque...{w} ¡Todos!"
    girl "Hemos conseguido {w}{b}otro final{b}."
    jump credits