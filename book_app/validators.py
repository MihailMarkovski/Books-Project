from django.core.exceptions import ValidationError


def clean_pages(self):
    pages = self.cleaned_data['pages']
    if pages <= 0:
        raise ValidationError('Pages shout be with positive number!')

    return pages