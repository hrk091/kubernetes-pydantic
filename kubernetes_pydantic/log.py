import logging

logger = logging.getLogger("k8s-pydantic")

LOG_FORMAT = "%(asctime)s %(levelname)8s %(filename)s:%(lineno)s - %(message)s"
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(handler)
