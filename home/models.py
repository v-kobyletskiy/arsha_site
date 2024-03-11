from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Project Categories'


class Project(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='projects/', blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()

    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('position',)
        # constraints = [
        #     models.UniqueConstraint(fields=['position', 'category'], name='unique_position_per_each_category')
        # ]
        unique_together = ('id', 'slug')
