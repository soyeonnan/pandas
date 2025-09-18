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