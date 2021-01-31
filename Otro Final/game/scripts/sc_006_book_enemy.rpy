label sc_006_book_enemy:
    call playerTOfairy
    fairy "Esto se está volviendo cada vez más peligroso."
    girl "Sí..."
    girl "¡Pero no podemos volver ahora!"
    girl "Estamos cada vez más cerca de algo, lo presiento."
    girl "Cada vez hay más zonas verdes, esto es muy extraño."
    fairy "Sí, es cierto."
    fairy "Y parece que todo esto nos está llevando en una dirección, así que es posible que si encontramos alguna respuesta..."
    call playerTOfairy
    girl "Ves, tú también tienes curiosidad."
    call playerFROMfairy
    fairy "Sí, la tengo."
    fairy "Pero debemos ser precavidas. Cuanto más nos adentramos, más lejos estamos de la salida."
    call playerTOfairy
    girl "Iremos con todo el cuidado del mundo."
    scene bg text forest 2 with dissolve
    call HIDE
    nvl_narrator "Sabiendo como avanzar de forma segura continuaron su aventura adentrándose aún más en el bosque"
    nvl_narrator "El bosque cada vez era más verde y podría asemejarse a un lugar normal..."
    nvl_narrator "Si no fuera porque las ramas de los árboles aún se entrelazaban entre si dejando que apenas pasara la luz"
    nvl_narrator "Y aquellas oscuras y extrañas criaturas deambulaban de un lado para otro como eternamente vigilantes"
    nvl_narrator "Pero no se les hizo esperar mucho"
    nvl_narrator "Tras unos cuantos árboles se abría el bosque formando un claro, y en él se hallaba un árbol verde que parecía emanar luz propia"
    nvl_narrator "Cuando se acercaron y pusieron verlo mejor descubrieron que se trataba de un objeto que había en árbol"
    nvl_narrator "Se acercaron como hechizadas y maravilladas por aquel árbol resplandeciente y aquel objeto que había en él"
    nvl_narrator "Quizá ese fuera el objeto mágico que perteneció a la gran maga..."
    scene bg FondoQueNoTengoJeJeJeJe with dissolve
    call playerTOfairy
    girl "Mira, parece un libro."
    call NOplayer_fairy
    "{i}GIRL se acercó asomada al tronco del árbol y estiró una mano para tocarlo, pero entonces se dio la vuelta hacia HADA{\i}"
    call playerTOfairy
    girl "¿Crees que podría cogerlo?"
    call playerFROMfairy
    fairy "Bueno, hemos llegado hasta aquí para eso, ¿no?"
    call NOplayer_fairy
    "{i}GIRL sonrió ampliamente y se giró hacia el libro e intento abrirlo. HADA se acercó a ella y miró también{\i}"
    "{i}Tras ver lo que contenía, se preguntó si GIRL se sentiría decepcionada, pero lejos de eso ella habló con una voz totalmente entusiasmada{\i}"
    call playerTOfairy
    girl "Es un libro... de historias."
    girl "Con ésto hacía magia."
    girl "Por eso sus palabras eran mágicas."
    girl "Se dedicaba a contar historias."
    call playerFROMfairy
    fairy "Me alegro de que te haya gustado tanto."
    fairy "Pensé que te decepcionaría que no estuviera lleno de palabras raras y símbolos."
    call playerTOfairy
    girl "¡No, es mucho mejor así!"
    girl "¿Crees que podríamos intentar...?"
    scene text grey with dissolve
    call HIDE
    nvl_narrator "Un poderoso y escalofriante rugido les sobresaltó"
    nvl_narrator "Rebotando entre los árboles de aquel taciturno bosque, parecía venir de todas partes"
    nvl_narrator "Se apresuraron a salir del claro e intentar alejarse"
    nvl_narrator "Pero entonces la figura de una criatura oscura de rojizos ojos se alzó ante ellas"
    nvl_narrator "Esta vez no podían simplemente evitarlo, pues era evidente que la criatura sabía de su presencia en el bosque"
    nvl_narrator "Tendrían que buscar otra manera..."
    scene bg bosqueMarchito with dissolve
    call playerTOfairy
    girl "¿Qué hacemos?"
    call playerFROMfairy
    fairy "Nuestra estrategia no tiene mucho sentido ahora que ya nos ha visto."
    call playerTOfairy
    girl "¿Y que hacemos? ¡¿Qué hacemos?!"
    call playerFROMfairy
    fairy "Tendremos que tratar de esquivarle..."
    call playerTOfairy
    girl "¿Y si usáramos el libro?"
    call playerFROMfairy
    fairy "¿Qué quieres decir?"
    call playerTOfairy
    girl "La maga usó este libro para calmar a las criaturas, quizá podríamos usarlo nosotras también."
    call playerFROMfairy
    fairy "¿Quieres intentar usar el libro?"
    call playerTOfairy
    girl "¿Y qué otra cosa podemos hacer?"
    call playerFROMfairy
    fairy "Está bien, está bien..."
    fairy "Tú intenta contarle la historia, pero no dejes de moverte."
    fairy "Iremos avanzando en dirección a la salida en dirección a la salida por si no funciona."
    fairy "Está bien, guíame, yo seguiré tu luz."
    call HIDE
    nvl_narrator "GIRL ayudada por la luz de HADA comenzó a leer la historia que contenía el libro en voz alta"
    nvl_narrator "El libro comenzó a brillar y la magia comenzó a cambiar el lugar como contaba la antigua historia"
    nvl_narrator "Mientras, HADA intentaba guiarlas por un lugar seguro para que ella pudiera continuar leyendo aquella mágica historia"
    jump minigame_3