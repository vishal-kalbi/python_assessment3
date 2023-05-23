from django.db import models

# Create your models here.
class CommentApp(models.Model):
    postid=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    body=models.CharField(max_length=200)
          

# {
#     'postid':1,
#     'name':'vishal',
#     'email':'v@gmail.com',
#     'body':'very nice'
#  }         