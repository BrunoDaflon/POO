from abc import ABC, abstractmethod

class Objeto:
    def __init__(self, tipo):
        self.__tipo = tipo

    def definir_tipo_objeto(self, novo_tipo):
        self.__tipo = novo_tipo

    def get_tipo(self):
        return self.__tipo


class Personagem(ABC):
    def __init__(self, tipo, vida, objeto=None):
        self._tipo = tipo
        self.vida = vida
        self.objeto = objeto

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def conversar(self, personagem):
        pass

    @abstractmethod
    def defesa(self, atacante):
        pass

    @abstractmethod
    def ataque(self, alvo):
        pass

    @abstractmethod
    def pegar(self, novo_objeto):
        pass


class Personagem_NPC(Personagem):
    def apresentacao(self):
        print(f"Personagem NPC {self._tipo} não sou jogável.")

    def conversar(self, personagem):
        print(f"Personagem NPC {personagem._tipo}, eu sou um NPC.")

    def defesa(self, atacante):
        print(f"NPC defende ataque de {atacante._tipo}")
        return 10

    def ataque(self, alvo):
        print(f"NPC atacou {alvo._tipo}, muito fraco.")
        return 15

    def pegar(self, novo_objeto):
        print(f"NPC pegou {novo_objeto.get_tipo()}, mas não tem habilidade.")
        self.objeto = novo_objeto


class Personagem_RPG(Personagem):
    def __init__(self, nome, tipo, vida, objeto=None):
        super().__init__(tipo, vida, objeto)
        self.nome = nome
        self._afinidades = {
            "Mago": ["Elfo", "Arqueiro", "Anão"],
            "Arqueiro": ["Mago", "Elfo", "Bardo"],
            "Anão": ["Mago", "Anão"],
            "Bardo": ["Mago", "Arqueiro", "Anão", "Elfo"],
            "Elfo": ["Mago", "Arqueiro", "Bardo"],
        }

    def definir_tipo(self, novo_tipo):
        self._tipo = novo_tipo

    def apresentacao(self):
        print(f"{self.nome} do tipo {self._tipo} diz: Salve, sou um personagem jogável!!!!")

    def conversar(self, personagem):
        if personagem._tipo in self._afinidades.get(self._tipo, []):
            print(f"{self.nome} diz: {personagem._tipo}, bora explorar umas dungeons!!!")
        else:
            print(f"{self.nome} diz: {personagem._tipo}, não gosto de você!!!")

    def defesa(self, atacante):
        if atacante._tipo in self._afinidades.get(self._tipo, []):
            print(f"{self.nome} tem defesa boa de {atacante._tipo}")
            return 20
        else:
            print(f"{self.nome} se defendeu normal de {atacante._tipo}")
            return 15

    def ataque(self, alvo):
        if alvo._tipo in self._afinidades.get(self._tipo, []):
            print(f"{self.nome} atacou o {alvo._tipo} com uma força reduzida")
            return 25
        else:
            print(f"{self.nome} atacou {alvo._tipo} com todas as forças!")
            return 50

    def pegar(self, novo_objeto):
        print(f"{self.nome} pegou {novo_objeto.get_tipo()} para equipar no inventário!")
        self.objeto = novo_objeto


class Ambiente:
    def __init__(self, nome):
        self.nome = nome
        self.participantes = []

    def apresentar_participantes(self):
        print(f"Participantes do lobby {self.nome}:")
        for p in self.participantes:
            if isinstance(p, Personagem_NPC):
                print(f"{p._tipo} - VIDA: {p.vida}")
            else:
                print(f"{p.nome} ({p._tipo} - VIDA: {p.vida})")

    def adicionar_personagens(self, *personagens):
        for p in personagens:
            self.participantes.append(p)
            if isinstance(p, Personagem_NPC):
                print(f"NPC tipo: {p._tipo} está no lobby")
            else:
                print(f"{p.nome} está no lobby")


def jogando():
    print("...RPG DO BRUNÃO...")
    print()

    cajado = Objeto("Cajado")
    escudo = Objeto("Escudo")

    heroi = Personagem_RPG("Herói", "Mago", 100, cajado)
    vilao = Personagem_RPG("Vilão", "Elfo", 100, escudo)
    npc = Personagem_NPC("Normal", 50)

    dungeon = Ambiente("CAVE DA MORGANA")
    dungeon.adicionar_personagens(heroi, vilao, npc)

    print("\nApresentando:\n")
    heroi.apresentacao()
    vilao.apresentacao()
    npc.apresentacao()

    print("\nConversando:\n")
    heroi.conversar(vilao)
    vilao.conversar(heroi)
    npc.conversar(heroi)

    print("\nCombatendo:\n")
    ataque_heroi = heroi.ataque(vilao)
    defesa_vilao = vilao.defesa(heroi)
    vilao.vida -= max(0, ataque_heroi - defesa_vilao)

    ataque_vilao = vilao.ataque(heroi)
    defesa_heroi = heroi.defesa(vilao)
    heroi.vida -= max(0, ataque_vilao - defesa_heroi)

    ataque_npc = npc.ataque(heroi)
    defesa_heroi = heroi.defesa(npc)
    heroi.vida -= max(0, ataque_npc - defesa_heroi)

    print("\nEstado final:\n")
    dungeon.apresentar_participantes()


# Executar o jogo
jogando()
