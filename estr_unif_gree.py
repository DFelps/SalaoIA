from matplotlib.pyplot import title
from pyvis.network import Network
import networkx as nx

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai = pai
        self.estado = estado
        self.valor1 = valor1        # valor do nó na árvore
        self.valor2 = valor2        # custo do caminho até o nó atual
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):

        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s, v1, v2, p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None:
                    break

            if atual == self.head:
                self.inserePrimeiro(s, v1, v2, p)
            else:
                if atual is None:
                    self.insereUltimo(s, v1, v2, p)
                else:
                    novo_no = No(p, s, v1, v2, None, None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual

    # REMOVE NO INÍCIO DA LISTA

    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            str.append(aux.estado)
            aux = aux.proximo

        return str

    def exibeArvore(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

    def exibeArvore1(self, s):

        atual = self.head
        while atual.estado != s:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

    def exibeArvore2(self, s, v1):

        atual = self.tail

        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior

        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

    def primeiro(self):
        return self.head

    def ultimo(self):
        return self.tail


class busca(object):

    def custo_uniforme(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado, atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]  # custo do caminho
                v1 = v2  # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"

    def greedy(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []
        2
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado, atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                j = nos.index(novo)

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]  # custo do caminho
                v1 = h[j]  # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"

    def a_estrela(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado, atual.valor1)
                return caminho, atual.valor1

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                j = nos.index(novo)

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]  # custo do caminho
                v1 = h[j] + v2  # f1(n) + f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"


nos = ["Falkreath",
       "Markarth",
       "Riften",
       "Solitude",
       "Whiterun",
       "Dragon Bridge",
       "Kartvasten",
       "Rockstead",
       "Riverwood",
       "Helgen",
       "Ivarsted",
       "Shorstone"]

grafo = [
    [["Falkreath", 46], ["Helgen", 38], ["Riverwood", 15]],
    [["Markarth", 136], ["Kartvasten", 87], ["Rockstead", 41]],
    [["Riften", 132], ["Shorstone", 94], ["Ivarsted", 67]],
    [["Solitude", 166], ["Dragon Bridge", 120], ["Kartvasten", 87]],
    [["Whiterun", 0], ["Riverwood", 15], ["Ivarsted", 67], ["Rockstead", 41]],
    [["Dragon Bridge", 120], ["Solitude", 166], ["Kartvasten", 87]],
    [["Kartvasten", 87], ["Markarth", 136], ["Dragon Bridge", 120], ["Rockstead", 41]],
    [["Rockstead", 41], ["Whiterun", 0], ["Kartvasten", 87], ["Dragon Bridge", 120]],
    [["Riverwood", 15], ["Whiterun", 0], ["Helgen", 38], ["Falkreath", 46]],
    [["Helgen", 38], ["Falkreath", 46], ["Riverwood", 15]],
    [["Ivarsted", 67], ["Riften", 132], ["Shorstone", 94], ["Whiterun", 0]],
    [["Shorstone", 94], ["Riften", 132], ["Ivarsted", 67], ["Whiterun", 0]]
]

# HEURISTICA SERVE SOMENTE PARA DESTINO WHITERUN
h = [166, 0, 140, 242, 111, 78, 70, 151, 226, 244, 241, 234,]



g = Network('100%', '100%',  bgcolor='#222222', font_color='#FFFFFF')
g.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], value=[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
            title=['Falkreath nv.2', 'Markarth nv.2', 'Riften nv.2', 'Solitude nv.4', 'Whiterun nv.0', 'Dragon Bridge nv.3',
                   'Kartvasten nv.2', 'Rockstead nv.1', 'Riverwood nv.1', 'Helgen nv.2', 'Ivarsted nv.1', 'Shorstone nv.2'],
            label=nos,
            color=['blue', 'blue', 'blue', 'blue', 'red', 'blue',
                   'blue', 'blue', 'blue', 'blue', 'blue', 'blue'],
            )
g.add_edges([(5, 9), (5, 8), (5, 11), (9, 5), (9, 10), (1, 10),(1, 8),(2, 7),(2, 8),(3, 12),(3, 11),(4, 6),(6, 4),(6, 7),(7, 2),(7, 6),(8, 7),(8, 5),(10, 9),(10, 1),(11, 5),(11, 12),(12, 3),(12, 11)])



g.show('nx.html')

sol = busca()
caminho = []

caminho, custo = sol.custo_uniforme("Riften", "Whiterun") #Destino, Origem
print("Custo Uniforme: ", caminho[: : -1], "\ncusto do caminho: ", custo)

f = open('script/uniforme.txt', 'a')
f.truncate(0)
f = open('script/uniforme.txt', 'a')
f.write(str(caminho))
f.close()

caminho, custo = sol.greedy("Riften", "Whiterun") #Destino, Origem
print("\nGreedy: ", caminho[: : -1], "\ncusto do caminho: ", custo)

f = open('script/greed.txt', 'a')
f.truncate(0)
f = open('script/greed.txt', 'a')
f.write(str(caminho))
f.close()

caminho, custo = sol.a_estrela("Riften", "Whiterun") #Destino, Origem
print("\nA estrela: ", caminho[: : -1], "\ncusto do caminho: ", custo)

f = open('script/estrela.txt', 'a')
f.truncate(0)
f = open('script/estrela.txt', 'a')
f.write(str(caminho))
f.close()

