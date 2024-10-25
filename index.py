# ##################################################################################################################################

# ### Questão 1 ###
# ##
# ##Python é uma linguagem de programação de alto nível, interpretada, orientada a objetos, de tipagem dinâmica e forte. 
# # O que cada uma dessas características significa?

# ## De alto nível:
# #  quer dizer que ela é uma linguagem muito próxima a linguagem humana, abstraindo boa parte da linguagem 
# # tecnica da máquina, tornando sua sintaxe mais fácil e produtiva.

# ## Interpretada:
# # Refere-se ao fato dela não necessitar de um compilador para rodar, fazendo com que seu desenvolvimento seja mais rápido,
# #  entretanto a sua execução acaba perdendo no desempenho

# ## Orientada a objetos:
# #Permite a utilização da orientação a objetos(POO), tornando o código modular e de fácil reutilização.

# #Tipagem dinâmica e forte:
# # Python é uma linguagem de tipagem forte, o que significa que as operações entre diferentes tipos de dados são restritas.
# #  Por exemplo, não é possível somar uma string com um número diretamente, a menos que você faça uma conversão explícita.
# #sendo também uma tipagem dinamica que quer dizer que o próprio python tem a capacidade de dizer qual tipo de dado sem a 
# # necessidade do programador informar o tipo.

# ##################################################################################################################################

# ### Questão 2 ###
# ##
# ## Fale sobre as funções input(), print() e o método format(). Além disso, dê exemplo dos principais tipos primitivos de dados em Python

# ##Função Input():
# #A função input() é usada para receber entrada do usuário via teclado
# #Ela exibe uma mensagem (prompt) para o usuário e aguarda que o usuário digite algo.
# #O valor digitado é tratado como uma string (texto) e pode ser atribuído a uma variável.

# ##Função Print():
# #A função print() é usada para exibir informações na tela.
# #Ela aceita um ou mais argumentos (separados por vírgula) e os imprime.

# ##Metodo format():
# #O método format() é usado para formatar strings, substituindo marcadores de posição por valores específicos.
# #Ele permite criar strings dinâmicas com base em variáveis.

# ##################################################################################################################################

# ### Questão 3 ###
# ##
# ## Elabore um programa que lê o nome e a nota de um aluno, depois exibe esses dados, mas com a nota formatada para
# #  exibir apenas uma casa decimal.

# nome = str(input("informe seu nome"))
# nota = float(input("informe sua nota"))

# print(f'A nota do Aluno: {nome} é: {nota:.1f}')


# ##################################################################################################################################

# ### Questão 4 ###
# ##
# ##Quais são os operadores matemáticos usados em Python? Dê exemplos

# #Os operadores matemáticos em python são:

# ##Adição(+):
# a = 5
# b = 5
# print(f'soma: {a+b}')
# #Saída esperada: soma: 10

# ##$Subtração(-):a
# a = 5
# b = 5
# print(f'Subtração {a-b}')
# #Saída esperada: Subtração 0

# ##Multiplicação (*)
# a = 5
# b = 5
# print(f'Multiplicação {a*b}')
# #Saída Multiplicação 25

# ##Divisão (/):
# a = 5
# b = 5
# print(f'Divisão {a/b}')
# #Saída esperada: Divisão 1.0

# ##Módulo (%):
# a = 5
# b = 5
# print(f'Módulo {a%b}')
# #Saída esperada: Módulo 0

# ##Exponenciação (**): 
# a = 5
# b = 5
# print(f'Exponenciação {a**b}')
# #Saída esperada: Exponenciação 3125

# ##Divisão inteira (//):
# a = 5
# b = 5
# print(f'Divisão inteira {a//b}')
# #Saída esperada: Divisão inteira 1

# ##################################################################################################################################

# ### Questão 5 ###
# ##
# ##Dê um exemplo de uso da estrutura condicional aninhada (if, elif e else). 

# Coca_cola = float(input("Digite o valor da Coca-cola na sua cidade"))
# Pepsi = float(input("Digite o valor da Pepsi na sua cidade"))

# if Coca_cola > Pepsi:
#     print("Coca-cola está mais caro")
# elif Coca_cola == Pepsi:
#     print('Estão no mesmo preço')
# else:
#     print("Pepsi está mais caro")

# ##################################################################################################################################

# ### Questão 6 ###
# ##
# #Quais são os operadores comparativos usados em Python? Dê exemplos.

# ##Igual (==):
# a = 5
# b = 5
# resultado = a == b
# # O resultado será True

# ##Diferente (!=):
# x = 10
# y = 7
# resultado = x != y
# # O resultado será True

# ##Maior que (>):
# p = 15
# q = 10
# resultado = p > q
# # O resultado será True

# ##Menor que (<):
# num1 = 5
# num2 = 8
# resultado = num1 < num2
# # O resultado será True

# ##Maior ou igual a (>=):
# a = 12
# b = 12
# resultado = a >= b
# # O resultado será True

# ##Menor ou igual a (<=):
# x = 7
# y = 9
# resultado = x <= y
# # O resultado será True

# ##################################################################################################################################

# ### Questão 7 ###
# ## Quatro times estão disputando as semifinais de um campeonato de futebol. Leia os gols que cada time marcou em suas partidas
# #  e informe qual time saiu vencedor. Em caso de empate em uma das partidas, leia o número de pênaltis cobrados corretamente 
# # (valores entre 0 e 5) para cada time. Supondo que haverá dois times vencedores das partidas, exiba-os. Exemplo de mensagem final:
# #  “Os times A e B estão na grande final!”.
# time1 = input("Informe o time 1")
# gols_time1 = int(input(f'Informe os gols do {time1}'))

# time2 = input("Informe o time 2")
# gols_tome2 = int(input(f'Informe os gols do {time2}'))

# time3 = input("Informe o time 3")
# gols_time3 = int(input(f'Informe os gols do {time3}'))

# time4 = input("Informe o time 4")
# gols_time4 = int(input(f'Informe os gols do {time4}'))

# if gols_time1 == gols_tome2:
#     penalt_time1 = int(input(f'Informe os gols de penalti do {time1}'))
#     penalt_time2 = int(input(f'Informe os gols de penalti do {time2}'))
#     if penalt_time1 > penalt_time2:
#         final1 = time1
#     else:
#         final1 = time2
# elif gols_time1 > gols_tome2:
#     final1 = time1
# else: final1 = time2

# if gols_time3 == gols_time4:
#     penalt_time3  = int(input(f'Informe os gols de penalti do {time3}'))
#     penalt_time4  = int(input(f'Informe os gols de penaltido {time4}'))
#     if penalt_time3 > penalt_time4:
#         final2 = time3
#     else:
#         final2 = time4
# elif gols_time3 > gols_time4:
#     final1 = time3
# else: final1 = time4

# print(f'A grande final será entre: {final1} e {final2}')


##################################################################################################################################

### Questão 8 ###
##
#Faça um programa que leia três números e, em seguida, exiba-os em ordem crescente.

# num1 = int(input("Digite o primeiro numero"))
# num2 = int(input("Digite o segundo numero"))
# num3 = int(input("Digite o terceiro numero"))
# numeros = [num1, num2, num3]
# apoio = numeros

# print(f'numeros antes da execução: \n{numeros}')

# tamanho = len(numeros)
# for _ in range(tamanho):
#     verify = False
#     for i in range(tamanho-1):
#         if numeros[i] > numeros[i+1]:
#             temp = 0
#             temp = numeros[i]
#             numeros[i] = numeros[i+1]
#             numeros[i+1] = temp
#             verify = True
#     if not verify:
#         break
# print(f'numeros após a execução: \n{numeros}')


##################################################################################################################################

### Questão 9 ###
##
#Elabore um programa que leia o salário mensal de uma pessoa, realize o cálculo do imposto de renda e, por fim, informe
#  se a pessoa deve declarar ou não o imposto de renda. Assuma que será obrigada a apresentar a declaração anual a pessoa 
# que receber rendimentos tributáveis, sujeitos ao ajuste na declaração, cuja soma foi superior a R$ 28.559,70.
#

# Pessoa = "Allysson"
# salario = float(input("informe seu salario mensal"))
# salarioAnual = 0
# count = 0
# somaoBase = 28559.70
# while count < 12:
#     count += 1
#     salarioAnual += salario
# if salarioAnual >= somaoBase:
#     print("Deve declarar o impostp")
# else:
#     print("Não precisa declarar")


##################################################################################################################################

### Questão 10 ###
##
#Faça um programa que calcule a conta de energia elétrica, solicitando apenas o número de kW/h e levando em consideração:
# a)     O preço do kW/h é R$ 0,56.
# b)     O valor da Geração de energia é 41% do valor do consumo.
# c)     O valor de imposto é de 22,52% do valor do consumo.
# d)     Qual a “bandeira” (acréscimo a cada kWh consumido) tarifária está em vigor: 
# I.         Amarela: R$ 0,015.
# II.        Bandeira vermelha - Patamar 1: R$ 0,040. 
# III.       Bandeira vermelha - Patamar 2: R$ 0,060.
# Informe o valor final da conta de Energia

# continuar = True

# while continuar:
#     try:
#         kwUsados = float(input("informe a quantidade de Kw/h usados no mês: "))
#         print('( 1 ) - Bandeira Amarela. \n( 2 ) - Bandeira VermelhaP1\n( 3 ) - Bandeira VermelhaP2')
#         bandeira = int(input(f'Escolha a bandeira: '))
#         valorkw = 0.56
#         consumo = kwUsados * 0.56
#         imposto = consumo * 0.2252
#         geracaoEnergia = consumo * 0.41

#         if bandeira == 1:
#             valorComBandeira = consumo + (0.015 * kwUsados)
#         elif bandeira == 2:
#             valorComBandeira = consumo + (0.040 * kwUsados)
#         elif bandeira == 3:
#             valorComBandeira = consumo + (0.060 * kwUsados)
#         else:
#             print("Por favor, escolha uma opção válida")
#             continue

#         valorAposGeracao = valorComBandeira - geracaoEnergia
#         valorFinal = valorAposGeracao + imposto

#         print(f'O valor final de sua conta é: R$ {valorFinal:.2f}')
#     except ValueError:
#         print("Por favor, insira um válor válido.")
#         continue

#     repetir = input("Fim do programa. Deseja executar novamente? Sim (S) | Não (N):").upper()
#     if repetir == "N": 
#         continuar = False
#     elif repetir != "S":
#         print('Opção inválida. Digite "S" para Sim e "N" para não.')
       






