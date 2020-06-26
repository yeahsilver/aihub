## BeautifulSoup 라이브러리

: HTML, XML, JSON 등 파일의 구문을 분석하는 모듈. 웹 페이지를 표현하는 HTML을 분석하기 위해 사용.



```python
soup = BeautifulSoup(open("index.html"), "html.parser")
# html.parser: BeautifulSoup 객체에게 "HTML을 분석해라" 라고 알려주는 의미
```

##### 

```python
# HTML 태그 추출
soup.find("p") # 처음 등장하는 태그 찾기 (한개)
soup.find_all("p") # 모든 태그 찾기 (리스트)
soup.find("div", class_ = "elice") # class가 elice인 div 찾기
soup.find("div", id = "elice") # id 매개변수의 값을 지정
soup.find("div", class_ = "elice").find("p") #div 태그 안에 있는 p 태그 추출
soup.find("div", class_ = "elice").find("p").get_text() # 태그가 가지고 있는 텍스트 추출
```



## Request 라이브러리

: Python에서 HTTP 요청을 보낼 수 있는 모듈

- GET 요청: 정보를 조회하기 위핸 요청 (예: 네이버 홈페이지에 접속한다. 구글에 키워드를 검색한다.)
- POST 요청: 정보를 생성, 변경하기 위한 요청 (예: 웹 사이트에 로그인한다. 메일을 삭제한다.)



```python
url = "http://ww.google.com"
result = requests.get(url) # 지정한 URL로 GET 요청 후 응답 저장.
print(result.status_code) # 요청의 결과 출력
print(result.text) # 웹사이트의 HTML 출력.
```

```python
soup = BeautifulSoup(result.text, "html.parser") # 웹페이지의 HTML 분석
```



