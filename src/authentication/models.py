from django.db import models
from os import urandom
import hmac
from hashlib import sha256
from uuid import uuid4

def get_salt():
    return urandom(16).hex()

HASH_SEPARATOR = b'#'

class AccountVerification(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    verification_code = models.CharField(max_length=64, blank=True)
    salt = models.CharField(max_length=32, unique=True, blank=True, default=get_salt)
    uuid = models.UUIDField(unique=True, blank=True, default=uuid4)
    is_verified = models.BooleanField(blank=True, default=False)
    is_registered = models.BooleanField(blank=True, default=False)

    def get_verification_code(self):
        if not self.verification_code:
            verification_code = urandom(32).hex()
            user_msg = self.salt.encode() + HASH_SEPARATOR + self.verification_code.encode()
            hashed_user_code = hmac.new(
                str(self.uuid).encode(),
                msg=user_msg,
                digestmod=sha256)
            hashed_user_code = hashed_user_code.hexdigest()
            msg = self.salt.encode() + HASH_SEPARATOR + hashed_user_code.encode()
            saved_code = hmac.new(
                str(self.uuid).encode(),
                msg=msg,
                digestmod=sha256)
            self.verification_code = saved_code.hexdigest()
            self.save()
            #get that once the verification account is created
            return hashed_user_code
        else:
            raise ValueError("account already have a verification code")

    def verify_code(self, user_code):
        user_msg = self.salt.encode() + HASH_SEPARATOR + user_code.encode()
        hashed_code = hmac.new(
                str(self.uuid).encode(),
                msg=user_msg,
                digestmod=sha256)
        return hmac.compare_digest(self.verification_code, hashed_code.hexdigest())

    class Meta:
        db_table = 'account_verification'
        verbose_name = 'account verification'
        verbose_name_plural = 'accounts verification'

    def __str__(self):
        return self.email