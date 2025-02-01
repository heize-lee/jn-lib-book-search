from django.shortcuts import render
from .utils import get_call_numbers

def scrape_and_save_call_numbers(request):
    query = request.GET.get('query', '')  # 검색어 입력 받기
    if not query:
        return render(request, 'library_app/scrape_form.html', {'error': '검색어를 입력해주세요.'})

    try:
        # 스크래핑 실행
        books = get_call_numbers(query)

        # 디버깅 출력
        print("뷰에서 전달할 데이터:", books)

        # 템플릿으로 데이터 전달
        return render(request, 'library_app/scrape_success.html', {'books': books})
    except Exception as e:
        # 오류 처리
        print("오류 발생:", e)
        return render(request, 'library_app/scrape_error.html', {'error': str(e)})
