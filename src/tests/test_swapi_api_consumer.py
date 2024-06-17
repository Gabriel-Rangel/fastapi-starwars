from app.swapi_api_consumer import SwapiApiConsumer

def test_get_starships(requests_mock):

    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some':'thing'})
    swapi = SwapiApiConsumer()
    response = swapi.get_starships(page=1)

    print(response)
