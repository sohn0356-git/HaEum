from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    name = models.CharField(max_length=20, verbose_name='이름')
    password = models.CharField(max_length=128, verbose_name='비밀번호')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'haeum user'
        verbose_name = '셀원'
        verbose_name_plural = '셀원'
