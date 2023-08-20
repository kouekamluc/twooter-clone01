from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
# Create your models here.



class Post(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    
    def __str__(self):
        return self.content[:5]
    
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    
    

class Comment(models.Model):
    content = models.TextField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True) 
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post , on_delete=models.CASCADE)
    
    
class Preference(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)   
    post = models.ForeignKey(Post , on_delete=models.CASCADE)   
    value = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.user) + ':' + str(self.post) + ':' + str(self.value)
    
    
    class Meta:
        unique_together = ("user" , "post" , "value")