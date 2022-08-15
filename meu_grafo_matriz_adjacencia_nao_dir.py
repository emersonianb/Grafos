from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        aux = set()
        vertices = set()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        aux.add("{}-{}".format(self.M[i][j][x].getV1(), self.M[i][j][x].getV2()))
                        aux.add("{}-{}".format(self.M[i][j][x].getV2(), self.M[i][j][x].getV1()))
        for i in self.N:
            for x in self.N:
                if i != x:
                    if str(i) + "-" + str(x) not in aux and str(x) + "-" + str(i) not in vertices:
                        vertices.add("{}-{}".format(str(i), str(x)))
                        vertices.add("{}-{}".format(str(x), str(i)))
        print(aux)
        return vertices

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
            if len(self.M[i][i]) > 0:
                return True
            return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N:
            raise VerticeInvalidoException
        cont = 0
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getV1() == V or self.M[i][j][x].getV2() == V:
                            if self.M[i][j][x].getV1() == self.M[i][j][x].getV2():
                                cont += 2
                            else:
                                cont += 1
        return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x, v1 in enumerate(self.M[i][j]):
                    for z, v2 in enumerate(self.M[i][j]):
                        if x > z and ([self.M[i][j][v1].getV1(), self.M[i][j][v1].getV2()] == [self.M[i][j][v2].getV2(),
                                                                                               self.M[i][j][
                                                                                                   v2].getV1()] or
                                      [self.M[i][j][v1].getV1(), self.M[i][j][v1].getV2()] == [self.M[i][j][v2].getV1(),
                                                                                               self.M[i][j][
                                                                                                   v2].getV2()]):
                            return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        arestas = set()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getV1() == V or self.M[i][j][x].getV2() == V:
                            arestas.add(self.M[i][j][x].getRotulo())
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas() or self.vertices_nao_adjacentes():
            return False
        return True

    def vertices_partindo_de(self, v):
        lista = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] != self.SEPARADOR_ARESTA:
                    n = len(self.M[i][j])
                    if (n >= 1) and (self.N[i] == v or self.N[j] == v):
                        for c in range(n):
                            if self.N[i] == v:
                                if self.N[j] not in lista:
                                    lista.append(self.N[j])
                            elif self.N[j] == v:
                                if self.N[i] not in lista:
                                    lista.append(self.N[i])

        return lista

    def djikstra(self, vi, vf):
        import math

        vertices = self.N
        lista_menor_caminho = []

        beta = {}
        pi = {}

        nao_visitados = []

        for vertice in vertices:
            beta[vertice] = math.inf
            pi[vertice] = '0'
            nao_visitados.append(vertice)
        beta[vi] = 0
        nao_visitados.remove(vi)
        w = vi
        while w != vf:
            lista_aresta = self.vertices_partindo_de(w)
            for r in lista_aresta:
                if r in nao_visitados:
                    if beta[r] > (beta[w] + 1):
                        beta[r] = (beta[w] + 1)
                        pi[r] = w

            menor_beta = math.inf
            r_menor_beta = 0
            for r in nao_visitados:
                if beta[r] < menor_beta:
                    menor_beta = beta[r]
                    r_menor_beta = r

            if menor_beta == math.inf:
                return False

            R = r_menor_beta
            nao_visitados.remove(R)
            w = R

        lista_menor_caminho.append(vf)
        while vf != vi:
            lista_menor_caminho.append(pi[vf])
            vf = pi[vf]
        lista_menor_caminho.reverse()
        return lista_menor_caminho
