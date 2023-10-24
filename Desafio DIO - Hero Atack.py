class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "discurso no jutso"
        print(f"Com os seus {self.idade} anos de experiência, o {self.tipo}, conhecido como {self.nome}, atacou usando {ataque}. Obliterando assim, o seu adversário")

quantidade_herois = int(input("Digite a quantidade de heróis: "))

for i in range(quantidade_herois):
    nome = input("Digite o nome do herói: ")
    idade = int(input("Digite a idade do herói: "))
    tipo = input("Digite o tipo do herói: ")

    heroi = Heroi(nome, idade, tipo)
    heroi.atacar()