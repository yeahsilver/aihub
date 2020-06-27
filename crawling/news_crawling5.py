import requests
from bs4 import BeautifulSoup

    
def get_href(soup) :
    div_list = soup.find_all("div", class_="mduSubjectList")
    
    result = []
    
    for div in div_list:
        result.append("https:"+div.find('a')["href"])
        
    return result
    

def main() :
    list_href = []
    
    # href 수집할 사이트 주소 입력
    url = "https://news.nate.com/recent?mid=n0100"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup)
    
    print(list_href)


if __name__ == "__main__" :
    main()

