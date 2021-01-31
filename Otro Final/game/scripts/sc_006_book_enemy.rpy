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
    call HIDE
    scene bg text forest 2 with fade
    nvl_narrator "{enf}Sabiendo como avanzar de forma segura continuaron su aventura adentrándose aún más en el bosque{/enf}"
    nvl_narrator "{enf}El bosque cada vez era más verde y podría asemejarse a un lugar normal...{/enf}"
    nvl_narrator "{enf}Si no fuera porque las ramas de los árboles aún se entrelazaban entre si dejando que apenas pasara la luz{/enf}"
    nvl_narrator "{enf}Y aquellas oscuras y extrañas criaturas deambulaban de un lado para otro como eternamente vigilantes{/enf}"
    nvl_narrator "{enf}Pero no se les hizo esperar mucho{/enf}"
    nvl_narrator "{enf}Tras unos cuantos árboles se abría el bosque formando un claro, y en él se hallaba un árbol verde que parecía emanar luz propia{/enf}"
    nvl_narrator "{enf}Cuando se acercaron y pusieron verlo mejor descubrieron que se trataba de un objeto que había en árbol{/enf}"
    nvl_narrator "{enf}Se acercaron como hechizadas y maravilladas por aquel árbol resplandeciente y aquel objeto que había en él{/enf}"
    nvl_narrator "{enf}Quizá ese fuera el objeto mágico que perteneció a la gran maga...{/enf}"
    scene bg  forest book with fade
    call playerTOfairy
    girl "Mira, parece un libro."
    call NOplayer_fairy
    "{i}Éstel se acercó asomada al tronco del árbol y estiró una mano para tocarlo, pero entonces se dio la vuelta hacia Sairina{\i}"
    call playerTOfairy
    girl "¿Crees que podría cogerlo?"
    call playerFROMfairy
    fairy "Bueno, hemos llegado hasta aquí para eso, ¿no?"
    call NOplayer_fairy
    "{i}Éstel sonrió ampliamente y se giró hacia el libro e intento abrirlo. Sairina se acercó a ella y miró también{\i}"
    "{i}Tras ver lo que contenía, se preguntó si Éstel se sentiría decepcionada, pero lejos de eso ella habló con una voz totalmente entusiasmada{\i}"
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
    call HIDE
    scene text grey with fade
    nvl_narrator "{enf}Un poderoso y escalofriante rugido les sobresaltó{/enf}"
    nvl_narrator "{enf}Rebotando entre los árboles de aquel taciturno bosque, parecía venir de todas partes{/enf}"
    nvl_narrator "{enf}Se apresuraron a salir del claro e intentar alejarse{/enf}"
    nvl_narrator "{enf}Pero entonces la figura de una criatura oscura de rojizos ojos se alzó ante ellas{/enf}"
    nvl_narrator "{enf}Esta vez no podían simplemente evitarlo, pues era evidente que la criatura sabía de su presencia en el bosque{/enf}"
    nvl_narrator "{enf}Tendrían que buscar otra manera...{/enf}"
    scene bg forest dark with fade
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
    scene text grey with fade
    nvl_narrator "{enf}Éstel ayudada por la luz de Sairina comenzó a leer la historia que contenía el libro en voz alta{/enf}"
    nvl_narrator "{enf}El libro comenzó a brillar y la magia comenzó a cambiar el lugar como contaba la antigua historia{/enf}"
    nvl_narrator "{enf}Mientras, Sairina intentaba guiarlas por un lugar seguro para que ella pudiera continuar leyendo aquella mágica historia{/enf}"
    jump minigame_3