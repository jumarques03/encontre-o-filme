# 🎬 Encontre o Filme

Um projeto pessoal para praticar Python, FastAPI e integração com APIs REST. Este código permite buscar filmes pela OMDb API, salvar seus favoritos, listá-los e removê-los.

---

## 🚀 Funcionalidades

- 🔍 Buscar um filme pelo título (`/`)
- 📚 Buscar vários filmes por palavra-chave (`/buscar?query=...`)
- ❤️ Adicionar filmes à lista de favoritos (`/favoritos` com `POST`)
- ❌ Remover filmes da lista de favoritos (`/favoritos` com `DELETE`)
- 📄 Ver todos os filmes favoritos (`/favoritos` com `GET`)

---

## 🛠️ Tecnologias

- Python 3.11+
- FastAPI
- Requests
- OMDb API (gratuita)
- Uvicorn (para rodar o servidor)

---

## 📂 Boas práticas aprendidas

- Criação e uso de um arquivo `.gitignore` para esconder dados sensíveis, como a chave da API.
- Organização de variáveis de ambiente com o pacote `python-dotenv`.

---

## 🧪 Como testar

1. Clone o repositório
2. Crie um arquivo `.env` com sua chave OMDb
3. Instale as dependências:
```bash
pip install -r requirements.txt
