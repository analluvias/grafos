from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        # set não tem item repetido
        verticesNaoAdjacentes = set()

        # percorrendo todas as linhas
        for i in range(len(self.vertices)):

            # percorrendo a parte superior da lista
            for j in range(i + 1, len(self.vertices)):

                # pegando o rotulo da aresta
                rotulo = f'{self.vertices[i]}-{self.vertices[j]}'

                # se naquela casinha não tiver nenhum objeto
                if len(self.arestas[i][j]) == 0:

                    # aqueles vertices do rótulo não são adjacentes
                    verticesNaoAdjacentes.add(rotulo)

        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        # for na qtd de vertices
        for i in range(len(self.vertices)):

            # acessando a lista de dicionários de arestas em
            # cada celula da diagonal principal
            if len(self.arestas[i][i]) > 0:
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        v = self.get_vertice(V)
        linha_do_vertice = self.indice_do_vertice(v) # linha do vertice
        grau = 0

        for celula_parte_superior in range(linha_do_vertice, len(self.vertices)):

            # se ele tiver um laço, contamos o dicionario 2 vezes
            if celula_parte_superior == linha_do_vertice:
                grau += 2 * len(self.arestas[linha_do_vertice][celula_parte_superior])
            # se estiver fora da diag principal, contamos cada dicionário
            # da lista uma vez
            else:
                grau += len(self.arestas[linha_do_vertice][celula_parte_superior])

        # contando os dicionários nas coluna do vertice (que tem o msm indice da linha)
        # ainda na parte superior do grafo
        for i in range(linha_do_vertice):
            grau += len(self.arestas[i][linha_do_vertice])

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        # percorrendo a linha de vertices
        for i in range(len(self.vertices)):
            # percorrendo acima da diagonal principal
            for j in range(i, len(self.vertices)):
                #
                if len(self.arestas[i][j]) > 1:
                    return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas_sobre_vertice = set()
        indice_vertice = self.indice_do_vertice(self.get_vertice(V))

        # percorrendo coluna b
        for linha in range(0, self.indice_do_vertice(self.get_vertice(V)) + 1):
            dicionario_arestas = self.arestas[linha][indice_vertice]

            for aresta in dicionario_arestas:
                arestas_sobre_vertice.add(aresta)

        # percorrendo linha b
        for coluna in range(indice_vertice + 1, len(self.vertices)):
            dicionario_arestas = self.arestas[indice_vertice][coluna]

            for aresta in dicionario_arestas:
                arestas_sobre_vertice.add(aresta)

        return arestas_sobre_vertice

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        # verifica se o grafo nao tem paralelas
        if self.ha_paralelas() is True:
            return False

        if self.ha_laco() is True:
            return False

        if self.vertices_nao_adjacentes() != set():
            return False

        return True
