from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

alpha = ['D','E','F','G','H','I','J']
cols = ['Year','Lack of interest','Down, depressed', 'Trouble sleeping',\
  'Lathargic', 'Poor appetite', 'Feeling bad about self',\
  'Trouble concentrating', 'moving or speaking slowly or too fast',
  'Better off dead', 'difficulty problem caused','average']

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
    responses = answer.find('table', attrs = {'class':'values'})
    try:
      half = responses.find("tbody").find_all("tr")[1].find_all("td", attrs={"class":"values"})[2].text
      somewhat = responses.find("tbody").find_all("tr")[2].find_all("td", attrs={"class":"values"})[2].text
      all_days = responses.find("tbody").find_all("tr")[3].find_all("td", attrs={"class":"values"})[2].text
      total = responses.find("tbody").find_all("tr")[6]
      value = int(all_days) + int(half) + int(somewhat)
      total = total.find_all("td", attrs={"class":"values"})[3].text
      temp.append(int(value)/int(total))
    except:
      pass
  other_vals = temp[1:]
  try:
    avg = sum(other_vals)/len(other_vals)
    temp.append(avg)
  except:
    temp.append(0)

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