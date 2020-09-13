hi guys,welcome to your third django tutorial.

In this video will be dealing with data association and linking.

We will find out how we can associate some tutorials and comments to a tutorial series,some likes and dislikes to a comment.

Django models operate by on relational database systems so they support relationships among one another.

 The database relationships are used to associate records on the basis of a key or id, resulting in improved data maintenance, query performance, and less duplicate data, among other things.
 
 Django models support the same three relationships supported by relational database systems: one to many, many to manym and one to one.

For our case we will specifically dwell on the one to many relationship since its the one we will be applying on our database.

A one to many relationship implies that one model record can have many other model records associated with itself.

Take the example we highlighted in the previous video on tv show how to get away with murder.The show has 6 seasons,each seasons having a list of 10 episodes.

That illustrates the one to many relationship where one season has many episodes.

Coming back to our theory,the tutorial series class needs to be linked to several tutorials and comments and the comment class linked to likes and dislikes.

-------------------------------------------------------------------------
Alright,so in the last video,what we did is create our basic model tables.Now in this video we want to create relationships between these models.

So how are going to do this? 

Well,to define a one to many relationship in Django models you use the ForeignKey data type on the model that has the many records as a model field.
```
tutorial_series = models.ForeignKey()
```

The models.ForeignKey() definition creates the one to many relationship, where the first argument indicates the relationship model.

For our case is Tutorial series
```
tutorial_series = models.ForeignKey(TutorialSeries)
```
So,ill go ahead and set the null and blank value to true since we dont want to have any issues when adding items to our database.
```
tutorial_series = models.ForeignKey(TutorialSeries,null=True,blank=True)
```
The last thing we need to do on this foreign key is to add an on_delete method.

And what this is,is basically saying that whenever a series is deleted,what do we do with the tutorial child?

In this case,ill just say on_delete,models.CASCADE.
```
tutorial_series = models.ForeignKey(TutorialSeries, on_delete=models.CASCADE,blank=True, null=True)
```
So what this does is,when the referenced object is deleted,also delete the objects that have references to it.

Now ill just go ahead and copy past this to the rest of the necessary model classes
```


class Comment(models.Model):
	tutorial = models.ForeignKey(TutorialSeries,on_delete=models.CASCADE,blank=True, null=True)

	def __str__(self):
		return 'Comment by {} of {}-{}'.format(self.name, self.email,self.created_on)


class Like(models.Model):
    comment = models.ForeignKey(Comment,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.comment)


class Dislike(models.Model):
    comment = models.ForeignKey(Comment,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.comment)
```
If you remember on the prevous video,i had commented out the like and dislike models on admin.py.

So i'll first uncomment them out.

In order to make this work,lets go ahead and run the migrations,so :
```
python3 manage.py makemigrations
```
The migrations are made,lets go ahead and run the migrations now,
```
python3 manage.py migrate
```
Ok,so that just created the relationship,lets relaunch our server to test it out on our admin panel.

So if i create a new tutorial,you can see up here i can select a series to associate with.It list the available series in the database.This is so since we have set the tutorial must be associated with the series model.
Yeah,that's it for this video.Thanks for watching.