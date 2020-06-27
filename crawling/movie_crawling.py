import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 1장 실습의 영화 리뷰 추출 방식과 동일합니다.
    ul = soup.find("ul", class_ = "rvw_list_area")
    
    result = []
    
    for li in ul.find_all("li"):
        result.append(li.find("strong").get_text())
        
    return result
    
def get_href(soup) :
    #검색 결과, 가장 위에 있는 영화로 접근할 수 있는 href를 반환하세요.
    ul = soup.find("ul", class_ = "search_list_1")
    # 여기에서 None이 뜸. 이유를 모르겠음. 
    a = ul.find("a")
    
    href = a['href'].replace('basic', 'review')
    
    return "https://movie.naver.com" + href

def get_url(movie) :
    # 입력된 영화를 검색한 결과의 url을 반환하세요.
    return f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=all"
    
def main() :
    list_href = []
    
    # 섹션을 입력하세요.
    movie = input('영화 제목을 입력하세요. \n  > ')
    
    url = get_url(movie)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    movie_url = get_href(soup)
    
    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")
    print(crawling(href_soup))
    


if __name__ == "__main__" :
    main()

