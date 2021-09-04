import whois

from random import choice
from requests import get, exceptions

def components():
    pre = [
        'Hi', 'Oxyge', 'Tita', 'Nitro', 'Xeno', 'Ura', 'Vanda', 'Hype',
        'Nexu', 'Alpha', 'Ze', 'Zen', 'Force', 'Neo', 'Ne', 'Xe',
        'Veno', 'Ze', 'Argo', 'Xe', 'Auro', 'Nebula', 'Cryp', 'Lumi', 'Ve', 'Turbo',
        'Zenu', 'Fire', 'Phoe', 'Fo', 'Ve', 'Za', 'Mysti', 'Evo', 'Mythi', 'Micro'
    ]

    mid = [
        ''
    ]

    end = [
        'nix', 'y', 'xy', 'nus', 'vy', 'vex', 'Z', 'X',
        'vus', 'nit', 'nox', 'xie', 'xus', 'vos', 'vas', 'tic', 'neo',
        'nity', 'nium', 'phix', 'nia', 'vis', 'tix',
        'Side', 'Planet', 'World', 'Live', 'One', 'Net', 'lix', 'las', 'mi', 'Q', 'V', 'nion',
        'rious', 'ntic', 'ntix', 'night', 'rion', 'tical', 'no', 'tics'
    ]

    return (pre, mid, end)

def build():
    (pre, mid, end) = components()
    return ''.join([choice(pre), choice(mid), choice(end)])

def check_website(url: str) -> bool:
    try:
        if whois.whois(url):
            return True
        return False

    except Exception as e:
        return False

    # # thanks https://stackoverflow.com/a/55799417/14345173
    # try:
    #     response = get(url, timeout=0.75, allow_redirects=False)
    #     try:
    #         if response.status_code < 400:
    #             return True
    #     except exceptions.HTTPError:
    #         return False
    # except (exceptions.ConnectionError, exceptions.ReadTimeout):
    #     return False

def generate(check_tld='com'):
    generated = build()

    if check_tld:
        url = f'http://{generated.lower()}.{check_tld}'
        avaiable = not check_website(url)

        if avaiable:
            generated += ' ✔'

    return generated

def generate_list(length=5, check_tld=False):
    generated = []

    for _ in range(length):
        generated.append(generate(check_tld=check_tld))

    return generated

if __name__ == '__main__':
    print(generate_list())