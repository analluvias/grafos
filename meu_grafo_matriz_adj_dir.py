from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from math import inf


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

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        v = self.get_vertice(V)
        indiceVertice = self.indice_do_vertice(v)
        arestas = list()

        for j in range(len(self.arestas)):
            for aresta in self.arestas[indiceVertice][j]:
                arestas.append(self.arestas[indiceVertice][j][aresta])
        for j in range(len(self.arestas)):
            for aresta in self.arestas[j][indiceVertice]:
                arestas.append(self.arestas[j][indiceVertice][aresta])
        return arestas

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
                        if m1_simplificada[coluna][colunas_do_indice_que_tem_1] >= m1_simplificada[linha] \
                                [colunas_do_indice_que_tem_1]:
                            pass
                        else:
                            m1_simplificada[coluna][colunas_do_indice_que_tem_1] = m1_simplificada[linha] \
                                [colunas_do_indice_que_tem_1]
        return m1_simplificada

    def dijkstra(self, inicial, final):

        # armazena a distancia estimada do vertice inicial até o vertice v
        beta = {}

        # indica se o vertice já foi visitado - 0 nao 1 sim
        phi = {}

        # armazena o predecessor de v até o momento
        pi = {}

        # vertice inicial
        w = inicial

        # percorrendo todos os vertices e configurando
        # os valores iniciais padrões
        for n in self.vertices:
            v = str(n)
            beta[v] = inf
            phi[v] = 0
            pi[v] = 0

        beta[inicial] = 0
        phi[inicial] = 1
        w = inicial

        # laço infinito
        while True:
            # verificando qual aresta incide sobre o vertice inicial atual
            sobre = self.arestas_sobre_vertice(w)
            # so saimos do laco quando chegarmos a w
            if w == final:
                break

            # para cada vertice que incide
            for x in sobre:
                # se o inicial atual for igual ao v1 da aresta, pegar o v2
                if w == x.v1.rotulo:
                    contrario = x.v2.rotulo
                # se o inicial for igual ao v2, pegar o v1
                else:
                    contrario = x.v1.rotulo
                # se a distancia do outro vertic for maior que a distancia do
                # inicial atual mais o peso desse vertice
                # e nao tivermos passado por essa aresta
                if beta[contrario] > beta[w] + x.peso and phi[contrario] == 0:
                    # entao esse vertice recebe a distancia do inicial mais o peso
                    beta[contrario] = beta[w] + x.peso
                    # e seu predecessor é o inicial atual
                    pi[contrario] = w

            # o menor caminho vai ser igual a infinito
            menor = inf

            # rodando o dicionário beta que contem a distancia entre os adj ao inicial atual
            for i in beta:
                # se aquele caminho for menor que o menor e nao
                # tivermos passado por ele
                if beta[i] < menor and phi[i] == 0:
                    # encontramos um caminho mais curto para esse vértice do
                    # que os encontrados anteriormente.
                    menor = beta[i]
            # w inicial vai ser obtido do dicionario com os valores de beta
            # receberá o nome de beta, mas buscaremos pelo indice do menor
            w = list(beta.keys())[list(beta.values()).index(menor)]
            # vamos marcar o phi do novo inicial com 1
            phi[w] = 1

        # r recebe o vertice final
        r = final
        caminho = []
        while True:
            caminho.append(r)
            # quebramos ao chegar no inicial
            if r == inicial:
                return caminho
            # predecessor do final atual
            r = pi[r]

    def recalcula_distancias(self, contrario_old, beta, pai_anterior, passei_por_aqui, conta_recursoes):

        conta_recursoes += 1

        sobre = self.arestas_sobre_vertice(contrario_old)

        if len(sobre) == 0 or beta[contrario_old] == inf or conta_recursoes == len(self.vertices) - 1:
            return

        # para cada vertice que incide
        for x in sobre:
            # se o inicial atual for igual ao v1 da aresta, pegar o v2
            # if contrario_old == x.v1.rotulo:
            contrario_new = x.v2.rotulo
            # se o inicial for igual ao v2, pegar o v1
            # else:
            #     contrario_new = x.v1.rotulo

            if beta[contrario_new] != inf and contrario_new != pai_anterior and beta[contrario_new] > \
                    beta[contrario_old] + x.peso and beta[contrario_new] in passei_por_aqui:
                beta[contrario_new] = beta[contrario_old] + x.peso
                self.recalcula_distancias(contrario_new, beta, contrario_old, passei_por_aqui, conta_recursoes)
            else:
                return

    @staticmethod
    def obtem_caminho_vertice(pi, vertice_calculado, inicial):

        caminho = []
        while True:
            caminho.append(str(vertice_calculado))
            # quebramos ao chegar no inicial
            if str(vertice_calculado) == inicial:
                return caminho
            # predecessor do final atual
            vertice_calculado = pi[str(vertice_calculado)]

    def bellman_ford(self, inicial):
        # armazena os filhos de todos os vertices
        filhos = {}

        # armazena a distancia estimada do vertice inicial até o vertice v
        beta_atualizado = {}

        # armazena o estado dos betas da iteração anterior
        beta_anterior = {}

        # armazena o predecessor de v até o momento
        pi = {}

        # armazeno os vertices já passados
        passei_por_aqui = []

        # percorrendo todos os vertices e configurando
        # os valores iniciais padrões
        for n in self.vertices:
            v = str(n)
            beta_atualizado[v] = inf
            beta_anterior[v] = inf
            pi[v] = 0
            filhos[v] = self.arestas_sobre_vertice(v)

        # mudando distancia do beta inicial
        beta_atualizado[inicial] = 0
        # vertices que eu verificarei os filhos nessa iteração
        # começo pelo inicial
        proximo_vertice_a_verificar_filhos = [inicial]

        conta_iteracoes = 0

        vertice_anterior = inicial

        # percorrer n-1 vezes
        while True:

            # print(len(self.vertices) - 1)
            aux = []

            for proximo in proximo_vertice_a_verificar_filhos:
                # aux = []
                print("proximo: ", proximo)
                sobre = self.arestas_sobre_vertice(proximo)
                # para cada vertice que incide
                for x in sobre:

                    print("vertices de sobre: ", str(x))

                    # se o inicial atual for igual ao v1 da aresta, pegar o v2
                    if proximo == x.v1.rotulo:
                        contrario = x.v2.rotulo
                        contrario_eh_pai = False
                        contrario_eh_filho = True
                    # se o inicial for igual ao v2, pegar o v1
                    else:
                        contrario = x.v1.rotulo
                        contrario_eh_pai = True
                        contrario_eh_filho = False

                    if beta_atualizado[contrario] > beta_atualizado[proximo] + x.peso:
                        if contrario_eh_filho:
                            passei_por_aqui.append(contrario)
                            print("beta contrario_eh_filho:", beta_atualizado)
                            print("passei por aqui: ", passei_por_aqui)
                            print("\n contrario contrario_eh_filho: " + contrario + " ", beta_atualizado[proximo] + x.peso, " ", proximo)
                            # entao o vertice filho recebe a distancia do inicial atual mais o peso
                            beta_atualizado[contrario] = beta_atualizado[proximo] + x.peso
                            # e seu predecessor é o inicial atual
                            pi[contrario] = proximo

                            self.recalcula_distancias(contrario, beta_atualizado, proximo, passei_por_aqui, conta_recursoes=0)

                        if contrario_eh_pai and beta_atualizado[contrario] != inf:
                            passei_por_aqui.append(contrario)
                            print("beta contrario_eh_pai:", beta_atualizado)
                            print("passei por aqui: ", passei_por_aqui)
                            print("\n contrario contrario_eh_pai: " + contrario + " ", beta_atualizado[proximo] + x.peso, " ", proximo)
                            # entao o vertice filho recebe a distancia do inicial atual mais o peso
                            beta_atualizado[proximo] = beta_atualizado[contrario] + x.peso
                            # e seu predecessor é o inicial atual
                            pi[proximo] = contrario

                            self.recalcula_distancias(proximo, beta_atualizado, contrario, passei_por_aqui,
                                                      conta_recursoes=0)

                        if contrario != vertice_anterior:
                            aux.append(contrario)

                if conta_iteracoes != 0:
                    vertice_anterior = proximo

                proximo_vertice_a_verificar_filhos = list(set(aux))
                print(proximo_vertice_a_verificar_filhos)

            conta_iteracoes += 1

            if conta_iteracoes == len(self.vertices) - 1:
                print('numero de vezes')
                break
            elif beta_anterior == beta_atualizado:
                print('beta anterior = beta atualizado')
                print(beta_anterior)
                print(beta_atualizado)
                break
            else:
                pass
                beta_anterior = beta_atualizado

            # proximo_vertice_a_verificar_filhos = aux
            # print(proximo_vertice_a_verificar_filhos)

        print("\n", pi)
        print(beta_atualizado)

        caminhos = {}
        # for vertice in self.vertices:
        #     caminhos[str(vertice)] = self.obtem_caminho_vertice(pi, vertice, inicial)

        return caminhos
