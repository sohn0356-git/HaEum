from django.db import models
from datetime import datetime
import os, uuid

DISCLOSURE_CHOICES = (
    (0, 'private'),
    (1, 'public')
)

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE,
                               verbose_name='글쓴이')
    disclosure = models.SmallIntegerField(choices=DISCLOSURE_CHOICES)
    hits = models.IntegerField(default=0, verbose_name='조회수')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'haeum board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'

class Post_thanks(models.Model):
    contents = models.TextField(verbose_name='내용')
    image_url = models.CharField(max_length=30, verbose_name='이미지url')
    writer = models.ForeignKey('post.board', on_delete=models.CASCADE,
                               verbose_name='게시글')
    class Meta:
        db_table = 'haeum thanks'
        verbose_name = '감사열매'
        verbose_name_plural = '감사열매'

def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(instance.UPLOAD_PATH, "%s.%s" % (uuid.uuid4(), ext))
    #16자리 고유한 아이디 생성

class Photo(models.Model):
    UPLOAD_PATH = 'user-upload'
    title = models.CharField(max_length=30, verbose_name='제목')
    image = models.ImageField(upload_to=image_upload_to)
    order = models.SmallIntegerField() # image numbering
    reg_date = models.DateTimeField(verbose_name='날짜', default=datetime.now())

    class Meta:
        db_table = 'haeum photo'
        verbose_name = '사진'
        verbose_name_plural = '사진'
        ordering = ['order']

class Board_thanks(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE,
                               verbose_name='글쓴이')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'thanks board'
        verbose_name = '감사노트'
        verbose_name_plural = '감사노트'