"""
네이버 뉴스 기사 하나를 크롤링해서 해당 뉴스 기사에 많이 언급된 단어를 가지고 클라우드를 생성
"""

import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/001/0015633995'

response = requests.get(url)
print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)

data = soup.select('#dic_area')

text = data[0].text

# from konlpy.tag import Okt
# from collections import Counter

# okt = Okt()
# tokens = okt.nouns(text)
# print(tokens)

# word_count = Counter(tokens)

# print(word_count)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """
파이썬 데이터 분석 머신러닝 인공지능 시각화 판다스 넘파이 matplotlib seaborn
텍스트 마이닝 워드클라우드 형태소 분석 konlpy 자연어처리 데이터 전처리
"""

wc = WordCloud(
  font_path='C:\Windows\Fonts\malgun.ttf',
  width=800, height=400,
  background_color='white'
)

wc.generate(text)
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()