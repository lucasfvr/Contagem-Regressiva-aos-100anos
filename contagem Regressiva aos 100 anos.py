# Exibe para o usuario o titulo do programa.
print('Bem vindo à Contagem Regressiva aos 100 anos.') #Titulo do programa.

#Foi importada a função 'sleep' da biblioteca 'time'.
from time import sleep 

# Pausa de 1 segundo antes de mostrar as proximas mensagens. Isso dá tempo para o usuário ler a mensagem antes que a próxima seja exibida.
# A função 'sleep' é usada para adicionar uma pausa na execução do programa.
sleep(1) 
print ('Esse programa foi desenvolvido para descobrir quantos anos faltam para você completar 100 anos.') 
sleep(1)
print ('Para começarmos, preciso que responda algumas perguntas.')
sleep(1)
 # Inicia um loop para permitir a reinicialização do programa.

# Recebe o nome do usuário e valida se o nome é composto apenas por letras.
nome = input ('Qual é o seu nome? ')
while not all (part.isalpha() for part in nome.split()):
        print('Por favor, digite um nome válido (somente letras).')
        nome = input ('Qual é o seu nome? ')
        
# Divide o nome completo em partes e extrai apenas o primeiro nome.
nome_partes = nome .split()
primeiro_nome = nome_partes[0]

# Recebe a idade do usuário e valida se a idade é composto apenas por numeros e se esta no intervalo correto.
idade = input('Agora informe sua idade: ')
while not idade.isdigit() or not (1 <= int(idade)<= 99):
    if not idade.isdigit():
        print('Por favor, digite uma idade válida (somente números). ')
    else:
        print('A idade deve estar entre 1 e 99 anos.')
    idade = input ('Agora informe sua idade: ')

idade = int(idade)

print('Muito obrigado pelas informações.')
sleep(1)       
print ('Agora vamos fazer os cálculos.')
sleep(0.5)

# Calcula quantos anos faltam para o usuário completar 100 anos.
resultado = 100 - idade

# Exibe o resultado do cálculo, mencionando o primeiro nome do usuário.
print(f'Tudo pronto.\n{primeiro_nome}, faltam {resultado} anos para você completar 100 anos.')
sleep(0.8)

# Agradece ao usuário pela utilização do programa e solicita feedback.
print('Espero que tenha gostado da sua experiência em nosso aplicativo.')
sleep(0.2)
avaliacao = input ('De 0 a 5, qual nota você dá para nosso programa? ')
while not avaliacao.isdigit() or not (0 <= int(avaliacao)<= 5):
    if not avaliacao.isdigit():
        print('Digite um número válido.')
    else:
        print('Sua avaliação deve estar entre 0 e 5.')
    avaliacao = input ('De 0 a 5, qual nota você dá para nosso programa? ')
sleep(0.2)
print('Muito obrigado pela sua avaliação')

# Linha final para encerrar o programa e fornecer informações adicionais
sleep(0.1)
print('Direitos Reservados a Lucas Fernandes®.')
sleep(0.1)
print('Trabalho acadêmico desenvolvido por um aluno do curso de Sistemas de Informação, primeiro período, UniFOA.')
