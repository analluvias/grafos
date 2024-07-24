from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        m1_simplificada = []

        for linha in range(len(self.vertices)):
            linha_simplificada = []
            for coluna in range(len(self.vertices)):
                if len(self.arestas[linha][coluna]) >= 1:
                    linha_simplificada.append(1)
                else:
                    linha_simplificada.append(0)
            m1_simplificada.append(linha_simplificada)

        for linha in range(len(self.vertices)):  # i
            for coluna in range(len(self.vertices)):  # j
                # testando se verticalmente, tem um 1 naquele indice
                if m1_simplificada[coluna][linha] == 1:
                    for colunas_do_indice_que_tem_1 in range(len(self.vertices)):  # k
                        # compara linha que começa com 1 com a linha que tem o indice da coluna da vez
                        if m1_simplificada[coluna][colunas_do_indice_que_tem_1] >= m1_simplificada[linha]\
                                [colunas_do_indice_que_tem_1]:
                            pass
                        else:
                            m1_simplificada[coluna][colunas_do_indice_que_tem_1] = m1_simplificada[linha]\
                                [colunas_do_indice_que_tem_1]
        return m1_simplificada
