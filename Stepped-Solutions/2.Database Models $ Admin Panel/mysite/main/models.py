# The first model we will start with is the tutorial series model, since tutorials are the main aspect of this website.
#But first we need to import the django.db.models package, which is necessary to access Django model functionality in the class definition. 
from django.db import models
#Our model class will then inherit from models dot Model where the class is named “TutorialSereis”
class TutorialSeries(models.Model):
	#For the model fields,we have series name,series summary,series image,3source code url,video url
	tutorial_series_name = 
	series_summary = 
	series_image = 
	source_code_url =
	video_url = 
	date_published =

	#Now from our models library,we will define the type of the field,so “models.CharField and then specify the max length by default,
	tutorial_series_name = models.CharField(max_length=200)
	#The next properties are series summary which is also a charfield,so ill just copy paste this
	series_summary = models.CharField(max_length=200)
	#series image is of image field,which ill comment for now for later use
	series_image =  models.ImageField()
	# source code and video are of url fields of max length of 200 characters
	source_code = models.URLField(max_length=200)
	video_url = models.URLField(max_length=200)
	# For the date_published,As the name suggests, this field is used to store an object of datetime created in python.
	# It will inherit a string of "date published" attribute,which will apply as its label.Also a default of the current datetime which is datetime.now() so we need to import datetime from datetime module
	from datetime import datetime
	date_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)
	

	# For all these properties, ill also add a true null attribute that allows us to make migrations when the field is empty,especially if it never existed in case of updates.
	# Also a true blank attribute to allow us to leave the field empty at any time. 
	tutorial_series_name = models.CharField(max_length=200,blank=True, null=True)
	series_summary = models.CharField(max_length=200,blank=True, null=True)
	source_code = models.URLField(max_length=200,blank=True, null=True)
	video_url = models.URLField(max_length=200,blank=True, null=True)
	date_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)	

#The second is the archives model,which is almost similar to the above,so ill copy paste this and change a few things,
# first is the title and descriptions which are also of Char Field,
# date published of datetime field,
# live demo url is of url field and image of image type.
# I’ll also comment the image attribute.

class Archive(models.Model):
	archive_title = models.CharField(max_length=200)
	archive_description = models.CharField(max_length=200)
	date_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)
	live_demo_url = models.CharField(max_length=200)
	#image = models.ImageField()


#The next is the subscription model,where it has an email field and date of subscription of datetime field
class Subscription(models.Model):
	email = models.EmailField(blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True )


#Starting of is the tutorial model where it will have a title of char field with max of 200 characters,tutorial content of text field.
# A char field and text field are completely different data types.If I may open the official documentation
# the tutorial will also need a date of publish of datetime field and a tutorial image 
class Tutorial(models.Model):
	#tutorial_series = 
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now(),blank=True, null=True)
	tut_image =  models.ImageField()


#Next is the comment having commentor field of char field,an email of email field,comment body of textfield and comment date of datetime field
class Comment(models.Model):
	#tutorial = 
	commentor_name = models.CharField(max_length=80,blank=True, null=True)
	commentor_email = models.EmailField(blank=True, null=True)
	comment_body = models.TextField(blank=True, null=True)
	comment_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

#Finally are the likes and dislike models.Whch for now will comment out.
# class Like(models.Model):
#      comment = 




# class Dislike(models.Model):
#     comment = 


#To change this we need to represent the model object as string value.so under each model,
# ill define the str method which  returns its respectful entity attribute.for tutorial series,
# it will return tutorial series,For tutorial it will return tutorial title,
# For archives it will return archive title,for comments it will return string of “comment by {} of {}-{}”….for subscription it will return email.
# If I refresh again,we observe the changes

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