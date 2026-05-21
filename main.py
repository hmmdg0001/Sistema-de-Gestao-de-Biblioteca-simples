from datetime import datetime # Fornece funcionalidades relacionadas a datas e horas
import json # Módulo para trabalhar com arquivos JSON
import os # Módulo para interagir com o sistema operacional

BIBLIOTECA_FILE = "biblioteca.json" # Expecifica o nome do arquivo JSON onde a biblioteca será armazenada

def carregar_biblioteca():   # Carrega a biblioteca a partir do arquivo JSON
    if os.path.exists(BIBLIOTECA_FILE):
        try: # Tenta carregar a biblioteca do arquivo JSON
            with open(BIBLIOTECA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return [] # Retorna uma lista vazia se o arquivo não existir ou ocorrer um erro ao carregar


def salvar_biblioteca(biblioteca): # Salva a biblioteca no arquivo JSON
    try: # Tenta salvar a biblioteca no arquivo JSON
        with open(BIBLIOTECA_FILE, "w", encoding="utf-8") as f:
            json.dump(biblioteca, f, ensure_ascii=False, indent=2)
    except IOError as e: # Captura erros de entrada/saída
        print(f"\nErro ao salvar biblioteca: {e}") # Função já feita


def listar_livros(biblioteca): # Procura todos os livros na biblioteca
    if not biblioteca: # Verifica se a biblioteca está vazia
        print("\nNenhum livro registado.")
        return 
    
    print("\n--- Todos os Livros ---")
    for livro in biblioteca: # Procura todos os livros na biblioteca
        status = "Disponível" if livro.get("disponivel") else "Emprestado"
        print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | "
              f"Género: {livro['genero']} | Ano: {livro['ano_publicacao']} | Status: {status}")


def remover_livro(biblioteca, livro_id): # Remove um livro da biblioteca pelo ID
    for i, livro in enumerate(biblioteca): # Procura todos os livros na biblioteca
        if livro["id"] == livro_id: # Verifica se o livro com o ID fornecido existe
            titulo = livro["titulo"] 
            biblioteca.pop(i) 
            salvar_biblioteca(biblioteca)
            print(f"\nLivro '{titulo}' removido com sucesso.")
            return # Sai da função após remover o livro
    print(f"\nErro: Livro com ID {livro_id} não encontrado.") # Mensagem de erro se o livro não for encontrado

def emprestar_livro(biblioteca, livro_id): # Função para emprestar um livro
    for livro in biblioteca: # Procura todos os livros na biblioteca
        if livro["id"] == livro_id: # Verifica se o livro com o ID fornecido existe
            if livro["disponivel"]: # Verifica se o livro está disponível para empréstimo
                livro["disponivel"] = False
                livro["data_emprestimo"] = datetime.now().strftime("%Y-%m-%d") # Registra a data do empréstimo
                salvar_biblioteca(biblioteca)
                print(f"\nLivro '{livro['titulo']}' emprestado com sucesso.")
                return # Sai da função após emprestar o livro
            else:
                print(f"\nErro: Livro '{livro['titulo']}' já está emprestado.") # Mensagem de erro se o livro não estiver disponível
                return 
    print(f"\nErro: Livro com ID {livro_id} não encontrado.") 

def devolver_livro(biblioteca, livro_id): # Função para devolver um livro
    for livro in biblioteca: # Procura todos os livros na biblioteca
        if livro["id"] == livro_id: # Verifica se o livro com o ID fornecido existe
            if not livro["disponivel"]: # Verifica se o livro está emprestado
                livro["disponivel"] = True # Marca o livro como disponível
                livro["data_emprestimo"] = None # Remove a data de empréstimo
                salvar_biblioteca(biblioteca)
                print(f"\nLivro '{livro['titulo']}' devolvido com sucesso.")
                return
            else: # Se o livro não estiver emprestado
                print(f"\nErro: Livro '{livro['titulo']}' não está emprestado.")
                return 
        print(f"\nErro: Livro com ID {livro_id} não encontrado.")
    
    
def pesquisar_titulo(biblioteca, titulo): # Função para pesquisar livros por título
        resultados = [livro for livro in biblioteca if titulo.lower() in livro["titulo"].lower()] # Pesquisa o título ignorando maiúsculas e minúsculas
        if resultados: # Verifica se encontrou algum livro com o título fornecido
            print(f"\n--- Resultados da Pesquisa para '{titulo}' ---")
            for livro in resultados:  # Procura todos os livros na biblioteca
                status = "Disponível" if livro.get("disponivel") else "Emprestado" # Verifica o status do livro
                print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | "
                      f"Género: {livro['genero']} | Ano: {livro['ano_publicacao']} | Status: {status}")
        else: # Se não encontrou nenhum livro com o título fornecido
            print(f"\nNenhum livro encontrado com o título '{titulo}'.")

def listar_livros_disponiveis(biblioteca): # Função para listar livros disponíveis
    disponiveis = [livro for livro in biblioteca if livro.get("disponivel")] # Filtra os livros disponíveis
    if disponiveis: # Verifica se há livros disponíveis
        print("\n--- Livros Disponíveis ---")
        for livro in disponiveis: # Procura todos os livros na biblioteca
            print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | "
                  f"Género: {livro['genero']} | Ano: {livro['ano_publicacao']}")
    else: # Se não houver livros disponíveis
        print("\nNenhum livro disponível no momento.")

def estatisticas_genero(biblioteca): # Função para estatísticas por gênero
    genero_count = {} # Dicionário para contar o número de livros por gênero
    for livro in biblioteca: # Procura todos os livros na biblioteca 
        genero = livro.get("genero", "Desconhecido") # Obtém o gênero do livro, ou "Desconhecido" se não estiver definido
        genero_count[genero] = genero_count.get(genero, 0) + 1 # Incrementa a contagem para o gênero

    print("\n--- Estatísticas por Género ---")
    for genero, count in genero_count.items(): # Itera sobre os gêneros e suas contagens
        print(f"Género: {genero} | Número de Livros: {count}")

def taxa_emprestimo(biblioteca): # Função para calcular a taxa de empréstimo
    total_livros = len(biblioteca) # Total de livros na biblioteca
    if total_livros == 0: # Verifica se há livros na biblioteca
        print("\nNenhum livro registado na biblioteca.")
        return

    livros_emprestados = sum(1 for livro in biblioteca if not livro.get("disponivel")) # Conta o número de livros emprestados
    taxa = (livros_emprestados / total_livros) * 100 # Calcula a taxa de empréstimo em percentagem

    print(f"\nTaxa de Empréstimo: {taxa:.2f}% ({livros_emprestados} de {total_livros} livros emprestados)")


def menu_principal(): # Função principal do menu
    biblioteca = carregar_biblioteca() # Carrega a biblioteca antes de iniciar o menu

    while True:
        print("\n" + "="*40)
        print("     SISTEMA DE GESTÃO DE BIBLIOTECA")
        print("="*40)
        print("     GESTÃO DE LIVROS")
        print("1 - Adicionar Livro")
        print("2 - Remover Livro")
        print("3 - Listar Todos os Livros")
        print("---"*10)
        print("     SISTEMA DE EMPRÉSTIMOS")
        print("4 - Emprestar Livro")
        print("5 - Devolver Livro")
        print("---"*10)
        print("     PESQUISA E FILTROS")
        print("6 - Pesquisar por Título")
        print("7 - Listar Livros Disponíveis")
        print("---"*10)
        print("     ESTATÍSTICAS")
        print("8 - Estatísticas por Género")
        print("9 - Taxa de Empréstimo")
        print("---"*10)
        print("0 - Sair")
        print("="*40)

        escolha = input("Escolha uma opção: ")

        if escolha == '1': # Opção para adicionar um novo livro
            print("\n--- Adicionar Livro ---") 
            titulo = input("Título: ") # Pede o título do livro
            autor = input("Autor: ") # Pede o autor do livro
            genero = input("Género: ") # Pede o gênero do livro

            try: # Verifica se o ano de publicação é um número válido
                ano_publicacao = int(input("Ano de Publicação: ")) 
                adicionar_livro(biblioteca, titulo, autor, genero, ano_publicacao) # Função responsável por adicionar o livro
            except ValueError: # Se o ano de publicação não for um número, exibe uma mensagem de erro
                print("\nErro: Ano de publicação deve ser um número.")

        elif escolha == '2':
            print("\n--- Remover Livro ---") # Opção para remover um livro
            try: # Verifica se o ID do livro é um número válido
                livro_id = int(input("ID do Livro a remover: ")) 
                remover_livro(biblioteca, livro_id) # Função responsável por remover o livro
            except ValueError: # Se o ID do livro não for um número, exibe uma mensagem de erro
                print("\nErro: ID do livro inválido.")

        elif escolha == '3': ## Opção para listar todos os livros
            print("\n--- Listar Todos os Livros ---")
            listar_livros(biblioteca) #  Função responsável por listar todos os livros

        elif escolha == '4': ## Opção para emprestar um livro
            print("\n--- Emprestar Livro ---")
            try: # Verifica se o ID do livro é um número válido
                livro_id = int(input("ID do Livro a emprestar: "))
                emprestar_livro(biblioteca, livro_id) # Função responsável por emprestar o livro
            except ValueError: # Se o ID do livro não for um número, exibe uma mensagem de erro
                print("\nErro: ID do livro inválido.") 

        elif escolha == '5': ## Opção para devolver um livro
            print("\n--- Devolver Livro ---")
            try: # Verifica se o ID do livro é um número válido
                livro_id = int(input("ID do Livro a devolver: "))
                devolver_livro(biblioteca, livro_id)
            except ValueError: # Se o ID do livro não for um número, exibe uma mensagem de erro
                print("\nErro: ID do livro inválido.")

        elif escolha == '6': ## Opção para pesquisar por título
            print("\n--- Pesquisar por Título ---")
            titulo = input("Escreve o título ou parte do título para pesquisar: ")
            pesquisar_titulo(biblioteca, titulo) # Função responsável por pesquisar o título

        elif escolha == '7': ## Opção para listar livros disponíveis
            print("\n--- Listar Livros Disponíveis ---")
            listar_livros_disponiveis(biblioteca) # Função responsável por listar os livros disponíveis

        elif escolha == '8': ## Opção para estatísticas por gênero
            print("\n--- Estatísticas por Género ---")
            estatisticas_genero(biblioteca) # Função responsável por mostrar as estatísticas por gênero

        elif escolha == '9': ## Opção para taxa de empréstimo
            print("\n--- Taxa de Empréstimo ---")
            taxa_emprestimo(biblioteca) # Função responsável por mostrar a taxa de empréstimo

        elif escolha == '0': # Opção para sair do programa
            print("\nPrograma encerrado.")
            break  
        else:
            print("\nOpção inválida. Por favor, escolha um número de 0 a 9.") # Mensagem de erro para opção inválida

def gerar_novo_id(biblioteca): # Gera um novo ID para um novo livro
    if not biblioteca: # Verifica se a biblioteca está vazia
        return 1
    else:
        max_id = max(livro.get("id", 0) for livro in biblioteca) # Encontra o maior ID existente na biblioteca
        return max_id + 1 # Adiciona 1 ao maior ID para gerar um novo ID


def adicionar_livro(biblioteca, titulo, autor, genero, ano_publicacao): # Função responsavel por adicionar um novo Livro
    ano_atual = datetime.now().year # Utilizado para o programa saber o ano atual

    if not titulo or not autor: # Verifica se o título e o autor foram fornecidos
        print("\nErro: Título e Autor são obrigatórios.")
        return 

    if ano_publicacao < 1000 or ano_publicacao > ano_atual: # Verifica se o ano de publicação é válido, 
        print(f"\nErro: Ano de publicação inválido. Deve estar entre 1000 e {ano_atual}.")
        return

    novo_id = gerar_novo_id(biblioteca) # Gera um novo ID para o livro

    novo_livro = {      # Função que cria o dicionario do novo livro
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "ano_publicacao": ano_publicacao,
        "disponivel": True,
        "data_emprestimo": None,    
    }
    biblioteca.append(novo_livro) # Adiciona o novo livro à biblioteca
    salvar_biblioteca(biblioteca) # Salva a biblioteca atualizada
    print(f"\nLivro '{titulo}' adicionado com sucesso com ID {novo_id}.")

if __name__ == "__main__": # Inicia o menu principal quando o script é executado diretamente
    menu_principal()  