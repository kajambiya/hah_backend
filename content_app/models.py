from django.db import models
from django.core.validators import MinValueValidator, DecimalValidator
from django.utils import timezone
from .validators import validate_image_size, validate_image_extension


class Episode(models.Model):
    link = models.TextField(
        max_length=150,
        help_text="Episode link"
    )
    guest_name = models.CharField(
        max_length=100,
        help_text="Guest name"
    )
    title = models.CharField(
        max_length=255,
        help_text="Episode title"
    )
    summarized_title = models.CharField(
        max_length=150,
        help_text="Summarized episode title"
    )
    description = models.TextField(
        help_text="Episode description"
    )
    img = models.ImageField(
        upload_to='episodes/%Y/%m',
        validators=[validate_image_size, validate_image_extension],
        help_text="Episode Image(JPG or PNG, max 1MB)"
    )
    pub_date = models.DateField(
        default=timezone.now,
        help_text="Published Date"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"

class Testimonial(models.Model):
    name = models.CharField(
        max_length=150,
        help_text="Name"
    )
    country = models.CharField(
        max_length=100,
        help_text="Country" 
    )
    img = models.ImageField(
        upload_to='testimonials/%Y/%m',
        validators=[validate_image_size, validate_image_extension],
        help_text="Testimonial Image(JPG or PNG, max 1MB)"
    )
    testimony = models.TextField(
        help_text="Testimonial Content"
    )
    testimony_date = models.DateField(
        default=timezone.now,
        help_text="Testimonial Date"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-testimony_date']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

class Book(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="Book Title"
    )
    author = models.CharField(
        max_length=150,
        help_text="Author Name"
    )
    description = models.TextField(
        help_text="Book Description"
    )
    summary = models.TextField(
        help_text="Book Summary"
    )
    img = models.ImageField(
        upload_to='books/%Y/%m',
        validators=[validate_image_size, validate_image_extension],
        help_text="Book Image(JPG or PNG, max 1MB)"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Book Price"
    )
    purchase_link = models.URLField(
        max_length=200,
        help_text="Purchase Link"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f'{self.title} by {self.author}'
    
class Event(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="Event Title"
    )
    host = models.CharField(
        max_length=150,
        help_text="Event Host"
    )
    description = models.TextField(
        help_text="Event Description"
    )
    price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0)],
    help_text="Event Price"
    )
    summary = models.TextField(
        help_text="Event Summary"
    )
    event_date = models.DateTimeField(
        help_text="Event Date & Time"
    )
    location = models.CharField(
        max_length=255,
        help_text="Event Location"
    )
    img = models.ImageField(
        upload_to='events/%Y/%m',
        validators=[validate_image_size, validate_image_extension],
        help_text="Event Image(JPG or PNG, max 1MB)"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-event_date']
        verbose_name = "Event"
        verbose_name_plural = "Events"
    
    def __str__(self):
        return f'{self.title} - {self.event_date.strftime("%Y-%m-%d")}'
    
class Partner(models.Model):
    name = models.CharField(
        max_length=150,
        help_text="Partner Name"
    )
    logo = models.ImageField(
        upload_to='partners/%Y/%m',
        validators=[validate_image_size, validate_image_extension],
        help_text="Partner Logo(JPG or PNG, max 1MB)"
    )
    website = models.URLField(
        max_length=200,
        help_text="Partner Website"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name