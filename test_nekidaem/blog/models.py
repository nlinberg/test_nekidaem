from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import EmailMessage


class Blog(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, blank=True, related_name='is_follower')

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('-author',)

    def __str__(self):
        return str(self.author.username)


@receiver(post_save, sender=User)
def create_user_blog(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(author=instance)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.ManyToManyField(User, related_name='is_viewed', blank=True)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('-created',)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=Post)
def notification_create_post(sender, instance, created, **kwargs):
    if created:
        blog = instance.blog
        recipient_list = User.objects.filter(email__gt='', is_follower=blog).values_list('email', flat=True)
        for _email in recipient_list:
            msg = EmailMessage('Notification: New post in blog',
                               'posts url: http://localhost:8016' + reverse('post-detail', kwargs={'pk': instance.pk}),
                               to=[_email])
            msg.send()
