from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

paraiba = GrafoListaAdjacencia(["J", "C", "E", "P", "M", "T", "Z"])

paraiba.adicionaAresta("a1", v1="J", v2="C")
paraiba.adicionaAresta("a2", v1="C", v2="E")
paraiba.adicionaAresta("a3", v1="C", v2="E")
paraiba.adicionaAresta("a4", v1="C", v2="P")
paraiba.adicionaAresta("a5", v1="C", v2="P")
paraiba.adicionaAresta("a6", v1="C", v2="M")
paraiba.adicionaAresta("a7", v1="C", v2="T")
paraiba.adicionaAresta("a8", v1="M", v2="T")
paraiba.adicionaAresta("a9", v1="T", v2="Z")

print(paraiba)