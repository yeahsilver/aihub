import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    
    ul = soup.find("ul", class_ = "rvw_list_area")
    
    result = []
    
    for li in ul.find_all("li"):
        result.append(li.find("strong").get_text())
        
    return result
    


def main() :
    url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=168058#"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__" :
    main()

