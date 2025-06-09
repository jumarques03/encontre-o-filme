from fastapi import FastAPI
import requests
from config import omdb_api_key
import json

app = FastAPI()
filmes_favoritos = []

def buscar_filme(title:str): 
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={title}"
    response = requests.get(url)

    if response.status_code ==200:
        dados_filme_json = response.json()
        if dados_filme_json['Response'] == 'False':
            return {'erro': 'Filme não encontrado'}
        else:
            dados_importantes_filme = {
                'titulo': dados_filme_json['Title'],
                'ano': dados_filme_json['Year'],
                'genero': dados_filme_json['Genre'],
                'diretor': dados_filme_json['Director'],
                'avaliacao_imdb' : dados_filme_json['imdbRating'],
                'plot': dados_filme_json['Plot'],
                'poster': dados_filme_json['Poster']
            }
            return dados_importantes_filme
    else:
        return {'erro': 'Não foi possível buscar o filme'}
    
@app.get('/')
def procurar_por_titulo_filme(title: str):
   buscar_filme(title)

@app.get('/buscar')
def buscar_varios_filmes(query: str):
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&s={query}"
    response = requests.get(url)
    dados = response.json()

    if dados.get("Response") == "False":
        return {"erro": "Nenhum filme encontrado com essa busca"}

    resultados = []
    for item in dados["Search"]:
        resultados.append({
            "titulo": item["Title"],
            "ano": item["Year"],
            "poster": item["Poster"]
        })

    return resultados
    
@app.post('/favoritos')
def adicionar_favoritos(title: str):
    filme_fav = buscar_filme(title)
    if 'erro' in filme_fav: 
        return {'erro': 'Não foi possível adicionar o filme à sua lista de favoritos.'}
    
    if filme_fav not in filmes_favoritos:
        filmes_favoritos.append(filme_fav)
        return {'mensagem': 'Filme adicionado aos favoritos com sucesso!'}
    else:
        return {'alerta': 'Este filme já está na sua lista de favoritos!'}

@app.get('/favoritos')
def listar_favoritos():
    return filmes_favoritos

@app.delete('/favoritos')
def remover_filme_favoritos(title:str):
    for filme in filmes_favoritos:
        if filme['titulo'].lower() == title.lower():
                    filmes_favoritos.remove(filme)
                    return {"mensagem": f"Filme '{title}' removido dos favoritos."}

    return {"erro": f"Filme '{title}' não encontrado na lista de favoritos."}


    

