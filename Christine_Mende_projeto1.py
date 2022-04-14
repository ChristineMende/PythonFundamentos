#Projeto de Christine Mende 30/01/2022

import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

#Uma função que retorna uma lista contendo todas as categorias dos diferentes produtos:
def listar_categorias(dados):
    lista_categorias=[]  
    for elemento in dados:    
      nova_categoria = elemento['categoria']   
      if nova_categoria not in lista_categorias: 
        lista_categorias.append(nova_categoria)
    return lista_categorias
  
#Uma função que retorna uma lista contendo todos os produtos pertencentes à categoria dada:
def listar_por_categoria(dados, categoria):
  lista_items=[]  
  for elemento in dados: 
    if elemento['categoria'] == categoria: 
      lista_items.append({"id": elemento['id'],
    "preco": elemento['preco'],
    "categoria": elemento['categoria']})
  return lista_items  

#Uma função que retorna um dicionário representando o produto mais caro da categoria dada:
def produto_mais_caro(dados, categoria):
  lista_produtos=[]
  lista_precos=[]
  produto_mais_caro = {}  
  maior_preco = 0
  for elemento in dados: 
    if elemento['categoria'] == categoria: 
      if float(elemento ['preco']) >= maior_preco:
        maior_preco = float(elemento['preco'])
  for produto in dados:
    if produto['categoria'] == categoria and float(produto['preco']) == maior_preco: 
      produto_mais_caro = {"id": produto['id'],
    "preco": produto['preco'],
    "categoria": produto['categoria']}
  return produto_mais_caro

#Uma função que retorna um dicionário representando o produto mais barato da categoria dada:
def produto_mais_barato(dados, categoria):
  lista_produtos=[]
  lista_precos=[]
  produto_mais_barato = {}  
  for elemento in dados: 
    if elemento['categoria'] == categoria: 
      lista_precos.append(float(elemento['preco'])) 

  menor_preco = min(lista_precos)
  for produto in dados:
    if produto['categoria'] == categoria and float(produto['preco']) == menor_preco: 
        produto_mais_barato = {"id": produto['id'],
    "preco": produto['preco'],
    "categoria": produto['categoria']}
  return produto_mais_barato

#Uma função que retorna uma lista de dicionários representando os 10 produtos mais caros:
def top_10_caros(dados):
  lista_precos = []
  top_10_caros = []
  for item in dados:
    lista_precos.append(float(item['preco']))

  lista_precos.sort()
  lista_precos.reverse()
  
  for produto in dados:
    if float(produto['preco']) in lista_precos[0:10]:
      top_10_caros.append({"id": produto['id'],
    "preco": produto['preco'],
    "categoria": produto['categoria']})
      
  return top_10_caros


#Uma função que retorna uma lista de dicionários representando os 10 produtos mais baratos:
def top_10_baratos(dados):
  lista_precos = []
  top_10_baratos = []
  for item in dados:
    lista_precos.append(float(item['preco']))

  lista_precos.sort()

  for produto in dados:
    if float(produto['preco']) in lista_precos[0:10]:
      top_10_baratos.append({"id": produto['id'],
    "preco": produto['preco'],
    "categoria": produto['categoria']})
      
  return top_10_baratos

#Uma função que exibe as seguintes opções, em Loop: 
    #1. Listar categorias
    #2. Listar produtos de uma categoria
    #3. Produto mais caro por categoria
    #4. Produto mais barato por categoria
    #5. Top 10 produtos mais caros
    #6. Top 10 produtos mais baratos
    #0. Sair

def menu(dados):
  var_ejecutar = True    
  while (var_ejecutar):
    opcao = input("Selecione uma das seguintes opções: \n1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair\n")
  
    if opcao == '1':
      listar_categorias(dados)
      print(f"A lista de categorias é:\n {listar_categorias(dados)}\n")

    elif opcao == '2':
      categoria = input("Digite a categoria a consultar: ")
      listar_por_categoria(dados, categoria)
      print(f"A lista de produtos pertencentes à categoria {categoria} é:\n {listar_por_categoria(dados, categoria)}\n")

    
    elif opcao == '3':
      categoria = input("Digite a categoria a consultar: ")
      produto_mais_caro(dados, categoria)
      print(f"O produto mais caro da categoria {categoria} é:\n {produto_mais_caro(dados, categoria)}.\n")


    elif opcao == '4':
      categoria = input("Digite a categoria a consultar: ")
      produto_mais_barato(dados, categoria)
      print(f"O produto mais barato da categoria {categoria} é:\n {produto_mais_barato(dados, categoria)}. \n")

    
    elif opcao == '5':
      top_10_caros(dados)
      print(f"Os 10 produtos mais caros são: \n{top_10_caros(dados)}.\n") 


    elif opcao == '6':
      top_10_baratos(dados)
      print(f"Os 10 produtos mais baratos são: \n{top_10_baratos(dados)}.\n") 

    
    elif opcao == '0':
      var_ejecutar = False
      print("Você escolheu a opção SAIR.")

    else:
      print("Opção inválida.")


# Programa Principal - não modificar!
d = obter_dados()
menu(d)
