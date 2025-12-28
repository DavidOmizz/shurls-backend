from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import string, random
# from django.db import models

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortLink(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(
        max_length=10,
        unique=True,
        default=generate_code
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code
