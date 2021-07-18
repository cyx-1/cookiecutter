import logging
import sys


def configure_logging():
    FORMAT = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    logging.basicConfig(format=FORMAT, datefmt='%Y-%m-%d:%H:%M:%S', stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("hello")
