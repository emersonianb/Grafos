from unittest import TestCase
from meu_grafo import *


class TestMeuGrafo(TestCase):

    def setUp(self):
        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'B', 'A')

        # Busca em profundidade
        self.g_bp = MeuGrafo(["J", "C", "E", "P", "M", "T", "Z"])

        self.g_bp.adicionaAresta("a1", v1="J", v2="C")
        self.g_bp.adicionaAresta("a2", v1="C", v2="E")
        self.g_bp.adicionaAresta("a3", v1="C", v2="E")
        self.g_bp.adicionaAresta("a4", v1="C", v2="P")
        self.g_bp.adicionaAresta("a5", v1="C", v2="P")
        self.g_bp.adicionaAresta("a6", v1="C", v2="M")
        self.g_bp.adicionaAresta("a7", v1="C", v2="T")
        self.g_bp.adicionaAresta("a8", v1="M", v2="T")
        self.g_bp.adicionaAresta("a9", v1="T", v2="Z")
        """
        self.g_bp = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_bp.adicionaAresta('a1', 'A', 'B')
        self.g_bp.adicionaAresta('a2', 'A', 'D')
        self.g_bp.adicionaAresta('a3', 'A', 'C')
        self.g_bp.adicionaAresta('a4', 'B', 'C')
        self.g_bp.adicionaAresta('a5', 'B', 'G')
        self.g_bp.adicionaAresta('a6', 'B', 'J')
        self.g_bp.adicionaAresta('a7', 'B', 'I')
        self.g_bp.adicionaAresta('a8', 'B', 'K')
        self.g_bp.adicionaAresta('a9', 'H', 'G')
        self.g_bp.adicionaAresta('a10', 'G', 'C')
        self.g_bp.adicionaAresta('a11', 'C', 'F')
        self.g_bp.adicionaAresta('a12', 'F', 'D')
        self.g_bp.adicionaAresta('a13', 'D', 'C')
        self.g_bp.adicionaAresta('a14', 'D', 'E')
        """

        # Grafo desconxeo
        self.g_dcnx = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'K', 'W'])
        self.g_dcnx.adicionaAresta('a1', 'J', 'C')
        self.g_dcnx.adicionaAresta('a2', 'C', 'E')
        self.g_dcnx.adicionaAresta('a3', 'E', 'P')
        self.g_dcnx.adicionaAresta('a4', 'P', 'M')
        self.g_dcnx.adicionaAresta('a5', 'M', 'T')
        self.g_dcnx.adicionaAresta('a6', 'T', 'Z')
        self.g_dcnx.adicionaAresta('a7', 'Z', 'J')
        self.g_dcnx.adicionaAresta('a8', 'K', 'W')

        # Grafo sem ciclo
        self.g_sc = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'K', 'W'])
        self.g_sc.adicionaAresta('a1', 'J', 'C')
        self.g_sc.adicionaAresta('a2', 'C', 'E')
        self.g_sc.adicionaAresta('a3', 'E', 'P')
        self.g_sc.adicionaAresta('a4', 'P', 'M')
        self.g_sc.adicionaAresta('a5', 'M', 'T')
        self.g_sc.adicionaAresta('a6', 'Z', 'J')
        self.g_sc.adicionaAresta('a7', 'K', 'W')

    def test_dfs(self):
        self.assertEqual(self.g_bp.dfs_p('J'), {'J-C', 'C-E', 'C-P', 'C-M', 'M-T', 'T-Z'})
        self.assertEqual(self.g_bp.dfs_p('C'), {'J-C', 'C-E', 'C-P', 'C-M', 'M-T', 'C-T', 'T-Z'})
        self.assertEqual(self.g_bp.dfs_p('E'), {'J-C', 'C-E', 'C-P', 'C-M', 'M-T', 'T-Z'})
        self.assertEqual(self.g_bp.dfs_p('M'), {'C-M', 'J-C', 'C-E', 'C-P', 'C-T', 'M-T', 'T-Z'})
        self.assertEqual(self.g_bp.dfs_p('T'), {'C-M', 'J-C', 'C-E', 'C-P', 'C-T', 'M-T', 'T-Z'})
        self.assertEqual(self.g_bp.dfs_p('Z'), {'C-P', 'T-Z', 'J-C', 'C-E', 'C-M', 'C-T'})
        self.assertEqual(self.g_bp.dfs_p('P'), {'C-E', 'T-Z', 'J-C', 'C-M', 'C-P', 'M-T'})

    def test_bfs(self):
        self.assertEqual(self.g_bp.bfs("J"), ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'T-Z'])
        self.assertEqual(self.g_bp.bfs("C"), ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'T-Z'])
        self.assertEqual(self.g_bp.bfs("E"), ['C-E', 'J-C', 'C-P', 'C-M', 'C-T', 'T-Z'])
        self.assertEqual(self.g_bp.bfs("M"), ['C-M', 'M-T', 'J-C', 'C-E', 'C-P', 'T-Z'])
        self.assertEqual(self.g_bp.bfs("T"), ['C-T', 'M-T', 'T-Z', 'J-C', 'C-E', 'C-P'])
        self.assertEqual(self.g_bp.bfs("Z"), ['T-Z', 'C-T', 'M-T', 'J-C', 'C-E', 'C-P'])
        self.assertEqual(self.g_bp.bfs("T"), ['C-T', 'M-T', 'T-Z', 'J-C', 'C-E', 'C-P'])
        self.assertEqual(self.g_bp.bfs("P"), ['C-P', 'J-C', 'C-E', 'C-M', 'C-T', 'T-Z'])

    def test_ha_ciclo(self):
        self.assertEqual(self.g_bp.ha_ciclo(), True)
        self.assertEqual(self.g_sc.ha_ciclo(), False)
        self.assertEqual(self.g_dcnx.ha_ciclo(), True)

    def test_eh_conexo(self):
        self.assertEqual(self.g_bp.eh_conexo(), True)
        self.assertEqual(self.g_dcnx.eh_conexo(), False)
        self.assertEqual(self.g_sc.eh_conexo(), False)

    def test_caminho(self):
        self.assertEqual(self.g_bp.caminho(4), False)
        self.assertEqual(self.g_bp.caminho(3), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_dcnx.caminho(5), ['J', 'a1', 'C', 'a2', 'E', 'a3', 'P', 'a4', 'M'])
        self.assertEqual(self.g_sc.caminho(1), ['J'])
        self.assertEqual(self.g_sc.caminho(4), ['J', 'a1', 'C', 'a2', 'E', 'a3', 'P'])
        self.assertEqual(self.g_l1.caminho(2), ['A', 'a2', 'B'])
