import requests
import json
from bs4 import BeautifulSoup
def get_deta():
    #fileを取得
    file = "/Users/minori419252/Desktop/Study_Python/deta/paradox.txt"
    #urlを取得
    url = "http://complex1105.web.fc2.com/hikito.html"
    #urlを開く
    html = requests.get(url)
    html.raise_for_status()
    #beautifulsoup
    soup = BeautifulSoup(html.text,"html.parser")
    a_text = soup.find_all('a')
    new_text = str(a_text)
    try:
        f = open(file)
        old_text = f.read()
    except:
        old_text = " "
    if (new_text == old_text):
        return False
    else:
        f = open(file,"w")
        f.writelines(new_text)
        f.close()
        return True
if __name__ == "__main__":
    if get_deta():
        webhook_url = "https://hooks.slack.com/services/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"
        requests.post(webhook_url, data=json.dumps({'text': '更新されました！  http://complex1105.web.fc2.com/youkoso.html'}))
    else:
        webhook_url = "https://hooks.slack.com/services/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"
        requests.post(webhook_url, data=json.dumps({'text': '今日の更新はありませんでした'}))