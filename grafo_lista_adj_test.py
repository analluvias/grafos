# import unittest
# from meu_grafo_lista_adj import *
# from bibgrafo.grafo_errors import *
# from bibgrafo.aresta import Aresta
#
#
# class TestGrafo(unittest.TestCase):
#
#     maxDiff = None
#
#     def setUp(self):
#         # Grafo da Paraíba
#         self.g_p = MeuGrafo()
#         self.g_p.adiciona_vertice("J")
#         self.g_p.adiciona_vertice("C")
#         self.g_p.adiciona_vertice("E")
#         self.g_p.adiciona_vertice("P")
#         self.g_p.adiciona_vertice("M")
#         self.g_p.adiciona_vertice("T")
#         self.g_p.adiciona_vertice("Z")
#         self.g_p.adiciona_aresta('a1', 'J', 'C')
#         self.g_p.adiciona_aresta('a2', 'C', 'E')
#         self.g_p.adiciona_aresta('a3', 'C', 'E')
#         self.g_p.adiciona_aresta('a4', 'P', 'C')
#         self.g_p.adiciona_aresta('a5', 'P', 'C')
#         self.g_p.adiciona_aresta('a6', 'T', 'C')
#         self.g_p.adiciona_aresta('a7', 'M', 'C')
#         self.g_p.adiciona_aresta('a8', 'M', 'T')
#         self.g_p.adiciona_aresta('a9', 'T', 'Z')
#
#         # Clone do Grafo da Paraíba para ver se o método equals está funcionando
#         self.g_p2 = MeuGrafo()
#         self.g_p2.adiciona_vertice("J")
#         self.g_p2.adiciona_vertice("C")
#         self.g_p2.adiciona_vertice("E")
#         self.g_p2.adiciona_vertice("P")
#         self.g_p2.adiciona_vertice("M")
#         self.g_p2.adiciona_vertice("T")
#         self.g_p2.adiciona_vertice("Z")
#         self.g_p2.adiciona_aresta('a1', 'J', 'C')
#         self.g_p2.adiciona_aresta('a2', 'C', 'E')
#         self.g_p2.adiciona_aresta('a3', 'C', 'E')
#         self.g_p2.adiciona_aresta('a4', 'P', 'C')
#         self.g_p2.adiciona_aresta('a5', 'P', 'C')
#         self.g_p2.adiciona_aresta('a6', 'T', 'C')
#         self.g_p2.adiciona_aresta('a7', 'M', 'C')
#         self.g_p2.adiciona_aresta('a8', 'M', 'T')
#         self.g_p2.adiciona_aresta('a9', 'T', 'Z')
#
#         # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
#         # Esse tem um pequena diferença na primeira aresta
#         self.g_p3 = MeuGrafo()
#         self.g_p3.adiciona_vertice("J")
#         self.g_p3.adiciona_vertice("C")
#         self.g_p3.adiciona_vertice("E")
#         self.g_p3.adiciona_vertice("P")
#         self.g_p3.adiciona_vertice("M")
#         self.g_p3.adiciona_vertice("T")
#         self.g_p3.adiciona_vertice("Z")
#         self.g_p3.adiciona_aresta('a', 'J', 'C')
#         self.g_p3.adiciona_aresta('a2', 'C', 'E')
#         self.g_p3.adiciona_aresta('a3', 'C', 'E')
#         self.g_p3.adiciona_aresta('a4', 'P', 'C')
#         self.g_p3.adiciona_aresta('a5', 'P', 'C')
#         self.g_p3.adiciona_aresta('a6', 'T', 'C')
#         self.g_p3.adiciona_aresta('a7', 'M', 'C')
#         self.g_p3.adiciona_aresta('a8', 'M', 'T')
#         self.g_p3.adiciona_aresta('a9', 'T', 'Z')
#
#         # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
#         # Esse tem um pequena diferença na segunda aresta
#         self.g_p4 = MeuGrafo()
#         self.g_p4.adiciona_vertice("J")
#         self.g_p4.adiciona_vertice("C")
#         self.g_p4.adiciona_vertice("E")
#         self.g_p4.adiciona_vertice("P")
#         self.g_p4.adiciona_vertice("M")
#         self.g_p4.adiciona_vertice("T")
#         self.g_p4.adiciona_vertice("Z")
#         self.g_p4.adiciona_aresta('a1', 'J', 'C')
#         self.g_p4.adiciona_aresta('a2', 'J', 'E')
#         self.g_p4.adiciona_aresta('a3', 'C', 'E')
#         self.g_p4.adiciona_aresta('a4', 'P', 'C')
#         self.g_p4.adiciona_aresta('a5', 'P', 'C')
#         self.g_p4.adiciona_aresta('a6', 'T', 'C')
#         self.g_p4.adiciona_aresta('a7', 'M', 'C')
#         self.g_p4.adiciona_aresta('a8', 'M', 'T')
#         self.g_p4.adiciona_aresta('a9', 'T', 'Z')
#
#         # Grafo da Paraíba sem arestas paralelas
#         self.g_p_sem_paralelas = MeuGrafo()
#         self.g_p_sem_paralelas.adiciona_vertice("J")
#         self.g_p_sem_paralelas.adiciona_vertice("C")
#         self.g_p_sem_paralelas.adiciona_vertice("E")
#         self.g_p_sem_paralelas.adiciona_vertice("P")
#         self.g_p_sem_paralelas.adiciona_vertice("M")
#         self.g_p_sem_paralelas.adiciona_vertice("T")
#         self.g_p_sem_paralelas.adiciona_vertice("Z")
#         self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
#         self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
#         self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
#         self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
#         self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
#         self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
#         self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')
#
#         # Grafos completos
#         self.g_c = MeuGrafo()
#         self.g_c.adiciona_vertice("J")
#         self.g_c.adiciona_vertice("C")
#         self.g_c.adiciona_vertice("E")
#         self.g_c.adiciona_vertice("P")
#         self.g_c.adiciona_aresta('a1', 'J', 'C')
#         self.g_c.adiciona_aresta('a2', 'J', 'E')
#         self.g_c.adiciona_aresta('a3', 'J', 'P')
#         self.g_c.adiciona_aresta('a4', 'E', 'C')
#         self.g_c.adiciona_aresta('a5', 'P', 'C')
#         self.g_c.adiciona_aresta('a6', 'P', 'E')
#
#         # arvore grafo completo dfs
#         self.a_g_c_dfs = MeuGrafo()
#         self.a_g_c_dfs.adiciona_vertice("J")
#         self.a_g_c_dfs.adiciona_vertice("C")
#         self.a_g_c_dfs.adiciona_vertice("E")
#         self.a_g_c_dfs.adiciona_vertice("P")
#         self.a_g_c_dfs.adiciona_aresta('a1', 'J', 'C')
#         self.a_g_c_dfs.adiciona_aresta('a4', 'E', 'C')
#         self.a_g_c_dfs.adiciona_aresta('a6', 'P', 'E')
#
#         # arvore grafo completo bfs
#         self.a_g_c_bfs = MeuGrafo()
#         self.a_g_c_bfs.adiciona_vertice("J")
#         self.a_g_c_bfs.adiciona_vertice("C")
#         self.a_g_c_bfs.adiciona_vertice("E")
#         self.a_g_c_bfs.adiciona_vertice("P")
#         self.a_g_c_bfs.adiciona_aresta('a1', 'J', 'C')
#         self.a_g_c_bfs.adiciona_aresta('a2', 'J', 'E')
#         self.a_g_c_bfs.adiciona_aresta('a3', 'J', 'P')
#
#         self.g_c2 = MeuGrafo()
#         self.g_c2.adiciona_vertice("Nina")
#         self.g_c2.adiciona_vertice("Maria")
#         self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')
#
#         self.g_c3 = MeuGrafo()
#         self.g_c3.adiciona_vertice("Único")
#
#         # GRAFO DFS -> julgo ser verdadeira
#         self.g_c_dfs = MeuGrafo()
#         self.g_c_dfs.adiciona_vertice("J")
#         self.g_c_dfs.adiciona_vertice("C")
#         self.g_c_dfs.adiciona_vertice("E")
#         self.g_c_dfs.adiciona_vertice("P")
#         self.g_c_dfs.adiciona_aresta('a1', 'J', 'C')
#         self.g_c_dfs.adiciona_aresta('a5', 'P', 'C')
#         self.g_c_dfs.adiciona_aresta('a6', 'P', 'E')
#
#         # Grafos com laco
#         self.g_l1 = MeuGrafo()
#         self.g_l1.adiciona_vertice("A")
#         self.g_l1.adiciona_vertice("B")
#         self.g_l1.adiciona_vertice("C")
#         self.g_l1.adiciona_vertice("D")
#         self.g_l1.adiciona_aresta('a1', 'A', 'A')
#         self.g_l1.adiciona_aresta('a2', 'A', 'B')
#         self.g_l1.adiciona_aresta('a3', 'A', 'A')
#
#         self.g_l2 = MeuGrafo()
#         self.g_l2.adiciona_vertice("A")
#         self.g_l2.adiciona_vertice("B")
#         self.g_l2.adiciona_vertice("C")
#         self.g_l2.adiciona_vertice("D")
#         self.g_l2.adiciona_aresta('a1', 'A', 'B')
#         self.g_l2.adiciona_aresta('a2', 'B', 'B')
#         self.g_l2.adiciona_aresta('a3', 'B', 'A')
#
#         self.g_l3 = MeuGrafo()
#         self.g_l3.adiciona_vertice("A")
#         self.g_l3.adiciona_vertice("B")
#         self.g_l3.adiciona_vertice("C")
#         self.g_l3.adiciona_vertice("D")
#         self.g_l3.adiciona_aresta('a1', 'C', 'A')
#         self.g_l3.adiciona_aresta('a2', 'C', 'C')
#         self.g_l3.adiciona_aresta('a3', 'D', 'D')
#         self.g_l3.adiciona_aresta('a4', 'D', 'D')
#
#         self.g_l4 = MeuGrafo()
#         self.g_l4.adiciona_vertice("D")
#         self.g_l4.adiciona_aresta('a1', 'D', 'D')
#
#         self.g_l5 = MeuGrafo()
#         self.g_l5.adiciona_vertice("C")
#         self.g_l5.adiciona_vertice("D")
#         self.g_l5.adiciona_aresta('a1', 'D', 'C')
#         self.g_l5.adiciona_aresta('a2', 'C', 'C')
#
#         # Grafos desconexos
#         self.g_d = MeuGrafo()
#         self.g_d.adiciona_vertice("A")
#         self.g_d.adiciona_vertice("B")
#         self.g_d.adiciona_vertice("C")
#         self.g_d.adiciona_vertice("D")
#         self.g_d.adiciona_aresta('asd', 'A', 'B')
#
#         self.g_d2 = MeuGrafo()
#         self.g_d2.adiciona_vertice("A")
#         self.g_d2.adiciona_vertice("B")
#         self.g_d2.adiciona_vertice("C")
#         self.g_d2.adiciona_vertice("D")
#
#     def test_adiciona_aresta(self):
#         self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
#
#         a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
#         self.assertTrue(self.g_p.adiciona_aresta(a))
#         with self.assertRaises(ArestaInvalidaError):
#             self.assertTrue(self.g_p.adiciona_aresta(a))
#         with self.assertRaises(VerticeInvalidoError):
#             self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
#         with self.assertRaises(VerticeInvalidoError):
#             self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
#         with self.assertRaises(NotImplementedError):
#             self.g_p.adiciona_aresta('')
#         with self.assertRaises(NotImplementedError):
#             self.g_p.adiciona_aresta('aa-bb')
#         with self.assertRaises(VerticeInvalidoError):
#             self.g_p.adiciona_aresta('x', 'J', 'V')
#         with self.assertRaises(ArestaInvalidaError):
#             self.g_p.adiciona_aresta('a1', 'J', 'C')
#
#     def test_eq(self):
#         self.assertEqual(self.g_p, self.g_p2)
#
#         self.assertNotEqual(self.g_p, self.g_p3)
#         self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
#         self.assertNotEqual(self.g_p, self.g_p4)
#
#     def test_vertices_nao_adjacentes(self):
#         self.assertEqual(self.g_p.vertices_nao_adjacentes(),
#                          {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
#                           'M-Z'})
#
#         self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
#         self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
#         self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
#         self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
#
#     def test_ha_laco(self):
#         self.assertFalse(self.g_p.ha_laco())
#
#         self.assertFalse(self.g_p2.ha_laco())
#         self.assertFalse(self.g_p3.ha_laco())
#         self.assertFalse(self.g_p4.ha_laco())
#         self.assertFalse(self.g_p_sem_paralelas.ha_laco())
#         self.assertFalse(self.g_d.ha_laco())
#         self.assertFalse(self.g_c.ha_laco())
#         self.assertFalse(self.g_c2.ha_laco())
#         self.assertFalse(self.g_c3.ha_laco())
#         self.assertTrue(self.g_l1.ha_laco())
#         self.assertTrue(self.g_l2.ha_laco())
#         self.assertTrue(self.g_l3.ha_laco())
#         self.assertTrue(self.g_l4.ha_laco())
#         self.assertTrue(self.g_l5.ha_laco())
#
#     def test_grau(self):
#         # Paraíba
#         self.assertEqual(self.g_p.grau('J'), 1)
#         self.assertEqual(self.g_p.grau('C'), 7)
#         self.assertEqual(self.g_p.grau('E'), 2)
#         self.assertEqual(self.g_p.grau('P'), 2)
#         self.assertEqual(self.g_p.grau('M'), 2)
#         self.assertEqual(self.g_p.grau('T'), 3)
#         self.assertEqual(self.g_p.grau('Z'), 1)
#         with self.assertRaises(VerticeInvalidoError):
#             self.assertEqual(self.g_p.grau('G'), 5)
#
#         self.assertEqual(self.g_d.grau('A'), 1)
#         self.assertEqual(self.g_d.grau('C'), 0)
#         self.assertNotEqual(self.g_d.grau('D'), 2)
#         self.assertEqual(self.g_d2.grau('A'), 0)
#
#         # Completos
#         self.assertEqual(self.g_c.grau('J'), 3)
#         self.assertEqual(self.g_c.grau('C'), 3)
#         self.assertEqual(self.g_c.grau('E'), 3)
#         self.assertEqual(self.g_c.grau('P'), 3)
#
#         # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
#         self.assertEqual(self.g_l1.grau('A'), 5)
#         self.assertEqual(self.g_l2.grau('B'), 4)
#         self.assertEqual(self.g_l4.grau('D'), 2)
#
#     def test_ha_paralelas(self):
#         self.assertTrue(self.g_p.ha_paralelas())
#
#         self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
#         self.assertFalse(self.g_c.ha_paralelas())
#         self.assertFalse(self.g_c2.ha_paralelas())
#         self.assertFalse(self.g_c3.ha_paralelas())
#         self.assertTrue(self.g_l1.ha_paralelas())
#
#     def test_arestas_sobre_vertice(self):
#         self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
#
#         self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
#         self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
#         self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
#         self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
#         self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
#         with self.assertRaises(VerticeInvalidoError):
#             self.g_p.arestas_sobre_vertice('A')
#
#     def test_eh_completo(self):
#         self.assertFalse(self.g_p.eh_completo())
#
#         self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
#         self.assertTrue((self.g_c.eh_completo()))
#         self.assertTrue((self.g_c2.eh_completo()))
#         self.assertTrue((self.g_c3.eh_completo()))
#         self.assertFalse((self.g_l1.eh_completo()))
#         self.assertFalse((self.g_l2.eh_completo()))
#         self.assertFalse((self.g_l3.eh_completo()))
#         self.assertFalse((self.g_l4.eh_completo()))
#         self.assertFalse((self.g_l5.eh_completo()))
#         self.assertFalse((self.g_d.eh_completo()))
#         self.assertFalse((self.g_d2.eh_completo()))
#
#     def test_dfs(self):
#         resultado_dfs = self.g_c.dfs()
#
#         self.assertEqual(resultado_dfs.tam_arestas(), self.a_g_c_dfs.tam_arestas())
#         self.assertEqual(resultado_dfs.vertices, self.a_g_c_dfs.vertices)
#         self.assertEqual(resultado_dfs.arestas, self.a_g_c_dfs.arestas)
#         self.assertEqual(resultado_dfs, self.a_g_c_dfs)
#
#     def test_bfs(self):
#         resultado_bfs = self.g_c.bfs()
#
#         # self.assertEqual(resultado_bfs.tam_arestas(), self.a_g_c_bfs.tam_arestas())
#         # self.assertEqual(resultado_bfs.vertices, self.a_g_c_bfs.vertices)
#         # self.assertEqual(resultado_bfs.arestas, self.a_g_c_bfs.arestas)
#         self.assertEqual(resultado_bfs, self.a_g_c_bfs)


import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        # arvore grafo completo dfs
        self.a_g_c_dfs = MeuGrafo()
        self.a_g_c_dfs.adiciona_vertice("J")
        self.a_g_c_dfs.adiciona_vertice("C")
        self.a_g_c_dfs.adiciona_vertice("E")
        self.a_g_c_dfs.adiciona_vertice("P")
        self.a_g_c_dfs.adiciona_aresta('a1', 'J', 'C')
        self.a_g_c_dfs.adiciona_aresta('a4', 'E', 'C')
        self.a_g_c_dfs.adiciona_aresta('a6', 'P', 'E')

        # arvore grafo completo bfs
        self.a_g_c_bfs = MeuGrafo()
        self.a_g_c_bfs.adiciona_vertice("J")
        self.a_g_c_bfs.adiciona_vertice("C")
        self.a_g_c_bfs.adiciona_vertice("E")
        self.a_g_c_bfs.adiciona_vertice("P")
        self.a_g_c_bfs.adiciona_aresta('a1', 'J', 'C')
        self.a_g_c_bfs.adiciona_aresta('a4', 'E', 'C')
        self.a_g_c_bfs.adiciona_aresta('a6', 'P', 'E')

        # arvore grafo completo bfs
        self.a_g_c_bfs = MeuGrafo()
        self.a_g_c_bfs.adiciona_vertice("J")
        self.a_g_c_bfs.adiciona_vertice("C")
        self.a_g_c_bfs.adiciona_vertice("E")
        self.a_g_c_bfs.adiciona_vertice("P")
        self.a_g_c_bfs.adiciona_aresta('a1', 'J', 'C')
        self.a_g_c_bfs.adiciona_aresta('a2', 'J', 'E')
        self.a_g_c_bfs.adiciona_aresta('a3', 'J', 'P')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # GRAFO DFS -> julgo ser verdadeira
        self.g_c_dfs = MeuGrafo()
        self.g_c_dfs.adiciona_vertice("J")
        self.g_c_dfs.adiciona_vertice("C")
        self.g_c_dfs.adiciona_vertice("E")
        self.g_c_dfs.adiciona_vertice("P")
        self.g_c_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs.adiciona_aresta('a5', 'P', 'C')
        self.g_c_dfs.adiciona_aresta('a6', 'P', 'E')

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        # TESTE 2 BFS
        self.teste_2 = MeuGrafo()
        self.teste_2.adiciona_vertice("A")
        self.teste_2.adiciona_vertice("B")
        self.teste_2.adiciona_vertice("C")
        self.teste_2.adiciona_vertice("D")
        self.teste_2.adiciona_vertice("E")
        self.teste_2.adiciona_aresta('a1', 'A', 'C')
        self.teste_2.adiciona_aresta('a2', 'A', 'D')
        self.teste_2.adiciona_aresta('a3', 'D', 'B')
        self.teste_2.adiciona_aresta('a4', 'D', 'E')
        self.teste_2.adiciona_aresta('a5', 'B', 'E')

        self.teste_2_bfs = MeuGrafo()
        self.teste_2_bfs.adiciona_vertice("A")
        self.teste_2_bfs.adiciona_vertice("B")
        self.teste_2_bfs.adiciona_vertice("C")
        self.teste_2_bfs.adiciona_vertice("D")
        self.teste_2_bfs.adiciona_vertice("E")
        self.teste_2_bfs.adiciona_aresta('a1', 'A', 'C')
        self.teste_2_bfs.adiciona_aresta('a2', 'A', 'D')
        self.teste_2_bfs.adiciona_aresta('a3', 'D', 'B')
        self.teste_2_bfs.adiciona_aresta('a4', 'D', 'E')

        self.teste_2_dfs = MeuGrafo()
        self.teste_2_dfs.adiciona_vertice("A")
        self.teste_2_dfs.adiciona_vertice("B")
        self.teste_2_dfs.adiciona_vertice("C")
        self.teste_2_dfs.adiciona_vertice("D")
        self.teste_2_dfs.adiciona_vertice("E")
        self.teste_2_dfs.adiciona_aresta('a1', 'A', 'C')
        self.teste_2_dfs.adiciona_aresta('a2', 'A', 'D')
        self.teste_2_dfs.adiciona_aresta('a3', 'D', 'B')
        self.teste_2_dfs.adiciona_aresta('a5', 'B', 'E')

        self.hc = MeuGrafo()
        self.hc.adiciona_vertice("A")
        self.hc.adiciona_vertice("B")
        self.hc.adiciona_vertice("C")
        self.hc.adiciona_vertice("D")
        self.hc.adiciona_vertice("E")
        self.hc.adiciona_aresta('a1', 'A', 'B')
        self.hc.adiciona_aresta('a2', 'A', 'B')
        self.hc.adiciona_aresta('a3', 'B', 'C')
        self.hc.adiciona_aresta('a4', 'C', 'D')
        self.hc.adiciona_aresta('a5', 'C', 'E')

        self.hc2 = MeuGrafo()
        self.hc2.adiciona_vertice("A")
        self.hc2.adiciona_vertice("B")
        self.hc2.adiciona_vertice("C")
        self.hc2.adiciona_vertice("D")
        self.hc2.adiciona_aresta('a1', 'A', 'B')
        self.hc2.adiciona_aresta('a2', 'B', 'C')
        self.hc2.adiciona_aresta('a3', 'C', 'D')
        self.hc2.adiciona_aresta('a4', 'D', 'A')

        self.hc3 = MeuGrafo()
        self.hc3.adiciona_vertice("A")
        self.hc3.adiciona_vertice("B")
        self.hc3.adiciona_vertice("C")
        self.hc3.adiciona_vertice("D")
        self.hc3.adiciona_aresta('a1', 'A', 'B')
        self.hc3.adiciona_aresta('a2', 'B', 'C')
        self.hc3.adiciona_aresta('a3', 'C', 'D')

        self.tcam = MeuGrafo()
        self.tcam.adiciona_vertice("A")
        self.tcam.adiciona_vertice("B")
        self.tcam.adiciona_vertice("C")
        self.tcam.adiciona_vertice("E")
        self.tcam.adiciona_aresta('a1', 'A', 'B')
        self.tcam.adiciona_aresta('a2', 'B', 'C')
        self.tcam.adiciona_aresta('a3', 'B', 'E')
        self.tcam.adiciona_aresta('a4', 'A', 'E')

        # teste caminho
        self.c1 = MeuGrafo()
        self.c1.adiciona_vertice("A")
        self.c1.adiciona_vertice("B")
        self.c1.adiciona_vertice("C")
        self.c1.adiciona_vertice("D")
        self.c1.adiciona_vertice("E")
        self.c1.adiciona_aresta('a1', 'A', 'B')
        self.c1.adiciona_aresta('a2', 'B', 'C')
        self.c1.adiciona_aresta('a3', 'B', 'E')
        self.c1.adiciona_aresta('a4', 'A', 'D')

        # desconexo 1
        self.g_desc = MeuGrafo()
        self.g_desc.adiciona_vertice("A")
        self.g_desc.adiciona_vertice("B")
        self.g_desc.adiciona_vertice("C")
        self.g_desc.adiciona_vertice("D")
        self.g_desc.adiciona_aresta('a1', 'A', 'B')

        # desconexo 2
        self.g_desc2 = MeuGrafo()
        self.g_desc2.adiciona_vertice("A")
        self.g_desc2.adiciona_vertice("B")
        self.g_desc2.adiciona_vertice("C")
        self.g_desc2.adiciona_vertice("D")

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))

        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)

        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})

        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())

        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())

        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})

        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())

        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        resultado_dfs = self.g_c.dfs()

        self.assertEqual(resultado_dfs.tam_arestas(), self.a_g_c_dfs.tam_arestas())
        self.assertEqual(resultado_dfs.vertices, self.a_g_c_dfs.vertices)
        self.assertEqual(resultado_dfs.arestas, self.a_g_c_dfs.arestas)
        self.assertEqual(resultado_dfs, self.a_g_c_dfs)

        resultado_dfs_2 = self.teste_2.dfs()

        self.assertEqual(resultado_dfs_2.tam_arestas(), self.teste_2_dfs.tam_arestas())
        self.assertEqual(resultado_dfs_2.arestas, self.teste_2_dfs.arestas)
        self.assertEqual(resultado_dfs_2, self.teste_2_dfs)

    def test_bfs(self):
        resultado_bfs = self.g_c.bfs()

        self.assertEqual(resultado_bfs, self.a_g_c_bfs)

        resultado_bfs_2 = self.teste_2.bfs()

        self.assertEqual(resultado_bfs_2.tam_arestas(), self.teste_2_bfs.tam_arestas())
        self.assertEqual(resultado_bfs_2.arestas, self.teste_2_bfs.arestas)
        self.assertEqual(resultado_bfs_2, self.teste_2_bfs)

    def test_ha_ciclo(self):
        ha_ciclo = self.teste_2.ha_ciclo()
        self.assertTrue(ha_ciclo)

        ha_ciclo_2 = self.hc.ha_ciclo()
        self.assertTrue(ha_ciclo_2)

        ha_ciclo_3 = self.hc2.ha_ciclo()
        self.assertTrue(ha_ciclo_3)

        ha_ciclo_4 = self.hc3.ha_ciclo()
        self.assertFalse(ha_ciclo_4)

    def test_caminho(self):
        c1 = self.c1
        self.assertEqual(c1.caminho(self.c1.vertices[0], self.c1.vertices[3], 0), ['A', 'a4', 'D'])

        c2 = self.tcam
        self.assertEqual(c2.caminho(self.c1.vertices[0], self.c1.vertices[4], 0), ['A', 'a1', 'B', 'a3', 'E'])

        c3 = self.g_c
        self.assertEqual(c3.caminho(self.g_c.vertices[0], self.g_c.vertices[3], 0), ['J', 'a1', 'C', 'a4', 'E', 'a6', 'P'])

    def test_conexo(self):
        self.assertFalse(self.g_desc.conexo())

        self.assertFalse(self.g_desc2.conexo())

        self.assertTrue(self.g_p.conexo())

        self.assertTrue(self.g_c.conexo())

        self.assertTrue(self.g_c2.conexo())

        self.assertFalse(self.g_l1.conexo())

        self.assertFalse(self.g_l2.conexo())

        self.assertFalse(self.g_l3.conexo())
