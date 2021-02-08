label sc_008_running_reading:
    stop music fadeout 3.0 
    scene bg text magic 3 with fade
    play music "music/Oscuro Personajes.mp3" fadein 3.0
    nvl_narrator "{enf}Las dos intentaban con todas sus fuerzas mantenerse alejadas de la criatura.{/enf}"
    nvl_narrator "{enf}Se esforzaban por mantenerse a salvo y así poder continuar la historia.{/enf}"
    nvl_narrator "{enf}Pero la criatura era implacable y apenas le sacaban suficiente ventaja como para pararse a descansar.{/enf}"
    nvl_narrator "{enf}Ni siquiera tenían momento para contemplar lo que sucedía a su alrededor.{/enf}"
    nvl_narrator "{enf}Como que el suelo sobre el que pisaban cada vez era más blando debido a la hierba que crecía...{/enf}"
    nvl_narrator "{enf}O que eran las hojas de las ramas bajas de los árboles las que ahora les ayudaban a esconderse del monstruo{/enf}"
    scene bg forest dark with fade
    call playerTOfairy from _call_playerTOfairy_19
    girl "¿Qué hacemos Sairina? Cada vez está más cerca."
    girl "Y casi diría que cada vez está más enfadado."
    girl "¿Por qué la magia no funciona con él?"
    call playerFROMfairy from _call_playerFROMfairy_17
    fairy "No lo sé..."
    fairy "Quizá debas conseguir terminar la historia."
    call playerTOfairy from _call_playerTOfairy_20
    girl "Estoy tan nerviosa que ni siquiera yo sé de qué va la historia."
    call playerFROMfairy from _call_playerFROMfairy_18
    fairy "No te preocupes, tendrás tiempo para volver a leerla en otro momento."
    fairy "Espero..."
    call playerTOfairy from _call_playerTOfairy_21
    girl "Intenta ganar un poco más de tiempo."
    girl "Así yo podré esconderme, e intentar sacarle algo de distancia para poder terminar la historia."
    stop music fadeout 3.0
    play music "music/Kara Evanescent Slow Base.mp3" fadein 3.0
    jump minigame_5