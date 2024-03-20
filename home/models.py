from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    appointment = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='employees/', blank=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    twitter_profile = models.URLField(blank=True)
    facebook_profile = models.URLField(blank=True)
    instagram_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Skill(models.Model):
    name = models.CharField(max_length=50)
    progress = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Skills'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def clean(self):
        try:
            validate_email(self.email)
        except ValidationError as e:
            raise ValidationError({'email': 'Invalid email'}) from e
