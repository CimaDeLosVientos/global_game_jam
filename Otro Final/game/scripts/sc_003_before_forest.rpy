label sc_003_before_forest:
    window hide
    scene text normal with fade
    nvl_narrator "{enf}Las nairas son criaturas de fantasía\nde vibrantes y luminosos colores,\nsalidos de la más pura imaginación.{/enf}"
    nvl_narrator "{enf}Se dice que estos seres se componen de la imaginación, los pensamientos y los sentimientos que quedan suspendidos en el aire allá por donde otra criatura haya pasado.{/enf}"
    nvl_narrator "{enf}Por eso, dicen, se sienten atraídas por personas imaginativas, sabias y aventureras a las que no dudan en acompañar y ayudar en lo que puedan.{/enf}"
    nvl_narrator "{enf}También se dice que, a parte de los cientos de recuerdos, pensamientos e historias de las que se componen, guardan la esencia de los Ancestros.{/enf}"
    nvl_narrator "{enf}Es decir, de todos aquellos que ya no están, pero que dejaron una huella imborrable.{/enf}"
    nvl_narrator "{enf}Es por eso que muchos adivinan,\nentre las lenguas llameantes de la magia que les rodea, la forma de un corazón.{/enf}"
    nvl_narrator "{enf}Como un símbolo de la vida que late dentro de ellas.{/enf}"
    nvl_narrator "{enf}Sean ciertas o no estás creencias, sigue siendo verdad que una naira siempre tratará de traer algo de luz a la oscuridad de la manera que le sea posible.{/enf}"

    scene bg forest clear with fade
    show player left at cright
    girl "Pues... Aquí es."
    girl "No sé si este bosque será todas las palabras que dijo el Gran Sabio, pero..."
    girl "No parece un sitio muy animado."
    girl "Eso tiene un punto muy positivo y es que, si no hay nadie, nadie puede hacerte daño."
    "Espera, espera."
    show player right at cright
    girl "¿Eh? ¿Qué?"
    girl "¡Pero si no había nadie!"
    girl "Si antes lo digo..."
    show player right dark at cright with dissolve
    show fairy left at cleft with dissolve
    fairy "Tranquila, soy yo."
    call fairyFROMplayer from _call_fairyFROMplayer
    girl "Oh, Sairina, eres tú."
    girl "Había venido a ver cómo era el bosque de cerca, después de la historia que nos ha contado el Gran Sabio."
    call fairyTOplayer from _call_fairyTOplayer
    fairy "Tengo la corazonada de que ibas a algo más que a mirar desde la linde del bosque."
    call fairyFROMplayer from _call_fairyFROMplayer_1
    girl "Vaya, eres muy lista..."
    call fairyTOplayer from _call_fairyTOplayer_1
    fairy "Después de la historia que nos han contado... ¿Crees que lo más prudente es entrar ahí dentro?"
    call fairyFROMplayer from _call_fairyFROMplayer_2
    girl "Bueno... Pero no parece que haya nada peligroso."
    girl "Está bastante oscuro, pero parece más un sitio aburrido que agresivo."
    call fairyTOplayer from _call_fairyTOplayer_2
    fairy "Eso puede ser al principio, pero no sabemos qué habrá más allá."
    call fairyFROMplayer from _call_fairyFROMplayer_3
    girl "Pues...{w} Pues..."
    girl "Más allá..."
    girl "Podría..."
    call fairyTOplayer from _call_fairyTOplayer_3
    fairy "Podría haber algo interesante, ¿no?"
    call fairyFROMplayer from _call_fairyFROMplayer_4
    girl "¡Claro!{w} El objeto de la gran maga."
    girl "El que se quedó en el bosque cuando ella..."
    girl "Bueno...{w} Cuando ella..."
    call fairyTOplayer from _call_fairyTOplayer_4
    fairy "Desapareció."
    call fairyFROMplayer from _call_fairyFROMplayer_5
    girl "¡Sí, eso!{w} Cuando ella desapareció."
    girl "El objeto se quedó allí, en el bosque, según la historia del Gran Sabio..."
    call fairyTOplayer from _call_fairyTOplayer_5
    fairy "Ni siquiera sabemos si esa historia es verdad."
    call fairyFROMplayer from _call_fairyFROMplayer_6
    girl "Pero, si no lo fuera, eso significaría que el final de la historia es el que ha contado el Gran Sabio."
    girl "¡Y eso no puede ser!"
    girl "El objeto tiene que estar ahí dentro."
    girl "..."
    girl "Sólo hay que..."
    call fairyTOplayer from _call_fairyTOplayer_6
    fairy "Está bien, está bien."
    fairy "Te acompañaré."
    fairy "Pero, si el lugar es tan peligroso como cuenta la historia, tendremos que retroceder para no sufrir el mismo destino que la gran maga."
    call fairyFROMplayer from _call_fairyFROMplayer_7
    girl "Sí, sí.{w} Está bien."
    girl "¡Gracias, Sairina!"

    jump sc_004_within_forest