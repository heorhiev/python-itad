import requests

class Itad:

    PUBLIC_URL = 'https://api.isthereanydeal.com' 
    PRIVATE_URL = 'https://private-anon-d037b321a1-itad.apiary-proxy.com' 
    SUCC_STATUS_CODE = 200


    def __init__(self, key):
        self._key = key


    # возвращает магазины
    def getShops(self):
        shops = self._getPublicResult('v01/web/stores/all')  

        if (shops):
            return shops['data']            


    # возвращает предложения
    def getDeals(self, shops, limit = 100):
        deals = self._getPrivateResult('v01/deals/list', {
            'shops': shops,
            'limit': limit
        })

        if ('data' in deals and 'list' in deals['data']):
            return deals['data']['list']


    # доступ к приватному API
    def _getPrivateResult(self, path, params = {}):
        url = self.PRIVATE_URL + '/' + path + '/?';
        params['key'] = self._getKey();

        return self._getResult(url, params)  


    # доступ к публичному API
    def _getPublicResult(self, path, params = {}):
        url = self.PUBLIC_URL + '/' + path + '/?';
        return self._getResult(url, params)             


    # выполнение запроса к API
    def _getResult(self, url, params):
        response = requests.get(url, params)

        if (self.SUCC_STATUS_CODE != response.status_code):
            raise Exception('Ошибка ' + str(response.content))

        return response.json()         


    def _getKey(self):
        return self._key