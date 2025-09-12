import pandas as pd


def estrella(maze, start, end):
    print("Algoritmo A*")
    

#cargar el laberinto
maze = pd.read_csv('./maze.csv', header=None) #para no mostrar la cabecera se usa header=None, para no mostrar los indices se usa index_col=False


#print(maze)
#para imprimir una posicion concreta
#print(maze.iloc[5,0]) #primera fila, primera columna

print(len(maze)) #longitud del array
print("Seleccione el agoritmo que desea usar: \n 1. BFS \n 2. DFS \n 3. A*")
opcion = int(input("Opcion: "))
if opcion == 1:
    print("Ha seleccionado BFS")
elif opcion == 2:
    print("Ha seleccionado DFS")
elif opcion == 3:
    print("Ha seleccionado A*")
    estrella(maze, (0,0), (len(maze)-1, len(maze)-1))
else:
    print("Opcion no valida")
    
    
    
    
    
    
    
