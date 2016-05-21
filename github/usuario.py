import requests


def buscar_avatar_url(nome):
    reposta_http = requests.get('https://api.github.com/users/renzon')
    dct = reposta_http.json()
    return dct['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar_url('renzon'))
