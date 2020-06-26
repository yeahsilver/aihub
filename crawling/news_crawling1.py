import requests
from bs4 import BeautifulSoup


def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    result = []
    
    div = soup.find("div", class_ = "list_issue")
    
    for a in div.find_all("a"):
        result.append(a.get_text())
        
    return result
    

def main() :
    url = "http://www.naver.com"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__" :
    main()

