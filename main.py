import datetime
from datetime import datetime as dt
from check_cert_expire import *
from logging_result import logging_result

def main(event, context):
    cert = get_server_certificate('qiita.com')
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert.encode('utf-8'))
    today = datetime.date.today()
    not_before = dt.strptime(str(x509.get_notBefore())[2:16],'%Y%m%d%H%M%S') + datetime.timedelta(hours=9)
    not_after  = dt.strptime(str(x509.get_notAfter())[2:16],'%Y%m%d%H%M%S')  + datetime.timedelta(hours=9)
    #print(not_after)
    remaining = not_after - dt.now()
    remaining_days = remaining.days
    print (str(remaining_days) + ' days left')
    logging_result(str(remaining_days))
    