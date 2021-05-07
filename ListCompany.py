import requests
from bs4 import BeautifulSoup
import time
import json


class ListCompany:
    def __init__(self):
        self.H_PARAM_TIME = 2 * 60
        self._API_ENDPOINT = "https://dichvuthongtin.dkkd.gov.vn/inf/Public/Srv.aspx/GetSearch"
        self._HOME_URL = "https://dichvuthongtin.dkkd.gov.vn/inf/default.aspx"
        self._API_ENDPOINT2 = "https://www.thongtincongty.com/search/"
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
        result = {}
        if (time.time() - self._h_param_creation_time) > self.H_PARAM_TIME:
            self._reset_h_param()

        data = {'searchField': data, 'h': self._h_param}
        try:
            response = requests.post(url=self._API_ENDPOINT, json=data)
            result = response.json()['d'][0]
        except Exception as e:
            print(e)
        try:
            response = requests.get(url=self._API_ENDPOINT2+str(data["searchField"]))
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find('div', {'class': 'search-results'})
            b=soup.find('a')["href"]
            response = requests.get(url=b)
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find("div",{"class":"jumbotron"}).text
            data  = data.split("            ")
            loai_hinh = data[2].replace("\n","")

            loai_hinh = loai_hinh.replace(" \r","").split(": ")[1]
            ngay_cap =data[-4].replace("\n","").split(": ")[1]
            result["loai_hinh_doanh_nghiep"] = loai_hinh
            result["ngay_cap_phep"] = ngay_cap
        
            print(result)

        except Exception as e:
            print(e)
        return result