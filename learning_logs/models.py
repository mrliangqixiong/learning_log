from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    # 用户学习主题
    text = models.CharField(max_length=200,verbose_name='内容')
    date_added = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner = models.ForeignKey(User)

    def __str__(self):
        # 返回模型的字符串
        return self.text


    # 定义条目 ,多个条目可以关联到同一个主题,多对一的关系
class Entry(models.Model):
    # 学习到的有关某个主题的具体知识
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # 外键关联
    topic = models.ForeignKey(Topic)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        # 返回模型的字符串表示,截取前50个字符显示
        return self.text[:50] + '...'



