from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    text = models.TextField(verbose_name="Tekst")
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Data")
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Data publikacji")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200, verbose_name="Autor")
    text = models.TextField(verbose_name="Tekst")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data")
    approved_comment = models.BooleanField(default=False, verbose_name="Potwierdzony komentarz")

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"
