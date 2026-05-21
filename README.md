  # Sistema de Gestão de Biblioteca simples

  Este é um projeto desenvolvido em um âmbito universitário para unidade curricular de "Algoritmia".
  O principal objetivo deste projeto foi desenhar algoritmos eficientes para a manupilação, pesquisa, filtragem e persistência de dados utilizando o Python.

  ## Funcionalidades desenvolvidas

  O sistema simula o funcionamento real de uma biblioteca através de uma interface de linha de comando divida em quatro módulos:

  ### Gestão de Livros
  Adicionar Livro: Insere novos livros com validação automática (impede anos de publicação inválidos ou no futuro) e gera automaticamente IDs únicos de forma incremental.
  Remover Livro: Elimina um livro do catálogo através do algoritmo de busca pelo ID correspondente.
  Listar Todos os Livros: Percorre toda a estrutura de dados para exibir a lista completa de livros e o seu estado atual.

  ### Sistema de Empréstimos e Devoluções
  Emprestar Livro: Altera o estado do livro para "Emprestado" e regista automaticamente a data do empréstimo, aplicando uma validação que impede o empréstimo de livros que já não estejam disponíveis.
  Devolver Livro: Restaura o estado do livro para "Disponível" e limpa o registo da data de empréstimo.

  ###  Pesquisa e Filtros (Lógica de Busca)
  Pesquisar por Título: Implementa uma busca parcial e *case-insensitive* (ignora maiúsculas/minúsculas) para encontrar livros pelo título.
  Listar Livros Disponíveis: Filtra e exibe rapidamente apenas os elementos cujo estado de disponibilidade seja verdadeiro.

  ### Estatísticas e Métricas
  Estatísticas por Género: Utiliza uma estrutura de contagem (dicionário) para agrupar e contar os livros por cada género literário.
  Taxa de Empréstimo: Calcula a percentagem exata de livros que estão atualmente emprestados em relação ao total do catálogo.

  ## Tecnologia utilizada
  Linguagem utilizada : Python3
  Persistência de Dados (Decisão de Arquitetura) : Sendo este um proejto universitário e baixa escala, optei por utilizar o JSON para armazenar a base de dados.
