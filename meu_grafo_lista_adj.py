from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        arestas_existentes = set()

        vertices_nao_adjacentes = set()

        for a in self.arestas:
            arestas_existentes.add(f'{str(self.arestas[a].v1)}-{str(self.arestas[a].v2)}')

        for v in self.vertices:
            for w in self.vertices:

                if (f'{str(v)}-{str(w)}' not in arestas_existentes and f'{str(w)}-{str(v)}'
                        not in arestas_existentes) and str(v) != str(w):

                    if (f'{str(v)}-{str(w)}' not in vertices_nao_adjacentes and
                            f'{str(w)}-{str(v)}' not in vertices_nao_adjacentes):
                        vertices_nao_adjacentes.add(f'{str(v)}-{str(w)}')

        return vertices_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        grau = 0
        for vert in self.vertices:
            if str(vert) == V:

                for a in self.arestas:
                    if str(self.arestas[a].v1) == str(vert):
                        grau += 1

                    if str(self.arestas[a].v2) == str(vert):
                        grau += 1

                return grau

        raise VerticeInvalidoError

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for a1 in self.arestas:
            for a2 in self.arestas:

                if (str(self.arestas[a1].v1) == str(self.arestas[a2].v1)
                    and str(self.arestas[a1].v2) == str(self.arestas[a2].v2)) \
                        and self.arestas[a1] != self.arestas[a2]:
                    return True

                if str(self.arestas[a1].v1) == str(self.arestas[a2].v2) \
                        and str(self.arestas[a1].v2) == str(self.arestas[a2].v1) \
                        and self.arestas[a1] != self.arestas[a2]:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
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
