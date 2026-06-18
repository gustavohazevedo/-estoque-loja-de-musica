###Estoque de loja de Musica em geral
import sys

Produtos =  [
[1, "Encordoamento de Aço Giannini Cobra",15,"prateleira 01"],
[2, "Encordoamento Nylon Daddario",15, "prateleira 01"],
[3, "Kits C/ 50 Palhetas P/ Violão e Guitarra", 25, "prateleira 02"],
[4, "Afinador Digital Eletrico Violão",50, "prateleira 02"],
[5, "Capotraste Guitarra E Violão",30, "prateleira 02" ]
 ]

# print(Produtos)

def cadastrarProduto():
    print("cadastro de produtos")


def  ListarProdutos():
     print(f"{Produtos}\n")


##Ajuda do Gersão
def  buscarProdutos ():
    IDProcurado = int(input("Qual o ID do produto: "))
    produtoEncontrado = -1
    for linha in Produtos:
        if IDProcurado == linha[0]:
            print(f"Produto encontrado com sucesso! {linha}")
            produtoEncontrado = 1
            break

    if produtoEncontrado == -1:
        print("Esse produto não existe! Digite um ID existente.")


def  atualizarProdutos ():
    IDProcurado = int(input("Qual o ID do produto que você deseja alterar a quantidade: "))
    linha_produto = -1
    for i in range(len(Produtos)):
        if IDProcurado == Produtos[i][0]:
            linha_produto = i
    if linha_produto == -1:
        print("Produto não encontrado! Tente novamente.")
    else:
        Alteracao_qte = int(input("Qual a nova quantidade?: "))
        Produtos[linha_produto][2] = Alteracao_qte
        print("Quantidade atualizada!")
        ListarProdutos()

def sair():
    sys.exit(0)




print("\nBem vindo a loja de Instrumentos Musicais, escolha sua opção:")
print("1-Insira um novo Produto: |2-Listar Todos os Produtos: |3-Buscar Produto por ID: |4-Atualizar Estoque: |5- Sair do Programa.")
opcao = input("escolher opção:")
if opcao == "1":
     cadastrarProduto()
elif opcao == "2":
    ListarProdutos()
elif opcao == "3":
     buscarProdutos()
elif opcao == "4":
     atualizarProdutos()
elif opcao == "5":
    print("Saindo do sistema")
    sair()
    




