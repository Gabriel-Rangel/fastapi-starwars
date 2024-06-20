from app.swapi_api_consumer import SwapiApiConsumer

def test_get_starships():

    #requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some':'thing'})
    swapi = SwapiApiConsumer()
    page = 1
    
    response = swapi.get_starships(page=page)

    assert response.request.method == 'GET'
    assert response.request.url == 'https://swapi.dev/api/starships/'
    assert response.status_code == 200

    # req = requests.Request(
    # method='GET', 
    # url='https://swapi.dev/api/starships/', 
    # params={'page': page}
    # )

    print(response)
