import requests
from requests import Request
from typing import Type
from collections import namedtuple


class SwapiApiConsumer:
    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')
    
    def get_starships(self, page:int) -> any:
        # params = {'page':page}
        # response = requests.get('https://swapi.dev/api/starships/', params=params)
        # return response.json()
        req = requests.Request(
            method='GET', 
            url='https://swapi.dev/api/starships/', 
            params={'page': page}
            )
        
        req_prepared = req.prepare()
        response = self.__send_request(req_prepared)
        
        return self.get_starships_response(
            status_code=response.status_code,
            request=req,
            response=response.json()
        )


    @classmethod
    def __send_request(cls, req_prepared:Type[Request]) -> any:
        http_request = requests.Session()
        response = http_request.send(req_prepared)

        return response
