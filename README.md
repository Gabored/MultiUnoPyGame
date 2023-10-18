# MultiUnoPyGame
Local Multiplayer Uno Python Game using PyGame
---

### Dev Sessions 


*Card Class*

Represents the Uno card object and has attributes as this type of cards. We are using "color", "number" and "action" to represent the different type of cards that they might be. 


*Player Class*

Represents the UNO Player that  will be playing on a game , at this point only has the attribute of "name" and "hand" which represents a list of Card instances that a player can play with. 


*Game Class*

Represents the UNO Game as a Whole a class that will contain the neccesary instances to perform a normal UNO game. This class consumes a player list that has attributes of hand, also it will in the future have an implemention of a card stack and the turns will be control within this class as well . 



Cómo funciona la función Play de la clase Game? 

La función play() en la clase Game es el núcleo de la implementación del juego UNO en Python. Esta función inicia el juego y ejecuta un ciclo principal que continúa mientras no se haya determinado un ganador. En cada iteración del ciclo, se muestra el número de turno y se obtiene el jugador actual mediante la función player_on_turn(). Luego, se verifica y muestra la carta en la cima de la pila de cartas con get_top_card().

La función card_input() se llama para gestionar la entrada del jugador. En esta función, se solicita al jugador que ingrese una carta o "DRAW" para tomar una carta del mazo. Si el jugador ingresa una carta válida, se verifica su validez y se actualiza la pila de cartas con check_valid_move() y se avanza al siguiente turno con next_turn().

Si el jugador elige "DRAW," se llama a draw_from_deck() para que el jugador saque cartas del mazo. La función check_win() se utiliza para determinar si un jugador ha ganado al quedarse sin cartas. El ciclo se repite hasta que se encuentre un ganador y se muestre un mensaje de felicitación. En resumen, la función play() orquesta la secuencia de turnos, validación de jugadas, y control del flujo del juego, lo que permite disfrutar de una partida completa de UNO en Python.

Cómo funciona la función check_valid_move? 

La función check_valid_move() en la clase Game desempeña un papel crítico en la lógica del juego UNO. Su objetivo principal es validar la jugada del jugador y decidir si se debe agregar una carta a la pila de cartas o si el jugador debe tomar una carta del mazo. Cuando se llama a esta función, se le pasa la entrada del jugador, que puede ser una carta específica o la palabra "DRAW" para indicar que el jugador desea tomar una carta del mazo.

La función comienza por verificar si el jugador desea "DRAW" una carta. Si es así, se llama a draw_from_deck() para que el jugador saque cartas del mazo y no se ejecuta ninguna otra acción en este turno.

Si el jugador ha ingresado una carta específica, se llama a player.find_card_in_hand(), que busca la carta en la mano del jugador y determina si es una jugada válida según las reglas de UNO. Si la carta es válida, se agrega a la pila de cartas con self.card_stack.append(card), y luego se elimina de la mano del jugador con player.remove_card(card).

En caso de que el jugador haya ingresado una carta inválida, se le informa de la invalidez de la jugada y se le vuelve a solicitar que ingrese una jugada válida. Este ciclo continúa hasta que el jugador realice una jugada válida o elija "DRAW."

En resumen, la función check_valid_move() controla si se agrega una carta a la pila de cartas o si el jugador toma una carta del mazo, y garantiza que todas las jugadas sean válidas según las reglas del juego UNO.

Estas funciones están dentro de ciclos while True ya que están codificadas para poder proporcionar al usuario de intentos ilimitados en caso de que haya escrito de manera incorrecta una carta o haya puesto un input no válido. 

Qué falta? 

    - Check Win no funciona adecuadamente
    - Las cartas de acción no hacen acciones 
    - Los turnos solo se pueden en un sentido 
    






