from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Completed','Completed'),
    )
    PRIORITY = (
        ('⭐','⭐'),
        ('⭐⭐','⭐⭐'),
        ('⭐⭐⭐','⭐⭐⭐'),
        ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10,choices=STATUS)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10,choices=PRIORITY)

    def __str__(self):
        return self.user.username
    



