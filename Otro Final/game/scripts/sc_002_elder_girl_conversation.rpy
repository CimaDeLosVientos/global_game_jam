label sc_002_elder_girl_conversation:
    scene bg forest clear with dissolve
    call elderTOplayer from _call_elderTOplayer
    elder "Eh…"
    elder "Sí, sí. Es así. Lo recuerdo perfectamente."
    elder "Esa es la historia del Bosque Marchito."
    elder "El bosque que comienza tras aquella colina y que merma con su aspecto nuestros coloridos y hermosos paisajes..."
    call elderFROMplayer from _call_elderFROMplayer
    girl "Pero, Gran Sabio, eso es muy triste."
    girl "Así no acaban las historias."
    girl "No puede ser…"
    call elderTOplayer from _call_elderTOplayer_1
    elder "Querida, existen muchas historias."
    elder "No todas pueden acabar bien o tener el final que desearíamos."
    elder "Sobre todo si no depende de nuestra imaginación."
    elder "Si no que forma parte de nuestra historia."
    call elderFROMplayer from _call_elderFROMplayer_1
    girl "Pero…"
    girl "Gran Sabio... "
    girl "Los finales no son así…"
    window hide
    scene text normal with dissolve
    nvl_narrator "{enf}Éstel tenía una mente despierta y una gran curiosidad por todo lo que le rodeaba{/enf}"
    nvl_narrator "{enf}Le encantaba explorar y también dibujar, siempre iba con su libreta de notas a todas partes{/enf}"
    nvl_narrator "{enf}También era entusiasta, imaginativa y optimista{/enf}"
    nvl_narrator "{enf}Le encantaban las historias del Gran Sabio, por el que sentía una gran admiración y fascinación{/enf}"
    nvl_narrator "{enf}Aunque no siempre estuviera de acuerdo con sus historias…{/enf}"
    scene bg forest clear with dissolve
    call elderTOplayer from _call_elderTOplayer_2
    elder "Umm…"
    call NOelder_player from _call_NOelder_player
    "{i}El sabio acariciaba sus largas barbas, pensativo, mientras la joven con ojos brillantes y entusiastas esperaba ansiosa alguna sabia respuesta por su parte.{/i}"
    call elderTOplayer from _call_elderTOplayer_3
    elder "Bueno… Sólo hay una forma de que ese no sea el final."
    call elderFROMplayer from _call_elderFROMplayer_2
    girl "¿Y cuál es, Gran Sabio?"
    call NOelder_player from _call_NOelder_player_1
    "{i}La chica se adelantó con impaciencia y el sabio sonrió.{/i}"
    call elderTOplayer from _call_elderTOplayer_4
    elder "Que la historia aún no haya terminado."
    call NOelder_player from _call_NOelder_player_2
    "{i}El sabio se levantó y comenzó a andar con tranquilidad, mientras la joven le seguía impaciente.{/i}"
    call elderTOplayer from _call_elderTOplayer_5
    elder "La leyenda también cuenta que la maga tenía un objeto mágico."
    elder "Un objeto con el cual podría llevar a cabo su magia."
    elder "Un objeto tan poderoso que era capaz de liberar a las criaturas de tan terrible maldición… O casi."
    elder "Y cuando ella cayó, aquel objeto quedó en el bosque como único recuerdo de su paso por allí."
    call NOelder_player from _call_NOelder_player_3
    "{i}El sabio dejó de caminar y se volvió hacia ella para mirarla. sus ojos se movían inquietos como si ahora cientos de pensamientos se arremolinaran en su cabeza.{/i}"
    call elderTOplayer from _call_elderTOplayer_6
    elder "Así que supongo que podríamos decir que esa historia aún no ha acabado."
    elder "¿Estás más contenta ahora?"
    call elderFROMplayer from _call_elderFROMplayer_3
    girl "¡Muchísimo, Gran Sabio!"
    hide player with dissolve
    show elder left dark at cleft with dissolve
    "{i}La chica se despidió de él rápida y efusivamente, dándole las gracias por su historia, y se marchó, casi a saltos más que a pasos, con entusiasmo renovado.{/i}"
    show elder left dark at cright with dissolve
    "{i}El quedó un rato pensativo, mirando hacia el lugar por que el que ella se había marchado y, tras un tiempo de meditación en silencio, dijo:.{/i}"
    show elder right at cright
    elder "¡Sairina!"
    show fairy left at cleft with dissolve
    elder "Por favor, se mi voz y mis ojos acompañando a esa joven."
    elder "Temo que esta historia haya calado hasta hacerse algo personal."
    elder "Que la sabiduría de los Naira la acompañen allá donde la lleven sus aventuras."

    jump sc_003_before_forest
