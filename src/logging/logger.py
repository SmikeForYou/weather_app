import logging

from src.config import config

logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)