from collections import deque

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
                    index = int(palavras.pop(0))
                    cadeia_funcoes[index] = palavras

    def ler_arquivo_linha(self, linha: int):
        pass


class MP:
    estado: int
    func: str
    char: chr
    prox_estado: int
    final: bool
    fila: deque
    accept: bool

    def __str__(self) -> str:
        return '''Estado: {}
Função: {}
Caractere: {}
Próximo estado: {}'''.format(self.estado, self.func, self.char, self.prox_estado)

    def __init__(self, estado: int, fila: deque, func: str = "", char: chr = ""):
        self.estado = estado
        self.func = func
        self.char = char
        # self.prox_estado = estado + 1
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
        self.prox_estado = self.estado + 1

    def __jump(self, param):
        # caça no arquivo até encontrar instrução do estado
        # caso nao encontre, verificar novamente o mesmo estado até acabar ou gerar erro
        if self.char == param[0]:
            self.prox_estado = int(param[1])
        else:
            self.prox_estado = int(param[1]) + 1
        self.char = ""

    def __adiciona(self, param):
        self.fila.append(param)
        self.prox_estado = self.estado + 1

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
# 0 estado de aceitação
# -1 estao de rejeição


# Não é meu
# push S (add S na fila)
# jr S (encerra programa e rejeita se o símbolo lido da ponta de saída é S)
# ja S (encerra programa e aceita se o símbolo lido da ponta de saída é S)
# jmp E, S (desvia fluxo de execução caso a )
# read (lê símbolo da ponta de saída e armazena numa variável temporária pra fazer todos os testes desses S)
if __name__ == '__main__':
    cadeia = "ab"
    a = Arquivo("teste.txt")
    a.ler_arquivo()
    print(cadeia_funcoes)
    q = deque()
    q.append("a")
    q.append("b")
    #
    mp = MP(1, q)
    # print(cadeia_funcoes.get(1)[0])
    mp.func = cadeia_funcoes.get(1)[0]
    mp.funcao(cadeia_funcoes.get(1)[1:])
    while not mp.final:
        mp.estado = mp.prox_estado
        mp.func = cadeia_funcoes.get(mp.estado)[0]
        mp.funcao(cadeia_funcoes.get(mp.estado)[1:])

# print(q)
# mp.func = "read"
# mp.funcao()
# mp.func = "jump a 2"
# if mp.char == mp.func.split(" ")[1]:
#     mp.prox_estado = mp.func.split(" ")[2]
#     print(mp.prox_estado)
#     mp.func = mp.func.split(" ")[0]
#     mp.funcao("a")

# ; programa que reconhece cadeias vazias ou com número par de 1's
# 11: push #
# 12: read
# 13: jr 0
# 15: ja #
# 16: jmp 17, 1
# 17: read
# 18: jr 0
# 20: jr #
# 21: jmp 12, 1


# escreve #
# le
# se for b rejeita
# se for # aceita
# se for a le de novo
# se for a fica lendo e pondo no final
# se for b fica lendo b ate nao poder mais e pondo no final
# se for # le e poe no final
# volta pro inicio
