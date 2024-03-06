# ChatPDF

ChatPDF é um projeto em Python que utiliza a biblioteca LangChain e OpenIA para criar um chat que converte conversas em um arquivo PDF.

## Sobre o Projeto

Este projeto visa criar uma interface de chat onde os usuários podem conversar com um chatbot e converter suas conversas em um arquivo PDF. Ele é construído usando o Streamlit para a interface do usuário e integra a biblioteca LangChain para processamento de linguagem natural e a API OpenAI para geração de respostas.

## Instalação

Para instalar as dependências do projeto, certifique-se de ter o Python 3.10.11 instalado e execute o seguinte comando:

poetry install

## Utilização

Para executar o ChatPDF, utilize o seguinte comando:

poetry run streamlit run app.py

Isso iniciará o servidor Streamlit e abrirá o aplicativo no navegador padrão.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- Python 3.10.11
- Streamlit 1.31.1
- python-dotenv 1.0.1
- LangChain 0.1.11
- PyPDF2 3.0.1
- Faiss-cpu 1.8.0
- OpenAI 1.13.3
- TikToken 0.6.0
- Streamlit-Chat 0.1.1

Certifique-se de que todas as dependências estejam instaladas antes de executar o projeto.

## Autor

Moises Alvarenga <moises.alvarenga@outlook.com>

## Licença

Este projeto está licenciado sob a MIT License.
