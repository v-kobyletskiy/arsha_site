from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(default=1)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Project Categories'

