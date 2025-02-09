import os
from app.services.external.communication.email import send_email
from app.exceptions.exception_notifier_helper import email_body, email_subject

def notify_exception(exception, params):
    from_email = os.getenv('EXCEPTION_EMAIL_SENDER')
    recipients = os.getenv('EXCEPTION_EMAIL_RECIPIENTS')
    service_provider = os.getenv('DEFAULT_EMAIL_SERVICE_PROVIDER')
    template_id = os.getenv('DEFAULT_EXCEPTION_TEMPLATE')

    subject = email_subject(exception)
    body = email_body(exception, params)

    try:
        response = send_email(from_email, recipients, subject, body, service_provider, template_id)
    except Exception as e:
        pass
        # logger.error("exception_notification.notify_exception - Failed with error", e)
