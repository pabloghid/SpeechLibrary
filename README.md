# SpeechLibrary
Trabalho para a disciplina de Inteligência Artificial. Utiliza a Open Library API e reconhecimento de fala para buscar livros e autores.

## Funcionamento

O programa é capaz de fazer buscas por livros e autores pela voz. Ele apresenta dois botões, um para busca por livros e outra por autores. 
Existem outras funções de busca prontas para implantação prontas no model OpenBooks.

## Instalação

Versão do Python: 3.10

Clone o repositório:
```bash
git clone https://github.com/pabloghid/SpeechLibrary.git
```

Crie um ambiente virtual. Ex:
```bash
python -m venv venv
```
Ative o ambiente virtual.
No Windows:
```bash
venv\Scripts\activate
```
No Linux/macOS:
```bash
source venv/bin/activate
```

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

Para inicializar o projeto utilize o comando:
```bash
flask --app app run
```
