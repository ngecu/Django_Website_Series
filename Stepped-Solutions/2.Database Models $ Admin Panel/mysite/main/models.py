from django.db import models
from datetime import datetime

class TutorialSeries(models.Model):
	tutorial_series_name = models.CharField(max_length=200,blank=True, null=True)
	series_summary = models.CharField(max_length=200,blank=True, null=True)
# 	series_image = models.URLField(max_length=200,blank=True, null=True)
	source_code = models.URLField(max_length=200,blank=True, null=True)
	video_url = models.URLField(max_length=200,blank=True, null=True)
	series_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series
	

class Archive(models.Model):
	archive_title = models.CharField(max_length=200)
	archive_description = models.CharField(max_length=200)
	archive_url = models.CharField(max_length=200)
	archive_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)
	image = models.URLField(max_length=200,blank=True, null=True)
	def __str__(self):
		return self.archive_title

class Subscription(models.Model):
	email = models.EmailField(blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True )


	def __str__(self):
		return self.email	
	
class Tutorial(models.Model):
	#tutorial_series = models.ForeignKey(TutorialSeries, on_delete=models.CASCADE,blank=True, null=True)
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)
	image = models.URLField(max_length=200,blank=True, null=True)
	
	def __str__(self):
		return self.tutorial_title


class Comment(models.Model):
	#tutorial = models.ForeignKey(TutorialSeries,on_delete=models.CASCADE,related_name='comments',blank=True, null=True)
	commentor_name = models.CharField(max_length=80,blank=True, null=True)
	commentor_email = models.EmailField(blank=True, null=True)
	comment_body = models.TextField(blank=True, null=True)
	comment_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)



	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment by {} of {}-{}'.format(self.name, self.email,self.created_on)


# class Like(models.Model):
#     comment = models.ForeignKey(Comment,null=True,on_delete=models.SET_NULL)

#     def __str__(self):
#         return str(self.comment)


# class Dislike(models.Model):
#     comment = models.ForeignKey(Comment,null=True,on_delete=models.SET_NULL)

#     def __str__(self):
#         return str(self.comment)




