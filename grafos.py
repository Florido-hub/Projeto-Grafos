def criar_grafo():
  grafo = []

  qtdVertices = int(input("Digite a quantidade de vértices do grafo: "))
  while qtdVertices < 0:
    qtdVertices = int(input("Numero inválido, digite outro: "))    

  for i in range(0, qtdVertices, 1):
      grafo.append([])

  return grafo

def ler_grafo(grafo):
  for i in range(len(grafo)):
      a = input(f"Digite as arestas que ligam no vértice {i}: ")
      lista = a.split()

      for j in range(len(lista)):
        aresta = int(lista[j])
        while aresta < 0 or aresta >= len(grafo):
          aresta = int(input(f"Aresta {aresta} é inválida para o vértice {i}. Digite uma aresta válida: "))
        grafo[i].append(aresta)

def imprimir_grafo(grafo):
  for i in range(0, len(grafo), 1):
      print(f"Arestas do vértice {i}: ", end=' ')
      for j in range(0, len(grafo[i]), 1):
          print(grafo[i][j], end=' ')
      print()


grafo = criar_grafo()
ler_grafo(grafo)
imprimir_grafo(grafo)