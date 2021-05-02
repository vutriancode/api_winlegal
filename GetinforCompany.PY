import requests
import time
import config
from bs4 import BeautifulSoup 

class Company:

    def __init__(self):
        self.linkLogin = "https://dangkyquamang.dkkd.gov.vn/auth/Public/LogOn.aspx"
        self.linkDefault = "https://dangkyquamang.dkkd.gov.vn/online/Default.aspx"
        self.BASE_URL = "https://dangkyquamang.dkkd.gov.vn"
        self.linkRegisterComapy = ""
        self.time = time.time()
        self.requests  = requests.Session()
    
    def find_data_login(self,webpage):
        #try:
        soup = BeautifulSoup(webpage.text, 'html.parser')
        data = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__PREVIOUSPAGE": soup.find(id="__PREVIOUSPAGE")['value'],
            "__EVENTVALIDATION":soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='ctl00_hdParameter')['value'],
            "ctl00$searchtype": 1,
            "ctl00$C$W1$UserName": config.USER_NAME,
            "ctl00$C$W1$Password": config.PASS_WORD,
            "ctl00$C$W1$btnStep1_Login": "Đăng nhập"
            }
        #except Exception as e:
        #    print(e)
        #    return "loi trang"
        return data
    def login(self):
        webpage = self.requests.get(self.linkLogin)
        data =self.find_data_login(webpage)
        response = self.requests.post(self.linkLogin,data) 
    def find_link_company(self):
        times = time.time()
        delta_time = self.time - times
        if(delta_time>1000):
            self.time = times
            self.login()
        webpage = self.requests.get(self.linkDefault)
        soup = BeautifulSoup(webpage.text, 'html.parser')
        data = {
            "__EVENTTARGET": "ctl00$LV3$mCon",
            "__EVENTARGUMENT" : "bĐĂNG KÝ DOANH NGHIỆP",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1
            }

        response = self.requests.post(self.linkDefault,data = data,allow_redirects=False) 
        print(response.status_code)
        return  response.headers['Location']
    def get_Company(self,sdt, can_cuoc_cong_dan):
        #link =self.find_link_company()
        link =self.BASE_URL + self.find_link_company()
        print(link)
        response = self.requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        data1 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$CtlSubmissionType": 2,
            "ctl00$C$myWizard$StartNavigationTemplateContainerID$StartNextButton": "Tiếp theo"
            }
        response = self.requests.post(link,data1)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        data2 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$CtlType": "CHN",
            "ctl00$C$myWizard$StepNavigationTemplateContainerID$StepNextButton": "Tiếp theo"
            }
        response = self.requests.post(link,data2)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        data3 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$GDT_CODEFld": sdt,
            "ctl00$C$myWizard$btnAmendGDTUID": "Tìm kiếm",
            "ctl00$C$myWizard$AmenEnterpriseUIDFld": "" ,
            }
        response = self.requests.post(link,data3)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        data4 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$GDT_CODEFld": "", 
            "ctl00$C$myWizard$AmenEnterpriseUIDFld": "", 
            "ctl00$C$myWizard$StepNavigationTemplateContainerID$StepNextButton": "Tiếp theo"
            }
        response = self.requests.post(link,data4)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')

        data5 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$PERS_SUBGroup": "IS_REPRESENTATIVE_BUTTON",
            "ctl00$C$myWizard$Pers_Doc_NoFld": can_cuoc_cong_dan,
            "ctl00$C$myWizard$StepNavigationTemplateContainerID$StepNextButton": "Tiếp theo"
            }
        response = self.requests.post(link,data5)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        data6 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$CtlAmendmentType": "CHAPAR",
            "ctl00$C$myWizard$NAME_CHANGE_YN_IDFld": "N",
            "ctl00$C$myWizard$StepNavigationTemplateContainerID$StepNextButton": "Tiếp theo"
            }
        response = self.requests.post(link,data6)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        data7 = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            "ctl00$C$myWizard$FinishNavigationTemplateContainerID$FinishButton": "Bắt đầu"
            }
        response = self.requests.post(link,data7)
        return response.url

    def get_share(self,url):
        response = self.requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data8 = {
            "__EVENTTARGET": "ctl00$C$BLCtl$CtlList$ctl07$LnkEdit",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            }
        response = self.requests.post(response.url,data8)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', attrs={'id':'C_UC_DW_OTHEREditCtl_CtlList'})
        share_value = soup.find(id = "C_UC_DW_OTHEREditCtl_VALUE_OF_EACH_SHAREFld")["value"]
        table_rows = table.find_all('tr')
        print(share_value)
        for tr in table_rows[1:]:
            td = tr.find_all('td')
            row = [tr.find("input")["value"] for tr in td[2:]]
            print(row)
        table = soup.find('table', attrs={'id':'C_UC_DW_OTHEREditCtl_CtlListSales'})
        table_rows = table.find_all('tr')
        for tr in table_rows[1:]:
            td = tr.find_all('td')
            row = [tr.find("input")["value"] for tr in td[2:]]
            print(row)

            
    def get_capital(self,url):
        response = self.requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data8 = {
            "__EVENTTARGET": "ctl00$C$BLCtl$CtlList$ctl06$LnkEdit",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            }
        response = self.requests.post(response.url,data8)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', attrs={'id':'C_UC_DW_CAPITALEditCtl_CtlSourceList'})
        capital_value = soup.find(id = "C_UC_DW_CAPITALEditCtl_CPT_CHARTER_AMOUNTFld")["value"]
        table_rows = table.find_all('tr')
        print(capital_value)
        for tr in table_rows[1:]:
            td = tr.find_all('td')
            row = [tr.find("input")["value"] for tr in td[1:]]
            print(row)
        table = soup.find('table', attrs={'id':'C_UC_DW_CAPITALEditCtl_CtlList'})
        table_rows = table.find_all('tr')
        for tr in table_rows[1:]:
            td = tr.find_all('td')
            row = [tr.find("input")["value"] for tr in td[1:]]
            print(row)

    def get_business(self,url):
        response = self.requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data8 = {
            "__EVENTTARGET": "ctl00$C$BLCtl$CtlList$ctl04$LnkEdit",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            }
        response = self.requests.post(response.url,data8)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', attrs={'id':'C_CtlList'})
        table_rows = table.find_all('tr')
        for tr in table_rows[1:]:
            td = tr.find_all('td')
            row = td[3].text
            row2 = td[4].find("div").text
            print(row)
            print(row2)

    def get_address(self,url):
        response = self.requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data8 = {
            "__EVENTTARGET": "ctl00$C$BLCtl$CtlList$ctl03$LnkEdit",
            "__EVENTARGUMENT" : "",
            "__VIEWSTATE": soup.find(id='__VIEWSTATE')['value'],
            "__VIEWSTATEGENERATOR": soup.find(id='__VIEWSTATEGENERATOR')['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
            "ctl00$hdParameter" : soup.find(id='hdParameter')['value'],
            "ctl00$FldSearch": "",
            "ctl00$FldSearchID": "",
            "ctl00$searchtype": 1,
            }
        response = self.requests.post(response.url,data8)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find(id='C_ADDRCtl_COUNTRY_IDFld')
        country = table.find('option', attrs={'selected':'selected'}).text
        table = soup.find(id='C_ADDRCtl_CITY_IDFld')
        city = table.find('option', attrs={'selected':'selected'}).text
        table = soup.find(id='C_ADDRCtl_DISTRICT_IDTr')
        district = table.find('option', attrs={'selected':'selected'}).text
        table = soup.find(id='C_ADDRCtl_WARD_IDTr')
        ward = table.find('option', attrs={'selected':'selected'}).text
        stress = soup.find(id='C_ADDRCtl_STREET_NUMBERFld')["value"]

        phone_number = soup.find(id='C_DCONTClt_HO_PHONEFld').text
        email = soup.find(id='C_DCONTClt_HO_EMAILFld').text
        print(country)
        print(city)
        print(district)
        print(ward)
        print(stress)





        
      
if __name__=='__main__':
    company = Company()
    company.login()
    url = company.get_Company("0102549487","001178016496")
    company.get_share(url)
    company.get_capital(url)
    company.get_business(url)
    company.get_address(url)
