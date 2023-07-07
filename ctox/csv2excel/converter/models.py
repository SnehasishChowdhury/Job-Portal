from django.db import models

class Conversion(models.Model):
    csv_file = models.FileField(upload_to='csv_files/')
    excel_file = models.FileField(upload_to='excel_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversion {self.id}'
