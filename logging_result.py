from google.cloud import logging

def logging_result(result):
    logging_client = logging.Client()
    log_name = "check_web_ssl_expire_remaining_days_log"
    logger = logging_client.logger(log_name)
    logger.log_text(result)
    print("Logged: {}".format(result))