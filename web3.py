# web3.py
# 웹서버에 요청
import urllib.request
# 문자열 검색해서 크롤링
from bs4 import BeautifulSoup

#  정규 표현식
import re

# 문자열 리턴
# 웹브라우저의 헤더 셋팅
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

# 페이징 처리가 추가되는 경우
# http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=2
for i in range(1,11):
    url = "http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=" \
        + str(i)
    print(url)
    req = urllib.request.Request(url, headers = hdr)
    data = urllib.request.urlopen(req).read()
    page = data.decode('utf-8', 'ignore')
    soup = BeautifulSoup(page, "html.parser")

        # 	<td class="subject">
        #   <a href="/board/view.php">한국에서 이름을 잃어버린 이탈리아 과자</a>
        #   </td>

    lst = soup.find_all("td", attrs={"class":"subject"}) # class가 subject로 되어있는 것만 갖고와라.
    for item in lst:
        title = item.find("a").text # a태그 하나만 검색하고 하이퍼링크를 없애라
        if re.search("박수홍", title):
            print(title.strip()) # 공백문자 없애라

