from django.db import models
# 먼가 처리된 이미지 필드
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Feed(models.Model):
    content = models.CharField(max_length=150) 
    created_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(
            # 어떤 처리
            processors= [ResizeToFill(300, 300)],
            #어떤 확장자
            format='JPEG',
            options={'quality':90},
            # 어디 위치(앱별로 구분하기 위해)
            upload_to='feeds'
    )