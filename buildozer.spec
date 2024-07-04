[app]

# Nome do seu aplicativo
title = BTerror

# Nome do pacote do seu aplicativo (isso será seu nome de pacote no Android)
package.name = bterror

# Domínio do pacote do seu aplicativo (exemplo: com.seuapp)
package.domain = org.bterror

# Versão do seu aplicativo
version = 2.0

# Ícone do seu aplicativo (coloque o caminho para o ícone dentro do seu projeto)
icon.filename = assets/images/icon/bt.ico

# Principal arquivo Python que inicia seu aplicativo Kivy
# Deve ser o mesmo nome do arquivo que contém seu 'build'
main.py = run.py

# Lista das dependências do Python que seu aplicativo requer
requirements = python3,kivy

# Lista de arquivos/pastas a serem incluídos no pacote do seu aplicativo
# Inclui scripts Python, arquivos KV, imagens e sons necessários
source.include_exts = py,kv,png,mp3,ico
source.include_patterns = assets/**/*.png, assets/**/*.mp3, assets/**/*.kv
source.include_folders = assets

# Lista de arquivos/pastas a serem excluídos do pacote do seu aplicativo
source.exclude_exts = spec, txt, .gitignore
source.exclude_files = bterror.png
source.exclude_dirs = tests, __pycache__

# Diretório raiz onde Buildozer deve procurar pelos arquivos fonte do aplicativo
source.dir = .

# Versão mínima do Android suportada pelo seu aplicativo
android.minapi = 21

# Versão do SDK a ser usada para compilar o seu aplicativo
android.sdk = 28

# Nível de log do Buildozer (0 = sem logs, 1 = erros apenas, 2 = erros e avisos, 3 = tudo)
log_level = 2

# Configurações específicas do Android
android.arch = armeabi-v7a
android.allow_back_key = True
android.allow_downloads = True

# Kivy versão a ser usada
kivy = 2.0.0

# Correção da orientação do aplicativo
android.allow_screens = portrait, landscape
