from django.db import models
from ums.models import Users
import os
from django.conf import settings


class DocumentTemplate(models.Model):
    """Model to store LaTeX templates for PDF generation"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    latex_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GeneratedDocument(models.Model):
    """Model to store generated PDF documents with signature information"""
    title = models.CharField(max_length=200)
    template = models.ForeignKey(DocumentTemplate, on_delete=models.PROTECT)
    created_by = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='created_documents')
    signed_by = models.ManyToManyField(Users, through='DocumentSignature')
    file_path = models.CharField(max_length=255)
    context_data = models.JSONField(default=dict)  # Stores data used to generate the PDF
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_file_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.file_path)


class DocumentSignature(models.Model):
    """Model to track document signatures"""
    document = models.ForeignKey(GeneratedDocument, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    signature_data = models.TextField()  # Base64 encoded signature image or digital signature data
    timestamp = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.document.title} signed by {self.user.name} at {self.timestamp}"
