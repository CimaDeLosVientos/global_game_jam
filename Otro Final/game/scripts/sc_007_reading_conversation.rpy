label sc_007_reading_conversation:
    stop music fadeout 3.0
    scene bg text magic 2 with fade
    play music "music/Oscuro Personajes.mp3" fadein 3.0
    nvl_narrator "{enf}Sairina y Éstel trataba de sortear a la oscura y peligrosa criatura que les perseguía.{/enf}"
    nvl_narrator "{enf}Mientras, el libro brillaba con más fuerza con cada palabra pronunciada.{/enf}"
    nvl_narrator "{enf}A su paso, crecía la hierba, se vestían las ramas de los árboles y la sombras parecía retirarse.{/enf}"
    scene text grey with dissolve
    nvl_narrator "{enf}Pero no parecía tener efecto sobre la terrible criatura.{/enf}"
    scene bg forest dark with fade
    call playerFROMfairy from _call_playerFROMfairy
    fairy "No está funcionando..."
    call playerTOfairy from _call_playerTOfairy
    girl "¡Funcionará!"
    call playerFROMfairy from _call_playerFROMfairy_1
    girl "Mira el bosque, sólo necesitamos más tiempo."
    fairy "Intentaré distraerle..."
    fairy "Intenta moverte entre los árboles para ganar distancia."
    stop music fadeout 3.0
    play music "music/Kara Evanescent Slow Base.mp3" fadein 3.0
    jump minigame_4