from django.db import models

# Create your models here.

# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)

#     def __str__(self):
#         return self.full_name

class Article(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to = "images/%y")

    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic 
        