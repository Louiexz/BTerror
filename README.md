# BTerror

!["BTerror"]('bterror.png')

Aplicativo "BTerror" criado utilizando kivy, com interface simples.

## Funcionalidades

    Terror com personagens conhecidos.

## Pré-requisitos

### Certifique-se de ter o seguinte instalado antes de começar:
  
     Python 3
     Kivy

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

        python run.py

## Estrutura do Projeto

    BTerror/
    │
    ├── run.py           # Arquivo principal do aplicativo
    ├── assets/             # Diretório contendo arquivos necessários
    |   ├── scripts/           # Diretório contendo funções e/ou classes
    │   |   ├── functs/           # Diretório de funções
    |   |   |   ├── manageFiles.py   # Classe para gerenciar telas
    |   |   |   └── sound.py         # Classe para gerenciamento dos sons
    |   |   └── screenDirectory/  # Diretório de telas
    |   |       ├── splashFiles/     # Classe e interface da tela splash
    |   |       ├── homeFiles/       # Classe e interface da tela de home
    |   |       └── terrorFiles/     # Classe e interface da tela terror
    │   ├── sound/          # Diretório de sons
    |   └── images/         # Diretório contendo imagens
    │       ├── home/          # Imagens da tela home
    |       ├── splash/        # Imagens da tela splash
    |       └── terror/        # Imagens da tela terror
    └── requirements.txt  # Arquivo contendo as dependências do Python

## Contribuições
Louiexz - Autor e Desenvolvedor da BTerror<br>

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
