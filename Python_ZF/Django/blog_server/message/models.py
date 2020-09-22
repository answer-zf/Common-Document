from django.db import models

# Create your models here.
from topic.models import Topic
from user.models import UserProfile


class Message(models.Model):
    content = models.CharField(verbose_name="留言内容", max_length=100)
    create_time = models.DateTimeField()
    user = models.ForeignKey(UserProfile)
    topic = models.ForeignKey(Topic)
    parent_id = models.CharField(verbose_name="父留言", max_length=10, null=True)

    class Mete:
        db_table = "message"
