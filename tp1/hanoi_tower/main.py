import tracemalloc
import time
from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi
from search import (  # Importa las funciones de búsqueda del módulo search
    breadth_first_tree_search,
    breadth_first_graph_search,
    dfs_tree_search
)

def main(debug = False):
    """
    Función principal que resuelve el problema de la Torre de Hanoi y genera los JSON para el simulador.
    """
    # Define el estado inicial y el estado objetivo del problema
    initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
    goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

    # Crea una instancia del problema de la Torre de Hanoi
    problem_hanoi = ProblemHanoi(initial=initial_state, goal=goal_state)

    # Para medir tiempo consumido
    start_time = time.perf_counter()
    # Para medir memoria consumida (usamos el pico de memoria)
    tracemalloc.start()

    # Métodos no informados

    # Resuelve el problema utilizando búsqueda en anchura
    # Esta forma de búsqueda es muy ineficiente, por lo que si deseas probarlo, usa 3 discos o si querés esperar
    # un poco más, 4 discos, pero 5 discos no finaliza nunca.
    #last_node = breadth_first_tree_search(problem_hanoi)

    # Resuelve el problema utilizando búsqueda en anchura, pero con memoria que recuerda caminos ya recorridos.
    #last_node = breadth_first_graph_search(problem_hanoi, display=True)

    last_node = dfs_tree_search(problem_hanoi, display=debug)

    _, memory_peak = tracemalloc.get_traced_memory()
    memory_peak /= 1024*1024
    tracemalloc.stop()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if isinstance(last_node, NodeHanoi):
        # Imprime la longitud del camino de la solución encontrada
        if debug: print(f'Longitud del camino de la solución: {last_node.state.accumulated_cost}')

        # Genera los JSON para el simulador
        last_node.generate_solution_for_simulator()

    else:
        print(last_node)
        print("No se encuentra solución")

    # Imprime las métricas medidas
    if debug: print(f"Tiempo que demoró: {elapsed_time} [s]", )
    if debug: print(f"Maxima memoria ocupada: {round(memory_peak, 2)} [MB]", )
    return (elapsed_time, round(memory_peak, 2), last_node.state.accumulated_cost)


# Sección de ejecución del programa
if __name__ == "__main__":
    values = [ main(False) for i in range(10) ]
    cpu_time = [value[0] for value in values] 
    mem = [value[1] for value in values] 
    path_lengths = [value[2] for value in values] 
    print(values)
    print(f"Avg cpu time: {sum(cpu_time)/len(cpu_time)} s")
    print(f"Avg mem used: {sum(mem)/len(mem)} Mb")
    print(f"Avg path length: {sum(path_lengths)/len(path_lengths)} nodes")
    print(f"Theoretical optimal path length: {2**5 - 1} nodes")