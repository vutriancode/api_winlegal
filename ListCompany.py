import requests
from bs4 import BeautifulSoup
import time


class ListCompany:
    def __init__(self):
        self.H_PARAM_TIME = 2 * 60
        self._API_ENDPOINT = "https://dichvuthongtin.dkkd.gov.vn/inf/Public/Srv.aspx/GetSearch"
        self._HOME_URL = "https://dichvuthongtin.dkkd.gov.vn/inf/default.aspx"
        self._reset_h_param()

    def _get_h_param(self):
        h_param = ''
        try:
            response = requests.get(self._HOME_URL)
            soup = BeautifulSoup(response.text, 'html.parser')
            h_param = soup.find(id='ctl00_hdParameter')['value']
        except Exception as e:
            print(e)
        return h_param

    def _reset_h_param(self):
        self._h_param = self._get_h_param()
        self._h_param_creation_time = time.time()

    def get_list_company(self, data: str):
        result = None

        if (time.time() - self._h_param_creation_time) > self.H_PARAM_TIME:
            self._reset_h_param()

        data = {'searchField': data, 'h': self._h_param}
        try:
            response = requests.post(url=self._API_ENDPOINT, json=data)
            result = response.json()['d']
        except Exception as e:
            print(e)
        return result