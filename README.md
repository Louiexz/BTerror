# BTerror

!["BTerror"]('bterror.png')

Aplicativo "BTerror" criado utilizando kivy, com interface simples.
Dedicado ao aniversário de 9 anos do meu sobrinho.

## Funcionalidades

    Terror com personagens autênticos.
    Sons assustadores (Ou não).
    Fácil de usar.

## Pré-requisitos

### Certifique-se de ter o seguinte instalado antes de começar:
  
     Python 3
     Kivy
     Pygame

## Instalação e Uso

1. Baixe de acordo com sua plataforma:

    - Windows x64: 
    - Linux x86_64: 
    - Apk: Em breve.

2. Ou siga os seguintes passos:

- Clone o repositório:

        git clone https://github.com/Louiexz/BTerror.git
        cd BTerror
 
 - Instale as dependências:

        pip install -r requirements.txt

 - Execute o aplicativo:

        python main.py

## Estrutura do Projeto

    BTerror/
    │
    ├── main.py           # Arquivo principal do aplicativo
    ├── assets/             # Diretório contendo arquivos necessários
    |   ├── scripts/           # Diretório contendo funções e/ou classes
    │   |   ├── functs/           # Diretório de funções
    |   |   |   ├── manageFiles.py   # Classe para gerenciar telas
    |   |   |   └── sound.py         # Classe para gerenciamento dos sons
    |   |   └── screenDirectory/  # Diretório de telas
    |   |       ├── introduceFiles/  # Classe e interface da tela de introdução
    |   |       ├── splashFiles/     # Classe e interface da tela splash
    |   |       ├── homeFiles/       # Classe e interface da tela de home
    |   |       ├── terrorFiles/     # Classe e interface da tela terror
    |   |       └── creditsFiles/    # Classe e interface da tela de créditos
    │   ├── sound/          # Diretório de sons
    |   |   ├── splash/        # Sons da tela splash
    │   |   ├── home/          # Sons da tela home
    |   |   ├── terror/        # Sons da tela terror
    |   |   └── credits/       # Sons da tela de introdução
    |   └── images/         # Diretório contendo imagens
    │       ├── icon/          # Icones do jogo
    |       ├── splash/        # Imagens da tela splash
    │       ├── home/          # Imagens da tela home
    |       └── terror/        # Imagens da tela terror
    └── requirements.txt  # Arquivo contendo as dependências do Python

## Contribuições
Louiexz - Autor e Desenvolvedor do BTerror<br>

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
