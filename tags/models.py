from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Tag(models.Model):
    label = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.label)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tagged_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='tagged_items')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    
#  App: likes

#LikedItem 
        # what user likes what object
        # user:  ForeignKey to User (django.contrib.auth.models)
        
class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='liked_items')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
        