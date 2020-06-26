import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    
    result = []
    
    dd_list = soup.find_all("dd", class_ = "usertxt")
    
    for dd in dd_list:
        result.append(dd.get_text().replace('\t','').replace('\n',''))
    
    return result


def main() :
    url = "https://pann.nate.com/talk/350939697"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__" :
    main()

