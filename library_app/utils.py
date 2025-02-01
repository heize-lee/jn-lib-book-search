import requests
from bs4 import BeautifulSoup

def get_call_numbers(query):
    base_url = "https://yslib.yeosu.go.kr/dls_kapi/index.php"
    params = {
        "mod": "wdDataSearch",
        "act": "searchResultList",
        "manageCode": "MA",
        "cn": "booksearch",
        "searchItem": "allitem",
        "searchWord": query,
    }

    # GET 요청
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("웹사이트에 접속할 수 없습니다.")

    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 결과 리스트 초기화
    results = []

    # 검색 결과 항목 선택
    book_items = soup.select("div.list")  # 검색 결과의 각 항목을 선택

    for item in book_items:
        try:
            # 책 제목
            title = item.find("dd").find("a").get_text(strip=True)


            # 청구기호
            call_number = item.find("strong", text="청구기호").find_next_sibling(text=True).strip()

            # 소장기관
            library = item.find("strong", text="소장기관").find_next("span").get_text(strip=True)

            # 대출 가능 여부
            status = item.find("strong", class_="using").get_text(strip=True)

            # 결과 추가
            results.append({
                "title": title,
                "call_number": call_number,
                "library": library,
                "status": status,
            })
        except AttributeError:
            # 데이터가 누락된 경우 해당 항목 건너뛰기
            continue

    # 디버깅 출력
    print("스크래핑 결과:", results)

    return results