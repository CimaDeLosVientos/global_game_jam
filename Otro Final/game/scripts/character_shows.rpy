label elderTOplayer:
    show elder left at cleft
    show player right dark at cright
    return

label elderFROMplayer:
    show elder left dark at cleft
    show player right at cright
    return

label playerTOelder:
    show player left at cleft
    show elder right dark at cright
    return

label playerFROMelder:
    show player left dark at cleft
    show elder right at cright
    return

label fairyTOplayer:
    show fairy left at cleft
    show player right dark at cright
    return

label fairyFROMplayer:
    show fairy left dark at cleft
    show player right at cright
    return

label playerTOfairy:
    show player left at cleft
    show fairy right dark at cright
    return

label playerFROMfairy:
    show player left dark at cleft
    show fairy right at cright
    return

label NOelder_player:
    show elder left dark at cleft
    show player right dark at cright
    return

label NOplayer_fairy:
    show player left dark at cleft
    show fairy right dark at cright
    return

label NOfairy_player:
    show fairy left dark at cleft
    show player right dark at cright
    return

label ELDER_fairy_player:
    show player right dark at cright
    show fairy right dark at ccright
    show elder left at elderleft
    return

label elder_FAIRY_player:
    show player right dark at cright
    show fairy right at ccright
    show elder left dark at elderleft
    return

label elder_fairy_PLAYER:
    show player right at cright
    show fairy right dark at ccright
    show elder left dark at elderleft
    return



label HIDE:
    hide elder
    hide player
    hide fairy