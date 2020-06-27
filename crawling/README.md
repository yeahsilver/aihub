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



## Query

- 각 페이지의 URL에서 p=(숫자) 부분이 일정 숫자만큼 증가함. 이때 여러 페이지를 크롤링하기 위해서 아래의 방법을 취함. 

```python
# 예) 숫자가 1부터 시작해서 20씩 증가하는 URL (Query를 사용하지 않았을 경우)
# 문자열 연산으로 처리하여 새로운 URL을 얻음.
for in range(0, 5):
	url = "http://sports.donga.com/Enter?p="+st((i*20+1))
```

- 쿼리를 이용하면 더욱 효과적으로 작업 수행 가능.



 #### Query

: 웹 서버에 GET 요청을 보낼 때, 조건에 맞는 정보를 표현하기 위한 변수.

예) 번호가 1번인 학생을 보여줘라 / 전체 기사 중 페이지가 21일 기사들을 보여줘라.



#### requests 라이브러리

: request의 get 메소드로 GET 요청을 보낼 때 params 매개변수에 딕셔너리를 전달함으로써 쿼리를 지정할 수 있음.

```python
url = "https://www.google.com/search"
result = request.get(url, params ={'q':'elice'}})
```



## Tag attributes

```html
<div class = "elice" id = "title">제목</div>
// 이때 div는 태그, class, id는 속성.
<a href="https...">기사제목</a> // 이동할 URL을 href 속성에 삽입.
```

```python
div = soup.find("div")
print(div.attrs) # 태그의 속성 출력
print(div['class']) # attrs 딕셔너리의 키로 인덱싱하여 태그의 속성에 접근 가능.

a = soup.find("a")
href_url = a["href"] # 하이퍼링크의 URL 얻기.
```



## Children, Name

- Children: 어떤 태그가 포함하고 있는 태그
- Name: 어떤 태그의 이름을 의미하는 속성.

```html
<div>
	<span></span>
	<p></p>
</div>
// 이때 div가 포함하고 있는 span, p 태그가 children!
```

```python
# div 태그에 포함된 태그들의 리스트 얻기.
soup.find("div").children 

# 태그의 이름 출력.
children = soup.find("div").children
for child in children:
  print(child.name) 
```





