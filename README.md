# desafio-selecao

Desafio em Python

Faça um algoritmo que utilize o menu abaixo:

## MENU
1. Ler arquivo de jogadores
2. Escalar time
3. Realizar Substituição
4. Expulsão
5. Imprimir escalação

Escolha:

### Opção 1:
Ler de um arquivo texto todos os jogadores escalados para a copa e armazenar em uma lista (`lst_jogadores`). Cada elemento da lista será uma instância da classe `Jogador`.

### Opção 2:
Você deverá escalar 11 jogadores para iniciar a partida. Os jogadores escalados ficam em uma lista (`lst_escalados`) e o atributo `participou_partida` é alterado para `True`. Os jogadores que não forem escalados ficam em outra lista (`lst_reserva`).

### Opção 3:
Realizar a substituição de um jogador por outro. O jogador substituído vai para a lista de reserva e o outro para a lista de escalados.

### Opção 4:
Caso haja alguma expulsão, o jogador sai da lista de escalados e vai para a lista de reserva.

### Opção 5:
Mostrar a escalação de todos os jogadores que participaram do jogo, incluindo as substituições e expulsões. Os dados devem ser salvos em um arquivo (`todosjogadores.txt`).

```python
class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao  # GOLEIRO, DEFESA, MEIO-CAMPO ou ATACANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False  # ou True
        
      
## Aquirvo txt.
1:Alisson:GOLEIRO
2:Danilo:DEFESA
3:Thiago Silva:DEFESA
4:Marquinhos:DEFESA
5:Casemiro:MEIO-CAMPO
6:Alex Sandro:DEFESA
7:Lucas Paquetá:MEIO-CAMPO
8:Fred:MEIO-CAMPO
9:Richarlison:ATACANTE
10:Neymar:ATACANTE
11:Raphinha:ATACANTE
12:Weverton:GOLEIRO
13:Dani Alves:DEFESA
14:Éder Millitão:DEFESA
15:Fabinho:MEIO-CAMPO
16:Alex Telle:DEFESA
17:Bruno Guimarães:MEIO-CAMPO
18:Gabriel Jesus:ATACANTE
19:Antony:ATACANTE
20:Vinicius Junior:ATACANTE
21:Rodrygo:ATACANTE
22:Éverton Ribeiro:MEIO-CAMPO
23:Ederson:GOLEIRO
24:Bremer:DEFESA
25:Pedro:ATACANTE
26:Gabriel Martinelli:ATACANTE
