import requests
from bs4 import BeautifulSoup

def get_href(soup) :
    # soup에 저장되어 있는 각 기사에 접근할 수 있는 href들을 담고 있는 리스트를 반환해주세요.
    ul = soup.find("ul", class_="list_news")
    
    result = []
    
    for span in ul.find_all('span', class_="tit"):
        result.append(span.find('a')["href"])
    
    return result

def main():
    list_href = []

    url = "https://sports.donga.com/ent?p=1&c=02"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    print(get_href(soup))


if __name__ == "__main__":
    main()
