from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

alpha = ['D','E','F','G','H','I','J']
cols = ['Year','Lack of interest','Down, depressed', 'Trouble sleeping',\
  'Lathargic', 'Poor appetite', 'Feeling bad about self',\
  'Trouble concentrating', 'moving or speaking slowly or too fast',
  'Better off dead', 'difficulty problem caused']

def yearly(link,year):
  r = requests.get(link)
  soup = bs(r.content)
  soup

  tables = soup.find('div', attrs={'id':'Codebook'})
  tables = tables.find_all("div")
  if year >= 2009:
    actual_table = tables[1:]
  else:
    actual_table = tables[2:]
  temp = []
  temp.append(year+1)


  for answer in actual_table:
    # temp.append(answer.find('table', attrs = {'class':'Values'}.find_all('tr')[4]))
    responses = answer.find('table', attrs = {'class':'values'})
    try:
      fourth = responses.find("tbody").find_all("tr")[3]
      total = responses.find("tbody").find_all("tr")[6]
      value = fourth.find_all("td", attrs={"class":"values"})[2].text
      total = total.find_all("td", attrs={"class":"values"})[3].text
      temp.append(int(value)/int(total))
    except:
      pass

  return temp

year = 2005
link_head = 'https://wwwn.cdc.gov/Nchs/Nhanes/' #2007-2008/DPQ_E.htm', 2007)

big_df = []

for letter in alpha:
  tag = str(year) + '-' + str(year+1) + '/DPQ_' + letter + '.htm'
  big_df.append(yearly(link_head + tag, year))
  year += 2

big_df
df = pd.DataFrame(big_df, columns = cols)
df = df.set_index('Year')
df = df.drop(columns=['difficulty problem caused'])
df.to_csv('depression_data.csv')