import random
import string

from django.utils.text import slugify
from django.core.exceptions import ValidationError

from kavenegar import KavenegarAPI


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def validate_phone_number(value):

    sane = [
        '0','2','3','4','5','6','7','8','9','0','+',
        '۱','۲','۳','۴','۵','۶','۷','۸','۹','۰',
    ]
    for num in value:
        if num not in sane:
            raise ValidationError("شماره تلفن معقول وارد کنید")
    return value


# create producer and customer allowed mixins


#SEND OTP

def send_otp_kavenegar(params):
    api = KavenegarAPI('7A684663716F31777A3359794647744C69716E5470784530726E30366D4D6443554E584F5A4832374A57413D')
    api.sms_send(params)
    return None
