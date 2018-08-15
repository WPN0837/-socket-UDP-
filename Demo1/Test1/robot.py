# http://tubiao.zhcw.com/tubiao/zhcw_agent.jsp?url=ssqNew/ssqJsp/ssq_hq_general_dataTuAsc.jsp

import requests
from bs4 import BeautifulSoup
url = 'http://tubiao.zhcw.com/tubiao/zhcw_agent.jsp?url=ssqNew/ssqJsp/ssq_hq_general_dataTuAsc.jsp'
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
Cookie = 'Hm_lvt_692bd5f9c07d3ebd0063062fb0d7622f=1534132437; _ga=GA1.2.821283985.1534132437; _gid=GA1.2.1164185125.1534132437; Hm_lpvt_692bd5f9c07d3ebd0063062fb0d7622f=1534132505; JSESSIONID=abcKu1ylz97Ecf9RiBXuw'
headers = {'user-agent':User_Agent, 'cookie': Cookie}
response = requests.get(url, headers = headers)
if response.status_code == 200:
    responseB= BeautifulSoup(response.text, 'html.parser')
    # < tr class ='hgt' >
    response_list = responseB.find_all('tr', {'class': 'hgt'})
    print(response_list)