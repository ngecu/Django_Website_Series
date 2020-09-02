from django.db import models
from datetime import datetime
# Create your models here.

class TutorialSeires(models.Model):
    tutorial_series_name = models.CharField(max_length=200,blank=True,null=True)
    series_summary = models.CharField(max_length=200,blank=True,null=True)
    source_code_url = models.URLField(max_length=200,blank=True,null=True)
    video_url = models.URLField(max_length=200,blank=True,null=True)
    date_published = models.DateTimeField("date published",default=datetime.now(),blank=True,null=True)
    # series_image =  models.ImageField(,blank=True,null=True)

    def __str__(self):
        return self.tutorial_series_name


class Archives(models.Model):
    archive_title = models.CharField(max_length=200,blank=True,null=True)
    archive_description = models.CharField(max_length=200,blank=True,null=True)
    date_published = models.DateTimeField("date published",default=datetime.now(),blank=True,null=True)
    live_demo_url = models.URLField(max_length=200,blank=True,null=True)
    # series_image =  models.ImageField(,blank=True,null=True)

    def __str__(self):
        return self.archive_title


class Subscription(models.Model):
    email = models.EmailField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.email

class Tutorial(models.Model):
    # tutorial_series = 
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    date_published = models.DateTimeField("date published",default=datetime.now(),blank=True,null=True)
    # series_image =  models.ImageField(,blank=True,null=True)

    def __str__(self):
        return self.tutorial_title


class Comment(models.Model):
    # tutorial_series =
    commentor_name =  models.CharField(max_length=200)
    commentor_email = models.EmailField(blank=True,null=True)
    comment_body = models.TextField()
    comment_date = models.DateTimeField("comment date",default=datetime.now(),blank=True,null=True)
  
    def __str__(self):
       return 'Comment by {} of {}-{}'.format(self.commentor_name,self.commentor_email,self.comment_date)


#   class Like(models.Model):
#       comment =

    # def __str__(self):
    #     return self.comment


#   class DisLike(models.Model):
#       comment =

#   def __str__(self):
#         return self.comment
