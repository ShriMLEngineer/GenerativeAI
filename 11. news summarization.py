import json
from dotenv import load_dotenv
import requests
from newspaper import Article

load_dotenv()

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

article_url = "https://timesofindia.indiatimes.com/sports/cricket/ashes/how-yuvraj-singhs-six-sixes-sparked-stuart-broads-evolution-into-a-world-class-bowler/articleshow/102245583.cms"

session = requests.session()

try:
    response = session.get(article_url, headers=headers, timeout=10)
    if response.status_code == 200:
        article = Article(article_url)
        article.download()

        print(f"title: {}")

