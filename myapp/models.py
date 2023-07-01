from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


class PostStats(models.Model):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="post_stats"
    )
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post.title

