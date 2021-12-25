import socket
import ssl
import OpenSSL


def get_server_certificate(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as sslsock:
            der_cert = sslsock.getpeercert(True)
            return ssl.DER_cert_to_PEM_cert(der_cert)