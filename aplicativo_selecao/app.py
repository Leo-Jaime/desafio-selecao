

class Jogador:
    def __init__(self, nome, numero, posicao):
        self.numero = numero
        self.nome = nome
        self.posicao = posicao
        self.situacao = "Normal"  #ou "Expulso"
        self.participou_partida = False # ou True

    def __str__(self):
        return f"jogador {self.nome} numero {self.numero} posicao {self.posicao}"

jogadores = []
def ler_arquivo():
    with open ('convocaçao.txt','r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            numero, nome, posicao = linha.strip().split(':')
            jogador = Jogador(nome,numero,posicao)
            jogadores.append(jogador)
            print(f"Nome: {jogador.nome} " f"Camisa: {jogador.numero} " f" Posicao: {jogador.numero}")
            print("▬"*60)
    return jogadores
           

#Tem que escalar 11 jogadores para iniciar uma paDrtida, sao 26 jogadores
jogadores_escalados = []
reserva = []
def escalar_jogador(jogadores):
    for jogador in jogadores:

        if len(jogadores_escalados)< 11:
            escolha = input(f'Deseja escalar o jogador {jogador.nome} (s/n)?')

            if escolha == 's':
                jogador.participou_partida = True
                jogadores_escalados.append(jogador)
                print(f"Jogador Escalado")
            else:
                reserva.append(jogador)
                print(f"jogador na reserva")
                
        else:
            reserva.append(jogador)
            print(f"jogador na reserva")

    for jogador in jogadores_escalados: #for para testar se meu algoritmo esta funcionando corretamente
        print(f'jogador escalado {jogador.nome} numero {jogador.numero}')
        
    for jogador in reserva:
        print(f'jogador reserva {jogador.nome} numero {jogador.numero}')
    
    return jogadores_escalados, reserva

def substituir_jogador(jogadores_escalado, reservas):
    jogador_sair = input("Escolha o jogador quer vai ser substituido: ")
    jogador_entrar = input("Escolha o jogador quer vai entrar: ")
    
    for jogador in jogadores_escalados:
        if jogador.numero == jogador_sair:
            print(f'jogador que vai sair {jogador.nome}')
            jogadores_escalados.remove(jogador)
            jogador_fora = jogador.nome
            return jogador_fora
    for jogador in reserva: #jogador que vai entrar no lugar
        if jogador.numero == jogador_entrar:
            jogador.participou_partida = True
            print(f'jogador que vai entrar {jogador.nome}')
            jogadores_escalados.append(jogador)
            jogador_dentro = jogador.nome
            return jogador_dentro
    return subistituicao.append(f'jogador {jogador_fora} expulso, Entrou {jogador_dentro} ')   
subistituicao = []
def expulsar_jogador(jogadores_escalado, reservas):
    global subistituicao 
    jogador_expulso = input("Escolha o jogador quer vai ser expulso: ")
    jogador_entrar = input("Escolha o jogador quer vai entrar: ")

    for jogador in jogadores_escalados:
        if jogador.numero == jogador_expulso:
            print(f'jogador expulso {jogador.nome}')
            jogadores_escalados.remove(jogador)
            jogador_fora = jogador.nome
            return jogador_fora
    for jogador in reserva: #jogador que vai entrar no lugar
        if jogador.numero == jogador_entrar:
            jogador.participou_partida = True
            print(f'jogador que vai entrar {jogador.nome}')
            jogadores_escalados.append(jogador)
            jogador_dentro = jogador.nome
            return jogador_dentro
    return subistituicao.append(f'jogador {jogador_fora} expulso, Entrou {jogador_dentro} ')
def imprimir_escalacao():
    for jogador in jogadores_escalados:
        print(f"Nome: {jogador.nome} " f"Camisa: {jogador.numero} " f" Posicao: {jogador.numero}")
        print('#'*60)
    


def menu():

    print("""    
            MENU
============================
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha:""")
    while True:
        escolha = int(input("Escolha uma opcao:"))

        if escolha == 1:
            ler_arquivo()
            print("Arquivo carregado!!!")

        elif escolha == 2:
            escalar_jogador(jogadores)
        elif escolha == 3:
            substituir_jogador(jogadores_escalados, reserva)
        elif escolha == 4:
            expulsar_jogador(jogadores_escalados, reserva)
        elif escolha == 5:
            imprimir_escalacao()
            print(subistituicao)
        else:
            break


menu()    




