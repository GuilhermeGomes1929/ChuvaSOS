import requests
from bs4 import BeautifulSoup

url = 'http://old.apac.pe.gov.br/_lib/pluviometria.request.php'
page = requests.post(url, data={
                     'acao': 'exibePluviometrosRMRSite', 'local': '2611606', 'order': 'null'})

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    odd_values = soup.find_all('tr', {'class': 'odd'})

    for row in odd_values:
        columns = row.find_all('td')
        for column in columns:
            print(column.text)

else:
    print('Não foi possível acessar a página:', url)
