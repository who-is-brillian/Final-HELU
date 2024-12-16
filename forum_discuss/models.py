from django.db import models
from django.contrib.auth.models import User



class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Judul")
    description = models.TextField(verbose_name="Deskripsi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat pada")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Dibuat oleh")
    image = models.ImageField(upload_to='topic_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Terakhir diperbarui pada")
    likes = models.ManyToManyField(User, related_name='liked_topics', blank=True)
    unlikes = models.ManyToManyField(User, related_name='unliked_topics', blank=True)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()

    class Meta:
        verbose_name = "Topik"
        verbose_name_plural = "Topik-topik"
        ordering = ['-created_at']  # Mengurutkan topik berdasarkan waktu pembuatan terbaru


class Post(models.Model):
    topic = models.ForeignKey(
        Topic,
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name="Topik"
    )
    content = models.TextField(verbose_name="Konten")
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE,
        verbose_name="Balasan dari"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat pada")
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Dibuat oleh"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Terakhir diperbarui pada")

    def __str__(self):
        return f"Post oleh {self.created_by} di {self.topic.title}"

    class Meta:
        verbose_name = "Postingan"
        verbose_name_plural = "Postingan-postingan"
        ordering = ['created_at']  # Mengurutkan postingan berdasarkan waktu pembuatan

    @property
    def is_reply(self):
        """
        Mengembalikan True jika postingan adalah balasan, False jika bukan.
        """
        return self.parent is not None

    def get_all_replies(self):
        """
        Mengembalikan semua balasan dari postingan ini secara rekursif.
        """
        replies = []
        for reply in self.replies.all():
            replies.append(reply)
            replies.extend(reply.get_all_replies())
        return replies
