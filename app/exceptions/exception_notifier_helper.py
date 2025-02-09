import os


def error_type():
    import sys
    return str(sys.exc_info()[0]).split(' ')[1].strip('>').strip("'")


def error_backtrace():
    import traceback
    return traceback.format_exc().replace(':', '<br>', 1).replace(',', '<br>', 1)


def email_body(exception, params):
    from datetime import datetime
    import socket
    body = f"""
    <b>ERROR:</b><br> {exception}<br><br>
    -------------------<br>
    <b>Data:</b><br>
    -------------------<br> 
    Timestamp: {datetime.now()}<br> 
    Hostname: {socket.gethostname()}<br>
    ErrorType: {error_type()}<br>
    MigrationType: {params.get('migration_type')}<br>"""
    if params.get('table'):
        body += f"Table: {params.get('table')}<br>"
    if params.get('project_id'):
        body += f"ProjectId: {params.get('project_id')}<br>"
    body += f"""-------------------<br>  
            <b>Backtrace:</b><br>  
            -------------------<br><br>  
            #{error_backtrace()}<br><br>  
            -------------------<br>"""

    return body


def email_subject(exception):
    subject = os.getenv("EXCEPTION_EMAIL_PREFIX") + " " + str(exception)
    return subject
