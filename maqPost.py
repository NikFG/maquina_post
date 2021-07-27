from collections import deque


class MP:
    estado: int
    func: str
    char: chr
    prox_estado: int
    final: bool
    fila: deque

    def __str__(self) -> str:
        return '''Estado: {}
Função: {}
Caractere: {}
Próximo estado: {}
final: {}'''.format(self.estado, self.func, self.char, self.prox_estado, self.final, self.fila)

    def __init__(self, estado: int, func: str, char: chr, prox_estado: int, fila, final: bool = False):
        self.estado = estado
        self.func = func
        self.char = char
        self.prox_estado = prox_estado
        self.final = final
        self.fila = fila

    def funcao(self, param: str = ""):
        if self.func == "read":
            return self.__ler()
        if self.func == "jump":
            return self.__jump(param)
        if self.func == "add":
            return self.__adiciona(param)
        if self.func == "rej":
            return self.__rejeita(param)
        if self.func == "acc":
            return self.__aceita(param)

    def __ler(self):
        self.char = self.fila.popleft()

    def __jump(self, param):
        # caça no arquivo até encontrar instrução do estado
        # caso nao encontre, verificar novamente o mesmo estado até acabar ou gerar erro
        print("jumpou")

    def __adiciona(self, param):
        self.fila.append(param)

    def __rejeita(self, param):
        print("rejeitou")

    def __aceita(self, param):
        print("aceitou")


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
    q = deque()
    q.append("a")
    q.append("b")

    mp = MP(1, "add", "", 2, q)
    mp.funcao("#")
    print(q)
    mp.func = "read"
    mp.funcao()
    mp.func = "jump a 2"
    if mp.char == mp.func.split(" ")[1]:
        mp.prox_estado = mp.func.split(" ")[2]
        print(mp.prox_estado)
        mp.func = mp.func.split(" ")[0]
        mp.funcao("a")

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
