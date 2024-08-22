from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings

class BankName(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.ForeignKey(BankName, on_delete=models.CASCADE)
    bank_id = models.CharField(max_length=100)
    encrypted_password = models.BinaryField()  # Store the encrypted password

    def set_password(self, raw_password):
        cipher_suite = Fernet(settings.ENCRYPTION_KEY)
        self.encrypted_password = cipher_suite.encrypt(raw_password.encode('utf-8'))

    def get_password(self):
        cipher_suite = Fernet(settings.ENCRYPTION_KEY)
        return cipher_suite.decrypt(self.encrypted_password).decode('utf-8')
    
    def save(self, *args, **kwargs):
        # Encrypt the password before saving
        if self.encrypted_password:
            self.set_password(self.get_password())
        super().save(*args, **kwargs)