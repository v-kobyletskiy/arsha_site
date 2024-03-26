from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField


class ProjectCategory(models.Model):
    """
       A model representing category for projects.
       Attributes:
           name (models.CharField): The name of the project category.
               Must be unique and have a maximum length of 50 characters.
           slug (models.SlugField): The slug representation of the project category name.
               Must be unique, have a maximum length of 50 characters, and is indexed in the database.
           position (models.SmallIntegerField): The position or order of the project category.
               Must be unique.
           is_visible (models.BooleanField): A boolean indicating whether the project category is visible or not.
    """
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
    """
       A model representing a project.
       Attributes:
           name (models.CharField): The name of the project.
           slug (models.SlugField): The slug representation of the project name.
           description (models.TextField): The description of the project.
           photo (models.ImageField): The photo associated with the project.
           is_visible (models.BooleanField): A boolean indicating whether the project is visible or not.
           position (models.SmallIntegerField): The position or order of the project.
           category (models.ForeignKey): The category that the project belongs to.
               This is a foreign key reference to the ProjectCategory model.
    """
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
    """
      A model representing an employee.
      Attributes:
          name (models.CharField): The first name of the employee.
          surname (models.CharField): The last name or surname of the employee.
          appointment (models.CharField): The job title or appointment of the employee.
          description (models.TextField): A description or bio of the employee.
          photo (models.ImageField): The photo or image associated with the employee.
          position (models.SmallIntegerField): The position or order of the employee.
          is_visible (models.BooleanField): A boolean indicating whether the employee is visible or not.
          twitter_profile (models.URLField): The URL of the employee's Twitter profile.
          facebook_profile (models.URLField): The URL of the employee's Facebook profile.
          instagram_profile (models.URLField): The URL of the employee's Instagram profile.
          linkedin_profile (models.URLField): The URL of the employee's LinkedIn profile.
    """
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
    """
       A model representing company skill.
       Attributes:
           name (models.CharField): The name of the skill.
           progress (models.SmallIntegerField): A numerical value representing the progress or proficiency level of the skill.
           position (models.SmallIntegerField): The position or order of the skill.
           is_visible (models.BooleanField): A boolean indicating whether the skill is visible or not.
    """
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
    """
       A model representing a message form user.
       Attributes:
           name (models.CharField): The name of the person submitting the message.
           email (models.EmailField): The email address of the person submitting the message.
           subject (models.CharField): The subject or title of the message.
           message (models.TextField): The body or content of the message.
           is_processed (models.BooleanField): A boolean indicating whether the message has been processed or not.
           created_at (models.DateTimeField): The date and time when the message was created or submitted.
           updated_at (models.DateTimeField): The date and time when the message was last updated.
    """
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


class GeneralInfo(models.Model):
    """
       A model representing general information about company.
       Attributes:
           address (RichTextField): The address or location of the entity.
           phone (models.CharField): The phone number.
           email (models.EmailField): The email address.
           twitter (models.URLField): The URL of the Twitter profile.
           facebook (models.URLField): The URL of the Facebook profile.
           instagram (models.URLField): The URL of the Instagram profile.
           linkedin (models.URLField): The URL of the LinkedIn profile.
    """
    address = RichTextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'General Info'


class FrequentlyQuestion(models.Model):
    """
       A model representing a frequently asked question (FAQ).
       Attributes:
           question (models.TextField): The text of the frequently asked question.
           answer (models.TextField): The text of the answer to the question.
           position (models.SmallIntegerField): The position or order of the FAQ.
           is_visible (models.BooleanField): A boolean indicating whether the FAQ is visible or not.
    """
    question = models.TextField()
    answer = models.TextField()
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class Service(models.Model):
    """
       A model representing a service offered by company.
       Attributes:
           title (models.CharField): The title or name of the service.
           description (models.TextField): A description or details about the service.
           position (models.SmallIntegerField): The position or order of the service.
           is_visible (models.BooleanField): A boolean indicating whether the service is visible or not.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class Subscriber(models.Model):
    """
       A model representing a subscriber who has subscribed newsletter.
       Attributes:
           email (models.EmailField): The email address of the subscriber.
           is_active (models.BooleanField): A boolean indicating whether the subscriber is active.
           username (models.CharField): The username associated with the subscriber.
    """
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=255)
