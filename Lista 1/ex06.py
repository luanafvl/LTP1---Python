print("Bem-vindo(a) à Biblioteca Digital!")

livros = []
autores = []
ano = []
cont = 0

while True:

    print("Serviços:")

    opt = int(input("\n(1) - Adicionar um livro\n(2) - Lista de livros disponíveis\n(3) - Buscar livro pelo título\n(4) - Sair\n"))

    if opt == 1:
        print("Adicionando livro na estante...")
        livros.append(input("Título:\n"))
        autores.append(input("Autor:\n"))
        ano.append(int(input("Ano de publicação:\n")))
    elif opt == 2:
        if len(livros) == 0:
            print("Nenhum livro na estante.")
        else:
            for i in range(0, len(livros)):
                print(f"{i+1} - {livros[i]}")
    elif opt == 3:
        if len(livros) == 0:
            print("Nenhum livro na estante.")
        else:
            optLivro = input("Livro:\n")
            if optLivro in livros:
                print(f"'{optLivro}' está disponível na estante!")
            else:
                print(f"'{optLivro}' não está disponível na estante!")
    else:
        break

    cont += 1

print("Volte logo!")
