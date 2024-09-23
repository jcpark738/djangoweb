from django.db import models

# Create your models here.
class Program(models.Model):
    # id 작성하지 않으면 자동생성함
    id = models.AutoField(primary_key=True)
    # 제목
    title = models.CharField(max_length=200)
    # 내용
    maintext = models.TextField()
    # 서브텍스트
    subtext = models.CharField(max_length=200)
    # 스케줄
    schedule = models.CharField(max_length=200)
    # 이미지
    img = models.CharField(max_length=200)
    def __str__(self):
        return self.title