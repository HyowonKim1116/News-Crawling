# 1. 필요한 라이브러리 import
import requests
from bs4 import BeautifulSoup

# 2. 키워드 입력 및 변수 선언
keyword = input(">>>> 뉴스 검색 키워드: ")
count = 0

# 3. 중첩 반복문을 이용한 기사 제목 크롤링
# 3-1) 첫 번째 반복문: 페이지마다 기사의 제목&날짜 크롤링
for page in range(1, 4):
    news_url = "https://search.hankyung.com/apps.frm/search.news?query=" + keyword + "&mediaid_clust=HKPAPER,HKCOM&page=" + str(page)

    raw = requests.get(news_url)
    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class':'article'})
    titles = box.find_all('em', {'class':'tit'})
    dates = box.find_all('span', {'class':'date_time'})

    # 3-2) 두 번째 반복문: 기사의 제목&날짜 출력
    for i in range(10):
        count += 1
        title = titles[i].text
        date = dates[i]
        print('%2d - [%s] %s' %(count, date.text, title.strip()))