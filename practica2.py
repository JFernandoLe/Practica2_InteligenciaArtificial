import pandas as pd
import numpy as np


def estrella(maze, inicio, fin):
    print("Algoritmo A*")
    abiertos=[]
    cerrados=[]
    ruta={}
    #nodo: (Coordenada,g,h,f,parent)
    g_inicio=0;
    h_inicio=heuristica(inicio, fin)
    f_inicio=g_inicio+h_inicio
    nodo=(inicio,g_inicio,h_inicio,f_inicio,[])
    abiertos.append(nodo)
    
    print(f"Lista de abiertos: {abiertos}")
    print(f"Lista de cerrados: {cerrados}")
    while len(abiertos)!=0: 
        #Ordenamos la lista de abiertos por mejor f
        abiertos.sort(key=lambda s: (s[3],s[2],s[1],s[0][1],s[0][0]))
        nodo=abiertos[0]
        print(f"Nodo actual {nodo}")
        if(nodo[0]==fin):
            cerrados.append(nodo)
            print("Solucion: ")
            print(formarCamino(ruta,fin))
            imprimirSolucion(formarCamino(ruta,fin),maze)
            exit()
        abiertos.remove(nodo)
        cerrados.append(nodo)
        print(f"Lista de abiertos: {abiertos}")
        print(f"Lista de cerrados: {cerrados}")
        #Expansion de vecinos
        vecinos=[];
        #Obtenemos las coordenadas de los nodos vecinos y las insertamos en vecinos (arriba,derecha,abajo,izquierda)
        vecinos.extend([[nodo[0][0]-1,nodo[0][1]],[nodo[0][0],nodo[0][1]+1],[nodo[0][0]+1,nodo[0][1]],[nodo[0][0],nodo[0][1]-1]])
        for v in vecinos:
            #Si v es pared o esta en cerrados, continuar
            salir=False;
            print(f"Vecino a evaluar: {v}")
            if (v[0] or v[1])>=0:
                if 0 <= v[0] < maze.shape[0] and 0 <= v[1] < maze.shape[1]:
                    print(maze.iloc[v[0],v[1]] )
                    if str(maze.iloc[v[0], v[1]]) == '1':
                        print("Es pared")
                        continue
                    else:
                        for c in cerrados:
                            if c[0] == v:
                                print("Esta en cerrados")
                                salir=True;
                                break
                        if salir:
                            continue
                else:
                    print("Fuera de rango")
                    continue
            else:
                print("Fuera del limite")
                continue
            
            print("Codigo")
            tentativo_g=nodo[1]+1
            
            #Verificamos si el vecino esta en abiertos
            if len(abiertos)==0:
                print("Esta vacio abiertos")
                print("Agregamos vecino a abiertos")
                abiertos.append((v,tentativo_g,heuristica(v,fin),tentativo_g+heuristica(v,fin),nodo[0]))
                ruta[tuple(v)]=tuple(nodo[0])
                print(abiertos)
            else:
                for a in abiertos:
                    if a[0]==v:
                        print("Esta en abiertos")
                        if tentativo_g>=a[1]:
                            print("No agregar")
                            break
                        else:
                            print("Agregamos vecino a abiertos")
                            abiertos.append((v,tentativo_g,heuristica(v,fin),tentativo_g+heuristica(v,fin),nodo[0]))
                            ruta[tuple(v)]=tuple(nodo[0])
                            print(abiertos)
                            break
                    else:
                        print("No esta en abiertos")
                        print("Agregamos vecino a abiertos")
                        abiertos.append((v,tentativo_g,heuristica(v,fin),tentativo_g+heuristica(v,fin),nodo[0]))
                        ruta[tuple(v)]=tuple(nodo[0])
                        print(abiertos)
                        break
    print("No hay ruta")
    
        
def formarCamino(ruta,fin):
    camino=[]
    actual=tuple(fin)
    while actual in ruta:
        camino.append(actual)
        actual=ruta[actual]
    camino.append(actual)
    camino.reverse()
    return camino
    
def heuristica(a, b):   
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def imprimirSolucion(camino, maze):
    
    solucion = maze.copy().astype(object)
    for fila, columna in camino:
        solucion.iloc[fila, columna] = '*'
    solucion.to_csv("solucion.csv", index=False)

    print("Solución marcada y guardada en solucion.csv")
    print(solucion)


#cargar el laberinto
maze = pd.read_csv('./maze2.csv', header=None)
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
print("Seleccione el agoritmo que desea usar: \n 1. BFS \n 2. DFS \n 3. A*\n")
opcion = input()
opcion=(int(opcion))
if opcion == 1:
    print("Ha seleccionado BFS")
elif opcion == 2:
    print("Ha seleccionado DFS")
elif opcion == 3:
    print("Ha seleccionado A*")
    estrella(maze, inicio, fin)
else:
    print("Opcion no valida")
    

