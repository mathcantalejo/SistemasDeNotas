#variável para armazenar as notas dos alunos ímpares e pares
nota_total_impar = 0.0
nota_total_par = 0.0
print("Esse programa serve para anotar as notas dos alunos!")
#loop para repetir por 25 vezes (1,3,5,7...49) a solicitação da nota ímpar
for numero_impar in range(1,50,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    #para cada volta do loop, solicitar a nota do aluno x
    nota_impar = float(input("Digite a nota do aluno {}: ".format(numero_impar)))
    #para cada nota colocada, somar a nota total impar
    nota_total_impar = nota_total_impar + nota_impar
#loop para repetir por 25 vezes (2,4,6,8...50) a solicitação da nota par
for numero_par in range(2,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    #para cada volta do loop, solicitar a nota do aluno x
    nota_par = float(input("Digite a nota do aluno {}: ".format(numero_par)))
    #para cada nota colocada, somar a nota total par
    nota_total_par = nota_total_par + nota_par
media_par = nota_total_par/25
media_impar = nota_total_impar/25
if media_par>media_impar:
    print("Os números pares ficaram com a maior média de nota, exatamente {}, ganhando da média ímpar que ficou com apenas {}".format(media_par, media_impar))
else:
    print("Os números ímpares ficaram com a maior média de nota, exatamente {}, ganhando da média par que ficou com apenas {}".format(media_impar, media_par))


