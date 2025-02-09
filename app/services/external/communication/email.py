from flask import current_app
from app.lib.helpers import request_helper

def send_email(from_email, recipients, subject, body, service_provider, template_id):
    url = current_app.config['END_POINTS']['communication-api']['email']
    payload = {
        "email": {
            "service_provider": service_provider,
            "template_id": template_id,
            "from": from_email,
            "to": recipients,
            "subject": subject,
            "template_data": {"$body$": body}
        }
    }
    request_helper.post(url, payload)
