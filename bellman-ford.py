class Grafo:
    def __init__(self):
        self.nodos = {}
 
    def add_nodo(self, nro_nodo):
        nodo = Nodo(nro_nodo)
        self.nodos[nro_nodo] = nodo
 
    def get_nodo(self, nro_nodo):
        return self.nodos[nro_nodo]
 
    def add_arista(self, src_nro_nodo, dest_nro_nodo, peso=1):
        self.nodos[src_nro_nodo].add_nodo_adyacente(self.nodos[dest_nro_nodo], peso)
 
    def __len__(self):
        return len(self.nodos)
 
    def __iter__(self):
        return iter(self.nodos.values())
        
    def arista_existe(self, src_nro_nodo, dest_nro_nodo):
        return self.nodos[src_nro_nodo].es_adyacente(self.nodos[dest_nro_nodo])
 
 
 
class Nodo:
    def __init__(self, nro_nodo):
        self.nro_nodo = nro_nodo
        self.nodos_adyacentes = {}
 
    def get_key(self):
        return self.nro_nodo
 
    def add_nodo_adyacente(self, dest_nro_nodo, peso):
        self.nodos_adyacentes[dest_nro_nodo] = peso
 
    def get_nodos_adyacentes(self):
        return self.nodos_adyacentes.keys()
 
    def get_peso(self, dest_nro_nodo):
        return self.nodos_adyacentes[dest_nro_nodo]
    
    def es_adyacente(self, dest):
        return dest in self.nodos_adyacentes
 
def bellman_ford(grafo, nodo_origen):
    distancia = dict.fromkeys(grafo, float('inf'))
    distancia[nodo_origen] = 0

    for _ in range(len(grafo) - 1):
        for nodo in grafo:
            for nodo_adyacente in nodo.get_nodos_adyacentes():
                distancia[nodo_adyacente] = min(distancia[nodo_adyacente], distancia[nodo] + nodo.get_peso(nodo_adyacente))
                
    return distancia
    
    
def crearGrafo():
    g = Grafo()
    while True:
        usuario_input = input('Desea Agregar nodo/Agregar arista/Bellaman-Ford/Mostrar/Salir: ').split()
     
        operation = usuario_input[0].lower()
        if operation == "agregar":
            suboperation = usuario_input[1]
            if suboperation == 'nodo':
                key = int(usuario_input[2])
                if key not in g:
                    g.add_nodo(key)
                else:
                    print('El vertice ya existe.')
            elif suboperation == 'arista':
                src = int(usuario_input[2])
                dest = int(usuario_input[3])
                weight = int(usuario_input[4])
                if src not in g.nodos:
                    print('El nodo {} no existe'.format(src))
                elif dest not in g.nodos:
                    print('El nodo {} no existe.'.format(dest))
                else:
                    if not g.arista_existe(src, dest):
                        g.add_arista(src, dest, weight)
                    else:
                        print('La arista ya existe.')
     
        elif operation == 'bellman-ford':
            key = int(usuario_input[1])
            nodo_origen = g.get_nodo(key)
            distancia = bellman_ford(g, nodo_origen)            
            nodos = []
            for nodo in distancia:
                nodos.append((nodo.get_key(), distancia[nodo]))
            nodos =sorted(nodos, key=lambda tup: tup[0])
            
            from texttable import Texttable
            
            t = Texttable()
            row = ["Nodo"]
            row2 = ["Distancia"]
            for nodo in nodos:
                row.append(nodo[0])
                row2.append(nodo[1])
            t.add_row(row)
            t.add_row(row2)
            print(t.draw())
     
        elif operation == "mostrar":
            print('Nodos: ')
            for v in g:
                print(v.get_key())
            print()
     
            print('Aristas: ')
            for v in g:
                for dest in v.get_nodos_adyacentes():
                    w = v.get_weight(dest)
                    print('(src={}, dest={}, peso={}) '.format(v.get_key(),
                                                                 dest.get_key(), w))
            print()
     
        elif operation == 'salir':
            break
 
def main():
    crearGrafo()     
if __name__ == "__main__": main()
    
    






