# Nikollas Ferreira Gonçalves - 0040890

from collections import deque
import sys

cadeia_funcoes = dict()


class Arquivo:
    arquivo: str

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def ler_arquivo(self):
        with open(self.arquivo) as f:
            for line in f:
                if not line.rstrip() == "":
                    palavras = line.rstrip().split(" ")
                    palavras_sem_comentario = []
                    for p in palavras:
                        if not p.__contains__(";"):
                            palavras_sem_comentario.append(p)
                        else:
                            break
                    if palavras_sem_comentario:
                        index = int(palavras_sem_comentario.pop(0))
                        cadeia_funcoes[index] = palavras_sem_comentario


class MP:
    estado: int
    func: str
    char: chr
    final: bool
    fila: deque
    accept: bool

    def __str__(self) -> str:
        return '''Estado: {}
Função: {}
Caractere: {}'''.format(self.estado, self.func, self.char)

    def __init__(self, estado: int, fila: deque, func: str = "", char: chr = ""):
        self.estado = estado
        self.func = func
        self.char = char
        self.fila = fila
        self.final = False

    def funcao(self, param):
        if self.func == "read":
            return self.__ler()
        if self.func == "jump":
            return self.__jump(param)
        if self.func == "add":
            return self.__adiciona(param[0])
        if self.func == "rej":
            return self.__rejeita()
        if self.func == "acc":
            return self.__aceita()

    def __ler(self):
        self.char = self.fila.popleft()
        self.estado += 1

    def __jump(self, param):
        # caça no arquivo até encontrar instrução do estado
        # caso nao encontre, verificar novamente o mesmo estado até acabar ou gerar erro
        if self.char == param[0]:
            self.estado = int(param[1])
            self.char = ""
        else:
            self.estado += 1

    def __adiciona(self, param):
        self.fila.append(param)
        self.estado += 1

    def __rejeita(self):
        print("Cadeia rejeitada")
        self.final = True
        self.accept = False

    def __aceita(self):
        print("Cadeia aceita")
        self.final = True
        self.accept = True


# meu
# add (adiciona na fila)
# jump (desvia fluxo)
# read (le)
# acc (aceita)
# rej (rejeita)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cadeia = sys.argv[1]
        a = Arquivo(sys.argv[2])
    else:
        cadeia = input("Digite a cadeia sem espaços:\n")
        a = Arquivo(input("Digite o nome do arquivo com extensão:\n"))
    a.ler_arquivo()
    print(cadeia_funcoes)
    q = deque()
    for c in cadeia:
        q.append(c)
    mp = MP(1, q)
    while not mp.final:
        mp.func = cadeia_funcoes.get(mp.estado)[0]
        mp.funcao(cadeia_funcoes.get(mp.estado)[1:])

# escreve #
# le
# se for b rejeita
# se for # aceita
# se for a le de novo
# se for a fica lendo e pondo no final
# se for b fica lendo b ate nao poder mais e pondo no final
# se for # le e poe no final
# volta pro inicio
