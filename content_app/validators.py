from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import os

def validate_image_size(image):
    max_size = 1 * 1024 * 1024  # 1MB
    if image.size > max_size:
        raise ValidationError(
            f'Image size should not exceed !MB. Current size: {image.size / (1024 * 1024):.2f}MB'
        )
    
def validate_image_extension(image):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(image.name)[1].lower()

    if ext not in valid_extensions:
        raise ValidationError(
            f'Only JPG and PNG files are allowed. You uploaded a file with extension {ext}'
        )