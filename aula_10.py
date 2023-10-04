#1

def soma(n):
    soma = 0 
    for i in range(1,n):
        soma += i 
        print(soma)

soma(5)


#####################################
def contar(palavra, letra):
    c = 0
    for i in palavra:
        if i == letra:
            c += 1
            print("Existir a numero", i, c)
contar("casola", "a")




#####################################

def calcula(n):
    if n < 0:
        return 'Negativo'
    elif n == 0 or n ==1:

        return 1
    else:
        resultado = 1
        for i in range(2, n +1):
            resultado *= i
            return resultado

numero = int(input('digite um numero'))
resultado = calcula(numero)
print(f'Fatorial{numero} é {resultado}')

###############################
dicionario = {}
dicionario['chave1'] = 'palavra1'
dicionario['chave2'] = 'palavra2'
dicionario['chave3'] = 'palavra3'
print(dicionario)

#################
produtos = {}
for i in range(3):
    nome_do_produto = input("Digite o produto: ")
    preco_produto = float(input(f"Digite o preço:"))
    produtos[nome_do_produto] = preco_produto

    print('lista de produtos: ')
    for produto, preco in produtos.items():
        print(f'Produto: {produto}: preço R$ {preco:} ')
