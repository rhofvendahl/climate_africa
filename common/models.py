from django.db import models
from django.contrib.auth.models import User # unsure how to do this with string, my preference
# from cities_light.abstract_models import AbstractCity, AbstractRegion, AbstractCountry
# from cities_light.receivers import connect_default_signals (not necessary at this time)
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# ensures that multiple posts can upload same images without backblaze grouping them.
def image_upload_path(instance, filename):
    # return f'post-images/{instance.post.id}/{filename}'
    return f'users/{instance.post.user.id}/posts/{instance.post.id}/images/{filename}'

# Refactor idea: change to PostImage, to mesh with ProfileImage
class Image(models.Model):
    post = models.ForeignKey('common.Post', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_path)
    order_in_post = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'ID: {self.id}, post title: {self.post.title}'

@receiver(post_delete, sender=Image)
def remove_file_from_cloud(sender, instance, using, **kwargs):
    instance.image.delete(save=False)

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    text = models.TextField()
    tags = models.ManyToManyField('common.Tag', related_name='users')
    city = models.ForeignKey('cities_light.City', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    @property
    def all_images(self):
        return self.image_set.all()

    @property
    def first_image(self):
        return self.image_set.order_by('order_in_post').first()


    @property
    def n_supporters(self):
        return self.supporters.count()

    def __str__(self):
        return f'ID: {self.id}, title: {self.title}'

class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    is_starter = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'ID: {self.id}, name: {self.name}, is_starter: {str(self.is_starter)}'

# would be better to have abstract w subclasses, but tricky with existing migrations
# for now profile will have fields for organizations alongside fields for people profiles
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.ForeignKey('cities_light.City', on_delete=models.PROTECT, null=True, blank=True) # change to required later
    is_organization = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True) # suggested for orgs, maybe people too
    website = models.CharField(max_length=160, null=True, blank=True) # suggested for organizations
    # birthday, required for people

    @property
    def n_supporters(self):
        return self.user.supporters.count()

    def __str__(self):
        return f'ID: {self.id}, username: {self.user.username}'

    # might not need to be part of this class
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # might not need to be part of this class
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

# class OrganizationInfo(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     website = models.CharField(max_length=160, null=True, blank=True)

def user_image_upload_path(instance, filename):
    return f'users/{instance.user.id}/user_image/{filename}'

class UserImage(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_image_upload_path)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'ID: {self.id}, username: {self.user.username}'

class Support(models.Model):
    supporter = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='supports_made')
    supported_post = models.ForeignKey('common.Post', on_delete=models.CASCADE, null=True, blank=True, related_name='supporters')
    supported_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, related_name='supporters')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    @property
    def for_post(self):
        return self.supported_post != None

    @property
    def for_user(self):
        return self.supported_user != None

    def __str__(self):
        if self.for_post and self.for_user:
            return f'ID: {self.id}, supporter: {self.supporter.username}, ERROR support has post AND user. Post: {self.supported_post.title}; user: {self.supported_user.username}'
        elif self.for_post:
            return f'ID: {self.id}, supporter: {self.supporter.username}, supported post title: {self.supported_post.title}'
        elif self.for_user:
            return f'ID: {self.id}, supporter: {self.supporter.username}, supported user username: {self.supported_user.username}'
        else:
            return f'ID: {self.id}, supporter: {self.supporter.username}, ERROR support has neither supported post nor supported user.'
