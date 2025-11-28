# Projeto-Integrador-2Sem
Password Guardian

Um projeto simples e prático de cibersegurança focado em segurança de senhas.

Este repositório contém um script Python que permite:

1.
Verificar a força de uma senha fornecida, fornecendo feedback detalhado.

2.
Gerar senhas seguras e aleatórias com base em critérios definidos (comprimento, tipos de caracteres).

Estrutura do Projeto

O projeto possui uma estrutura limpa e minimalista, ideal para um repositório de exemplo:

•
password_guardian.py: O script principal com a lógica de verificação e geração de senhas.

•
README.md: Este arquivo, contendo a descrição, instalação e uso.

•
LICENSE: A licença do projeto (MIT).

•
requirements.txt: Lista de dependências (vazio, pois usa apenas bibliotecas padrão do Python).

Instalação e Uso

O projeto é escrito em Python e não requer a instalação de bibliotecas externas.

1. Clonar o Repositório

Para começar, clone o repositório para sua máquina local:

Bash


git clone [URL_DO_REPOSITORIO]
cd password_guardian


2. Executar o Script

Execute o script diretamente usando o interpretador Python:

Bash


python3 password_guardian.py


3. Opções do Menu

Ao executar, você será apresentado a um menu interativo:

Opção
Descrição
1
Verificar Força da Senha: Permite digitar uma senha e recebe uma classificação de força (Fraca, Moderada, Forte, Muito Forte) e um feedback detalhado sobre o que pode ser melhorado (comprimento, presença de maiúsculas, minúsculas, números e símbolos).
2
Gerar Senha Segura: Permite configurar o comprimento e os tipos de caracteres (maiúsculas, minúsculas, números, símbolos) para gerar uma senha aleatória e criptograficamente segura.
3
Sair


