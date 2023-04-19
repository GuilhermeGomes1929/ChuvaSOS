import requests
import pandas as pd
# import pyspark.pandas as ps
from bs4 import BeautifulSoup


def get_tag_content(tag):
    return tag.text


def concat_date_and_time(date_list):
    date_list_concat = []
    for i in range(len(date_list)):
        if i % 2 == 1:
            date_list_concat.append(
                str(date_list[i].text) + str(date_list[i - 1].text))
    return date_list_concat


url = 'http://old.apac.pe.gov.br/_lib/pluviometria.request.php'
page = requests.post(url, data={
                     'acao': 'exibePluviometrosRMRSite', 'local': '2611606', 'order': 'null'})

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    odd_values = soup.find_all('tr', {'class': 'odd'})
    local_tags = soup.find_all('span', {'class': 'glb-corpo-span-preto'})
    date_time_tags = soup.find_all(
        'td', {'class': 'medio'})  # corrigir TAG dps

    locals = list(map(get_tag_content, local_tags))
    date_time = concat_date_and_time(date_time_tags)

    print(date_time)
    psdf = pd.DataFrame.from_dict(
        {
            'Locals': locals
        }
    )
    print(psdf)

else:
    print('Não foi possível acessar a página:', url)
