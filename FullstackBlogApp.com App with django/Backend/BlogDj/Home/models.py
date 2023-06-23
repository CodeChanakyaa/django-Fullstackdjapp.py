from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=400)
    added_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
