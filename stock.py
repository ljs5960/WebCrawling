import requests
from bs4 import BeautifulSoup as bs

# https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page=1
# https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page=35
i = 1
for i in range(36):
  url = requests.get(f"https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page={i}")
  soup = bs(url.text, "lxml")
  
  stocks = soup.select("#contentarea > div.box_type_l > table.type_2 > tbody > tr")
  
  for stock in stocks:
    try:
      stock_name = stock.select_one("td:nth-child(2) > a").text
    except AttributeError:
      continue
    print(stock_name)
    
  i += 1