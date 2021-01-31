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


label PLAYER_fairy_elder:
    show player left at cleft
    show fairy left dark at ccleft
    show elder right dark at cright
    return

label player_FAIRY_elder:
    show player left dark at cleft
    show fairy left at ccleft
    show elder right dark at cright
    return

label player_fairy_ELDER:
    show player left dark at cleft
    show fairy left dark at ccleft
    show elder right at cright
    return



label HIDE:
    hide elder
    hide player
    hide fairy