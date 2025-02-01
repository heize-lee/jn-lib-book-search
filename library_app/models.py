from django.db import models

class BookCallNumber(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)  # 책 제목
    call_number = models.CharField(max_length=100)  # 청구번호
    library = models.CharField(max_length=100, blank=True, null=True)  # 소장 기관
    status = models.CharField(max_length=50, blank=True, null=True)  # 대출 가능 여부
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터 저장 시간

    def __str__(self):
        return f"{self.title} ({self.call_number})"
