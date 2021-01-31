label sc_007_reading_conversation:
    scene text normal with fade
    nvl_narrator "{enf}Sairina y Éstel trataba de sortear a la oscura y peligrosa criatura que les perseguía{/enf}"
    nvl_narrator "{enf}Mientras el libro brillaba con más fuerza con'cada palabra pronunciada{/enf}"
    nvl_narrator "{enf}A su paso, crecía la hierba, se vestian las ramas de los árboles y la sombras parecía retirarse{/enf}"
    nvl_narrator "{enf}Pero no parecía tener efecto sobre la terrible criatura{/enf}"
    scene bg forest dark with fade
    call playerFROMfairy from _call_playerFROMfairy
    fairy "No está funcionando..."
    call playerTOfairy from _call_playerTOfairy
    girl "¡Funcionará!"
    call playerFROMfairy from _call_playerFROMfairy_1
    fairy "Mira el bosque, sólo necesitamos más tiempo."
    fairy "Intentaré distraerle"
    fairy "Intenta moverte entre los árboles para ganar distancia."
    jump minigame_4