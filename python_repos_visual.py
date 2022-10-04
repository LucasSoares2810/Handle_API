from plotly.graph_objs import bar
from plotly import offline
from python_repos import *


repo_names = []
stars = []
labels = []
links = []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Mostrar informações quando passar o mouse por cima
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}\n{description}"
    labels.append(label)

    # Adicionando um link para cada projeto
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    links.append(repo_link)

# Construindo o gráfico
data = [{
    'type': 'bar',
    'x': links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 115, 130)',
        'line': {'width': 1.5, 'color': 'rgb(20,25,40)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Repositórios favoritos no Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Número de estrelas',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},

    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='repositorios_python.html')
