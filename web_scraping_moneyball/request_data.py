import requests
import json
import pandas as pd

url = "https://1xbet.whoscored.com/StatisticsFeed/1/GetPlayerStatistics?category=summary&subcategory=all&statsAccumulationType=0&isCurrent=true&playerId=&teamIds=&matchId=&stageId=&tournamentOptions=2,3,4,5,22&sortBy=Rating&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=Overall&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=true&page=&includeZeroValues=&numberOfPlayersToPick=1560"

payload={}
headers = {
  'authority': '1xbet.whoscored.com',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'model-last-mode': 'T3e3dgTjhvnAoGZ8aFIy/ptWITLOHoM+zqR+YUxKZpo=',
  'x-requested-with': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://1xbet.whoscored.com/Statistics',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': 'visid_incap_774906=Fa+x0sFLQtS3AE6kqGXFQZHl4mAAAAAAQUIPAAAAAABDa67uiQdGpdF25RpBBVe8; _ga=GA1.2.1634098555.1625482855; _gid=GA1.2.1977073524.1625482855; _pbjs_userid_consent_data=3524755945110770; _pubcid=5054d6c8-b273-464a-98c6-7cdacf98b387; _fbp=fb.1.1625482857238.843080706; _xpid=2563357798; _xpkey=xpaVEc0XTX-aTDJ-Mx5YWVHRVviXnyRh; _lr_env_src_ats=false; _unifiedid=%7B%22TDID%22%3A%222637eeaf-ff40-4ad1-bcf8-932141d50607%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222021-06-05T11%3A00%3A59%22%7D; __qca=P0-2038413970-1625482857950; incap_ses_572_774906=Qm1YfDhXG0mEhQ1XTifwB4724mAAAAAAL2lBlkvheFdhetnp1xwzCg==; _gat=1; _gat_subdomainTracker=1; ___utmvc=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'
}

r = requests.get(url, headers=headers)
playerdata = r.json()

#print(playerdata.keys())
#print((playerdata['playerTableStats']))
#print(playerdata['paging'])

df = pd.json_normalize(playerdata['playerTableStats'])
df.to_csv("D:\Python\Webscraping_with_Scrapy\Moneyball\data\playerstats.csv")
print(df.head())
