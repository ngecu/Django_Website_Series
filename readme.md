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

![Test Image 1](admin_panel_view.png)
Hi guys,in this video will explore on ways we can customize the admin panel to allow us organize how this model is presented to us. It's not always the case that the order of the columns in the table is what we prefer.

Also we need to customize the tutorial content field into a text editor, for us to be able to write readable content having a blend of code snippets and media utilities like videos or images.So lets get started

---------------------------------------------------------------------------------


One thing my tutorials desperately could use is an editor, not really just some text field. I can write HTML in here, sure, but that would be rather tedious, especially if I made some error and then I wouldn't see it until I push to publish it! Instead, I would like a WYSIWYG ie.what you see is what you get) editor. Luckily many of these exist within the Django ecosystem. The one I will make use of is a branch off of TinyMCE. To get it, we just need to do:
```
pip3 install django-tinymce4-lite.
```
Now this is an app that will over-ride the text field type to make it more of an editor, so we need to add it to our INSTALLED_APPS in the mysite/mysite/settings.py file:
```
INSTALLED_APPS = (
    ...
    'tinymce',
    ...
)
```
The text editor will surely need some configurations,like the widgets to include,plugins,height,width,toolbar content,menubar or even status bar.So what ill do is copy paste the configuration.As you can see its just an object notation.If you like to follow up on these and many other features the text editor has to offer,link will be in the description
```
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
```
Next thing we need to do is to point our app to tinymce because our widgets will call upon tinymce to work

o do this, let's now edit mysite/mysite/urls.py
```
urlpatterns = patterns('',
    ...
    path('tinymce/', include('tinymce.urls')),
    ...
)
```
Finally, we just need to make use of TinyMCE where we want it. To do this, we need to override a form to use our TinyMCE widget. In this case, it's not just any form, however, we want to use it within the admin page. To do this, go back into our mysite/main/admin.py file, and add the follwowing imports:
```
from tinymce.widgets import TinyMCE
```
Then will add:
```
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
```
The first is for our widget, the second is so we can override one of our models fields (the textfield)

So ill refresh the admin panel page to execute the changes

Awesome! So this editor allows us to more easily write HTML, insert code snippets and many other things.We can also view the raw HTML and insert our own custom HTML as well if something we want doesn't exist in the editor.

While we're here, let's go ahead and add a quick tutorial with a code snippet just for kicks. Put whatever you want, give it a title, and save.

Let's now head back to our views to learn how our views can interact with our models, as well as how the Django templating works for displaying and working with python objects inside of HTML templates