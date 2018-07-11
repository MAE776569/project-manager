from django.db import models
from os import urandom
from time import time
import hmac
from hashlib import sha256

def get_salt():
    return urandom(16).hex()

def get_timestamp():
    return str(time())

class AccountVerification(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    verification_code = models.CharField(max_length=100, blank=True)
    salt = models.CharField(max_length=32, blank=True, default=get_salt)
    time_stamp = models.CharField(max_length=32, blank=True, default=get_timestamp)
    verified = models.BooleanField(blank=True, default=False)

    def get_verification_code(self):
        if not self.verification_code:
            verification_code = urandom(17).hex()
            hashed_code = hmac.new(
                str(self.salt).encode() + str(self.time_stamp).encode(),
                msg=str(verification_code).encode(),
                digestmod=sha256)
            self.verification_code = hashed_code.hexdigest()
            return verification_code
        else:
            raise ValueError("account already have a verification code")

    def verify_code(self, user_code):
        hashed_code = hmac.new(
                str(self.salt).encode() + str(self.time_stamp).encode(),
                msg=str(user_code).encode(),
                digestmod=sha256)
        return hmac.compare_digest(self.verification_code, hashed_code.hexdigest())

    class Meta:
        verbose_name = 'account verification'
        verbose_name_plural = 'accounts verification'