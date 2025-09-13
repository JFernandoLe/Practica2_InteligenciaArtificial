import pandas as pd
import numpy as np


def estrella(maze, inicio, fin):
    print("Algoritmo A*")
    abiertos=[]
    cerrados=[]
    #nodo: (Coordenada,g,h,f,parent)
    g_inicio=0;
    h_inicio=heuristica(inicio, fin)
    f_inicio=g_inicio+h_inicio
    nodo=(inicio,g_inicio,h_inicio,f_inicio,[])
    abiertos.append(nodo)
    abiertos.append(([0,2],50,50,100,[]))
    print(abiertos)
    #Insertamos en abiertos el mejor nodo
    nodo=min(abiertos,key=lambda s: s[3])
    print(nodo)
            
        
        
    
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#cargar el laberinto
maze = pd.read_csv('./maze.csv', header=None)
print(maze)
#Obtener las coordenadas del inicio
indices_s = np.where(maze == 'S') 
inicio=[int(i) for i in [indices_s[0][0], indices_s[1][0]]]
#Obtener las coordenadas del fin
indices_e = np.where(maze == 'E')   
fin=[int(i) for i in [indices_e[0][0], indices_e[1][0]]]


print("Inicio: ", inicio)
print("Fin: ", fin)

#Menu para seleccionar el algoritmo
print("Seleccione el agoritmo que desea usar: \n 1. BFS \n 2. DFS \n 3. A*")
opcion = int(input("Opcion: "))
if opcion == 1:
    print("Ha seleccionado BFS")
elif opcion == 2:
    print("Ha seleccionado DFS")
elif opcion == 3:
    print("Ha seleccionado A*")
    estrella(maze, inicio, fin)
else:
    print("Opcion no valida")
    
    
    
    
    
    
    
