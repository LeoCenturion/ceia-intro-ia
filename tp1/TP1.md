1. ¿Cuáles son los PEAS de este problema? (Performance, Environment, Actuators, Sensors)
Performance: una función que da 1 si se llego al estado final y 0 si no.
Environment: las 3 varillas y los n discos.
Actuators: lo que sea que mueva los n discos.
Sensors: lo que sea que detecte los discos, en que varilla están y en que posición horizontal se encuentran.
2. ¿Cuáles son las propiedades del entorno de trabajo?
Totalmente  vs parcialmente observable: totalmente observable. Todos las varillas, discos, y sus posiciones en cada varilla son observables.
Determinista vs Estocástico: determinista, no hay elementos aleatorios en el problema.
Episódico vs secuencial: episódico. Si bien las acciones pasadas generaron la configuración actual, la posibilidad de alcanzar el objetivo no se ve comprometida por ellas. Siempre es posible llegar a la solución si se parte de una configuración valida.
Estática vs dinámica: estática. Solo el agente cambia el entorno.
Discreta vs continua. Discreta.
Agente individual vs Multiagente: agente individual.
3. En el contexto de este problema, establezca cuáles son los: estado, espacio de estados, árbol de búsqueda, nodo de búsqueda, objetivo, acción y frontera.

Estado: representando un estado como una 3-upla de listas de enteros del 1 al 5 (l1, l2, l3) donde cada li representa el estado de la varilla i siendo el primer elemento de li el disco del fondo de la varilla y el siguiente el disco que se encuentra por encima. Dado lo anterior el espacio de estados se conforma por todos los (l1, l2, l3) con li ordenado de forma descendiente, sin elementos repetidos, y con elementos del rango [1,5].

Espacio de estados: todas las 3-uplas que cumplan con lo de arriba.

Estado inicial: ([5,4,3,2,1], [], []).
Objetivo: ([],[],[5,4,3,2,1]).
Acción: quitar el ultimo elemento de una de las listas y agregarlo al final de otra lista si eso resulta en que la lista elegida sigue estando ordenada de forma descendiente.
Arbol de busqueda: ??
nodo de busqueda: ??
frontera: ??

4. Implemente algún método de búsqueda. Puedes elegir cualquiera menos búsqueda en anchura primero (el desarrollado en clase). Sos libre de elegir cualquiera de los vistos en clases, o inclusive buscar nuevos.
dfs




