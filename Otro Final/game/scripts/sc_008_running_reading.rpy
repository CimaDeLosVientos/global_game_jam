label sc_008_running_reading:
    scene bg text forest 1 with fade
    nvl_narrator "{enf}Las dos intentaban con todas sus fuerzas mantenerse alejadas de la criatura{/enf}"
    nvl_narrator "{enf}Se esforzaban por mantenerse a salvo y continuar a salvo y continuar la historia{/enf}"
    nvl_narrator "{enf}Pero la criatura era implacable y apenas le sacaban suficiente ventaja como para pararse a descansar{/enf}"
    nvl_narrator "{enf}Ni siquiera tenían momento para contemplar lo que sucedía a su alrededor{/enf}"
    scene bg forest dark with fade
    call playerTOfairy
    girl "¿Qué hacemos Sairina? Cada vez está más cerca."
    girl "Casi diría que cada vez está más enfadado."
    girl "¿Por qué la magia no funciona con él?"
    call playerFROMfairy
    fairy "No lo sé"
    fairy "Quizá debas conseguir terminar la historia."
    call playerTOfairy
    girl "Estoy tan nerviosa que ni siquiera yo sé de que va la historia."
    call playerFROMfairy
    fairy "No te preocupes, tendrás tiempo para volver a leerlo en otro momento."
    fairy "Espero..."
    call playerTOfairy
    girl "Intenta ganar un poco más de tiempo."
    girl "Así yo podré esconderme y ganar distancia para poder terminar la historia."
    jump minigame_5