'''send email '''
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from auth.tokens import account_activation_token


def check_user_by_email(user, to_email, current_site):
    '''send confirmation email to user'''
    mail_subject = 'Activate your account'
    message = render_to_string('auth/active_email.html',
                               {
                                   'user': user,
                                   'domain': current_site.domain,
                                   'uid': str(urlsafe_base64_encode(force_bytes(user.pk)),
                                              encoding='utf-8'),
                                   'token': account_activation_token.make_token(user),
                               })

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()
