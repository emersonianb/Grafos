from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):
    '''
    def vertices_nao_adjacentes(self):
        li = set()
        for i in self.N:
            v_adj = list()
            for j in self.A:
                if self.A[j].getV1() == i:
                    v_adj.append(self.A[j].getV2())
                elif self.A[j].getV2() == i:
                    v_adj.append(self.A[j].getV1())

            for k in self.N:
                if i == k:
                    pass
                elif k not in v_adj:
                    vs = (i + '-' + k)
                    li.add(vs)

        return li

    def ha_laco(self):
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True

    def grau(self, V=''):
        if V not in self.N:
            raise VerticeInvalidoException("O vertice passado é invalido")
        grau = 0
        for i in self.A:
            if self.A[i].getV1() == V:
                grau += 1
            if self.A[i].getV2() == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        arestas = self.A

        for i in arestas:
            a1 = arestas[i]
            for j in arestas:
                a2 = arestas[j]
                if a1 == a2:
                    continue

                if a1.getV1() == a2.getV1():
                    if a1.getV2() == a2.getV2():
                        return True

                if a1.getV1() == a2.getV2():
                    if a1.getV2() == a2.getV1:
                        return True
        return False

    def arestas_sobre_vertice(self, V):
        if V not in self.N:
            raise VerticeInvalidoException("O vértice passado não existe")

        arestas = set()
        for i in self.A:
            if self.A[i].getV1() == V or self.A[i].getV2() == V:
                if i not in arestas:
                    arestas.add(i)

        return arestas

    def arestas_sobre_vertice_list(self, V):
        if V not in self.N:
            raise VerticeInvalidoException("O vértice passado não existe")

        arestas = list()
        for i in self.A:
            if self.A[i].getV1() == V or self.A[i].getV2() == V:
                if i not in arestas:
                    arestas.append(i)

        return arestas

    def eh_completo(self):
        n_a = len(self.A)
        n_v = len(self.N)

        if n_v * (n_v - 1) / 2 == n_a:
            return True
        else:
            return False

    def dfs_p(self, r):
        visitados = list()
        arvore_dfs = set()
        self.dfs(r, visitados, arvore_dfs)
        return arvore_dfs

    def dfs(self, r, visitados, arvore_dfs):
        for a in self.arestas_sobre_vertice_list(r):
            rotulo = ("{}-{}".format(self.A[a].getV1(), self.A[a].getV2()))
            if self.A[a].getV1() == r:
                if rotulo not in arvore_dfs and self.A[a].getV2() not in visitados:
                    v = self.A[a].getV2()
                    arvore_dfs.add("{}-{}".format(self.A[a].getV1(), self.A[a].getV2()))
                    visitados.append(v)
                    self.dfs(v, visitados, arvore_dfs)
            elif self.A[a].getV2() == r:
                if rotulo not in arvore_dfs and self.A[a].getV1() not in visitados:
                    v = self.A[a].getV1()
                    arvore_dfs.add("{}-{}".format(self.A[a].getV1(), self.A[a].getV2()))
                    visitados.append(v)
                    self.dfs(v, visitados, arvore_dfs)
        return arvore_dfs

    def bfs(self, r):
        visitados = list()
        linha = list()
        fila = list()
        fila.append(r)
        visitados.append(r)
        while fila:
            s = fila.pop(0)
            g = self.arestas_sobre_vertice_list(s)
            for i in g:
                if self.A[i].getV1() != s:
                    a = self.A[i].getV1()
                else:
                    a = self.A[i].getV2()
                if a not in visitados:
                    fila.append(a)
                    linha.append("{}-{}".format(self.A[i].getV1(), self.A[i].getV2()))
                    visitados.append(a)

        return linha

    def ha_ciclo(self):
        lista = []
        lista2 = []
        v = self.N
        self.ha_ciclo_recursiva(v[0], lista)
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] == lista[j]:
                    lista2 = lista[i:j + 1:]
                    if lista2:
                        return True
        return False

        # return lista2

    def ha_ciclo_recursiva(self, v, lista):
        lista_aresta = self.A
        lista_v = self.arestas_sobre_vertice(v)

        if v not in lista:
            lista.append(v)
        else:
            lista.append(v)
            return

        for i in lista_v:
            if i not in lista:
                v1 = lista_aresta[i].getV1()
                v2 = lista_aresta[i].getV2()
                if v1 != v:
                    lista.append(i)
                    self.ha_ciclo_recursiva(v1, lista)
                if v2 != v:
                    lista.append(i)
                    self.ha_ciclo_recursiva(v2, lista)

    def eh_conexo(self):
        arestas = list()
        for i in self.A:
            arestas.append(self.A[i].getV1() + "-" + self.A[i].getV2())

        vertices = self.N

        listaadj = []

        for vertice in vertices:

            if len(listaadj) < 1:
                listaadj.append(vertice)

            if vertice in listaadj:
                for aresta in arestas:
                    # Perguntamos se o vertice atual esta presente na aresta atual
                    if vertice in aresta:
                        if vertice == aresta[0] and aresta[2] not in listaadj:
                            listaadj.append(aresta[2])
                        elif vertice == aresta[2] and aresta[0] not in listaadj:
                            listaadj.append(aresta[0])
        if len(listaadj) == len(self.N):
            return True
        else:
            return False

    def total_v(self, lis):
        lista_v = self.N
        cont = 0
        for a in lis:
            if a in lista_v:
                cont += 1
        return cont

    def caminho_dois_v(self, x, y):
        lista_a = self.A
        for aresta in lista_a:
            if (lista_a[aresta].getV1() == x) and (lista_a[aresta].getV2() == y):
                return aresta

    def caminho(self, tamanho):
        lista = []
        lista_v = self.N
        v = lista_v[0]
        lista = self.caminho_rec(v, tamanho, lista)
        if lista is None:
            return False
        return lista

    def caminho_rec(self, v, tam, lis):
        lista_aresta = self.A
        keys = list(lista_aresta.keys())
        n = 0
        if v not in lis:
            if len(lis) > 0:
                ar = self.caminho_dois_v(lis[(len(lis) - 1)], v)
                lis.append(ar)
            lis.append(v)
            for aresta in lista_aresta:
                v1 = lista_aresta[aresta].getV1()
                v2 = lista_aresta[aresta].getV2()
                paralela = self.ha_paralelas()
                if paralela:
                    v1 = lista_aresta[keys[n + 1]].getV1()
                    v2 = lista_aresta[keys[n + 1]].getV2()
                    if n == len(keys):
                        n = 0
                    if tam == self.total_v(lis):
                        return lis
                    if v1 != v:
                        self.caminho_rec(v1, tam, lis)
                    elif v2 != v:
                        self.caminho_rec(v2, tam, lis)
                else:
                    if n == len(keys):
                        n = 0
                    if tam == self.total_v(lis):
                        return lis
                    if v1 != v:
                        self.caminho_rec(v1, tam, lis)
                    elif v2 != v:
                        self.caminho_rec(v2, tam, lis)
'''

'''
    def caminho(self, n):
        for vertice in self.N:
            caminho = self.dfs_p(vertice)
            if (len(caminho) == (n * 2 + 1)):
                return caminho
            elif (len(caminho) > (n * 2 + 1)):
                caminho = caminho[0:n * 2 + 1]
                return caminho
        return False
        
    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass
'''
