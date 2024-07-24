from bibgrafo.grafo_exceptions import VerticeInvalidoException
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
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        nome_arestas_sobre_vertice = set()

        count = 0
        for vert in self.vertices:
            if str(vert) == str(V):
                count += 1

        if count == 0:
            raise VerticeInvalidoException

        for a in self.arestas:
            if str(self.arestas[a].v1) == str(V) or str(self.arestas[a].v2) == str(V) \
                    and str(self.arestas[a].rotulo) not in nome_arestas_sobre_vertice:
                nome_arestas_sobre_vertice.add(str(self.arestas[a].rotulo))

        return nome_arestas_sobre_vertice

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

    def arestas_incidentes(self, vertice_inicial):

        lista_arestas = list()

        for a in self.arestas:

            if str(self.arestas[a].v1) == str(vertice_inicial) or str(self.arestas[a].v2) == str(vertice_inicial):
                lista_arestas.append(f'{str(self.arestas[a].rotulo)}')

        return lista_arestas

    def tam_arestas(self):

        count = 0
        for aresta in self.arestas:
            count += 1
        return count

    def qtd_vetices(self):

        count = 0
        for vertice in self.vertices:
            count += 1
        return count

    def dfs_aux(self, vertice_inicial, arvore):

        if self.tam_arestas() == arvore.tam_arestas():
            return arvore

        a_incidentes = self.arestas_incidentes(vertice_inicial)
        arestas_incidentes = list(a_incidentes)

        lista_passar = list()

        for a_incidente in arestas_incidentes:

            # se nao existe aquela aresta na arvore, nao mapeei ela
            if not arvore.existe_rotulo_aresta(a_incidente):

                passar = ''
                # se o vertice inicial for v1, entao vamos analisar v2
                if str(vertice_inicial) == str(self.arestas[a_incidente].v1):
                    passar = self.arestas[a_incidente].v2.rotulo
                    lista_passar.append(passar)

                # se o vertice inicial for v2, entao vamos analisar v1
                if str(vertice_inicial) == str(self.arestas[a_incidente].v2):
                    passar = self.arestas[a_incidente].v1.rotulo
                    lista_passar.append(passar)

                if not arvore.existe_rotulo_vertice(passar):
                    arvore.adiciona_vertice(passar)
                    arvore.adiciona_aresta(self.arestas[a_incidente])

                    for ai in list(self.arestas_incidentes(passar)):
                        if not arvore.existe_rotulo_aresta(ai):
                            self.dfs_aux(passar, arvore)

        # print("arvore:")
        # for a in arvore.arestas:
        # print(arvore.arestas[a].v1, arvore.arestas[a].v2)
        # print(arvore.arestas[a].rotulo)
        # print("\n\n\n")

        return arvore

    def dfs(self):

        arvore = MeuGrafo()
        arvore.adiciona_vertice(str(self.vertices[0]))

        # print(self.vertices[0])

        return self.dfs_aux(self.vertices[0], arvore)

    def bfs_aux(self, vertice_inicial, arvore):

        if self.tam_arestas() == arvore.tam_arestas():
            return arvore

        a_incidentes = self.arestas_incidentes(vertice_inicial)
        arestas_incidentes = list(a_incidentes)

        lista_passar = list()

        for a_incidente in arestas_incidentes:

            # se nao existe aquela aresta na arvore, nao mapeei ela
            if not arvore.existe_rotulo_aresta(a_incidente):

                passar = ''
                # se o vertice inicial for v1, entao vamos analisar v2
                if str(vertice_inicial) == str(self.arestas[a_incidente].v1):
                    passar = self.arestas[a_incidente].v2.rotulo
                    lista_passar.append(passar)

                # se o vertice inicial for v2, entao vamos analisar v1
                if str(vertice_inicial) == str(self.arestas[a_incidente].v2):
                    passar = self.arestas[a_incidente].v1.rotulo
                    lista_passar.append(passar)

                if not arvore.existe_rotulo_vertice(passar):
                    arvore.adiciona_vertice(passar)
                    arvore.adiciona_aresta(self.arestas[a_incidente])

                    for ai in list(self.arestas_incidentes(passar)):
                        if not arvore.existe_rotulo_aresta(ai):
                            self.bfs_aux(passar, arvore)

        print("arvore:")
        for a in arvore.arestas:
            print(arvore.arestas[a].v1, arvore.arestas[a].v2)
            print(arvore.arestas[a].rotulo)
        print("\n\n\n")

        return arvore

    def bfs(self):
        arvore = MeuGrafo()
        arvore.adiciona_vertice(str(self.vertices[0]))

        return self.bfs_aux(self.vertices[0], arvore)

    def caminho(self, v1, v2, indice_v1):

        a2 = MeuGrafo()
        a2.adiciona_vertice(str(self.vertices[0]))

        # faço o dfs e nele encontro o grafo sem arestas de retorno
        arvore = self.dfs()
        caminho = list()
        lista = []

        caminho.append(str(v1))
        result = self.caminho_aux(v1, a2, arvore, caminho, v1, v2, lista)

        # print(result)

        def juntar_letras_vizinhas(lista):
            nova_lista = []
            i = 0
            while i < len(lista):
                nova_lista.append(lista[i])
                if i < len(lista) - 1 and lista[i].isupper() and lista[i] == lista[i + 1]:
                    i += 1  # Pular a próxima letra, pois será adicionada na próxima iteração
                i += 1
            return nova_lista

        lista_resultante = juntar_letras_vizinhas(result)

        # print(lista_resultante)

        def contar_ocorrencias(lista):
            ocorrencias = {}
            for elemento in lista:
                if elemento in ocorrencias:
                    ocorrencias[elemento] += 1
                else:
                    ocorrencias[elemento] = 1
            return ocorrencias

        def selecionar_lista_entre_letras(lista):
            indice_v1_mais_proximo = None
            indice_v2 = None

            for i in range(len(lista) - 1, -1, -1):
                if lista[i] == str(v2):
                    indice_v2 = i
                elif lista[i] == str(v1):
                    if indice_v1_mais_proximo is None or (
                            indice_v2 is not None and abs(i - indice_v2) < abs(indice_v1_mais_proximo - indice_v2)):
                        indice_v1_mais_proximo = i

            if indice_v1_mais_proximo is None or indice_v2 is None:
                return []

            indice_v1 = min(indice_v1_mais_proximo, indice_v2)

            return lista[indice_v1:indice_v2 + 1]

        parte_v1_v2 = selecionar_lista_entre_letras(lista_resultante)
        # print("parte v1 e v2", parte_v1_v2)

        ocorrencias = contar_ocorrencias(parte_v1_v2)

        # print(ocorrencias)

        def remove_duplicadas_no_meio(lista):

            letras_selecionadas = {chave: valor for chave, valor in ocorrencias.items() if valor >= 2}
            chaves_lista = list(letras_selecionadas)
            lista_dict = []
            tem_letra_repetida = False
            for letra in chaves_lista:

                tem_letra_repetida = True
                if letra != str(v1) and letra != str(v2):
                    abriu = 0
                    fechou = 0
                    dicionario = {}
                    for i in range(0, len(lista)):
                        if lista[i] == letra and abriu == 0:
                            abriu = 1
                            dicionario['letra'] = lista[i]
                            dicionario['abriu'] = i
                            # print("abriu", i)
                            continue
                        if lista[i] == letra and abriu == 1 and fechou == 0:
                            fechou = 1
                            dicionario['fechou'] = i
                            # print("fechou", i)
                    lista_dict.append(dicionario)
            retornar = []
            if tem_letra_repetida:

                for dct in lista_dict:
                    for i in range(0, len(lista)):

                        if dct['abriu'] < i - (dct['fechou'] - dct['abriu']):
                            retornar.append(lista[i])

                        if dct['fechou'] > i + (dct['abriu']):
                            retornar.append(lista[i])
            else:
                retornar = lista

            return retornar

        final = remove_duplicadas_no_meio(parte_v1_v2)
        # print(final)

        return final

    def caminho_aux(self, v_inicial, a_caminho, arvore, caminho, v1, v2, lista):

        rotulos = arvore.arestas_sobre_vertice(v_inicial)
        arestas_incidentes = list(rotulos)

        for aresta in list(arvore.arestas_incidentes(v_inicial)):

            # se nao existe aquela aresta na arvore, nao mapeei ela
            if not a_caminho.existe_rotulo_aresta(aresta):

                if str(v_inicial) == str(arvore.arestas[aresta].v1.rotulo):
                    passar = arvore.arestas[aresta].v2.rotulo

                else:
                    passar = arvore.arestas[aresta].v1.rotulo

                if aresta in list(arvore.arestas_incidentes(v_inicial)):
                    # caminho.append(str(aresta))
                    # print("aresta", aresta)
                    caminho.append(str(v_inicial))

                a_caminho.adiciona_vertice(passar)
                a_caminho.adiciona_aresta(self.arestas[aresta])
                caminho.append(str(aresta))
                caminho.append(str(passar))

                if caminho[-1]:

                    if arvore.grau(passar) > 1:
                        lista.append(aresta)
                        self.caminho_aux(passar, a_caminho, arvore, caminho, v1, v2, lista)
                else:
                    lista.append(aresta)
                    return caminho

        return caminho

    def conexo(self):

        qtd_vertices_iniciais = len(self.vertices)

        # chamando o dfs_conexo e guardando em uma arvore dfs
        arvore_dfs = self.dfs()

        # verificando se a arvore possui a mesma qtd de vertices que o grafo inicial
        if len(arvore_dfs.vertices) == qtd_vertices_iniciais:
            return True
        else:
            return False
