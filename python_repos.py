import requests

# Faz uma chamada da API e guarda a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# guarda a resposta da API em uma variével
response_dict = r.json()
repo_dicts = response_dict['items']


