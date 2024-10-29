import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0827b6d9abb0fadd162f27bba7ccbff9'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '16126'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200 

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'ТанЧик'