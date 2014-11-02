from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Description(models.Model):
	title = models.CharField(max_length=120)
	text = models.TextField(null=True, blank=True) #text feilds dont need max length
	slug = models.SlugField(unique=True) #what is a slug??
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #tells you when field is first created
	updated = models.DateTimeField(auto_now_add=False, auto_now=True) #tells you when field is changed
	active = models.BooleanField(default=False)
        rank = models.IntegerField()

	class Meta:
		unique_together = ('title', 'slug')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("memoir", kwargs={"slug": self.slug})
        def get_slug(self):
            return self.slug

class DescriptionImage(models.Model):
	description = models.OneToOneField(Description)
	image = models.ImageField(upload_to='content_manager/images/')
	thumbnail = models.BooleanField(default=False)
        timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #tells you when field is first created
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return self.description.title
        




