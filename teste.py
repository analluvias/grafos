from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

# Grafo da Paraíba
grafo_pb = GrafoListaAdjacencia()
grafo_pb.adiciona_vertice("J")
grafo_pb.adiciona_vertice("C")
grafo_pb.adiciona_vertice("E")
grafo_pb.adiciona_vertice("P")
grafo_pb.adiciona_vertice("M")
grafo_pb.adiciona_vertice("T")
grafo_pb.adiciona_vertice("Z")
grafo_pb.adiciona_aresta('a1', 'J', 'C')
grafo_pb.adiciona_aresta('a2', 'C', 'E')
grafo_pb.adiciona_aresta('a3', 'C', 'E')
grafo_pb.adiciona_aresta('a4', 'P', 'C')
grafo_pb.adiciona_aresta('a5', 'P', 'C')
grafo_pb.adiciona_aresta('a6', 'T', 'C')
grafo_pb.adiciona_aresta('a8', 'M', 'T')
grafo_pb.adiciona_aresta('a9', 'T', 'Z')
grafo_pb.adiciona_aresta('a7', 'M', 'C')

print(grafo_pb)