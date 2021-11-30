from django.db import models
# third party import:
from sorl.thumbnail import ImageField


# allows us to create a simple way to store data in a database called feed_Post
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()

    # whatever the above text variable is, that is what the post will be called in the admin
    def __str__(self):
        return self.text
    