label dead_end:
    scene text dark with fade
    nvl_narrator "{enf}{color=c8c8c8}No...\n{w}Las historias no pueden acabar así...{/color}{/enf}"
    return

label basic_end:


label credits:
    stop music fadeout 5.0
    scene credits with Fade(3.0, 1.0, 2.0)
    pause #nvl_narrator "{enf}Gracias por jugar :){/enf}"
    scene main_menu with fade
    scene final_menu with dissolve
    return