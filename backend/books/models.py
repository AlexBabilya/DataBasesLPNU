from django.db import models
from authors.models import Author
from publishers.models import Publisher


class Book(models.Model):
    title = models.CharField(max_length=55, db_index=True)
    isbn = models.CharField(max_length=13, unique=True, db_index=True)
    publication_date = models.DateField(db_index=True)
    price = models.FloatField(db_index=True)
    author = models.ManyToManyField(Author)
    publisher= models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    cover = models.ImageField()
    about = models.TextField(blank=True, null=True)
    page_count = models.PositiveSmallIntegerField()
    rating = models.FloatField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-title"]

    def __str__(self):
        return f"{self.title}" 

