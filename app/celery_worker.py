"""
Celery worker module
contains celery tasks
"""

import requests
from celery import Celery
from celery.utils.log import get_task_logger

from app.config import URL

celery = Celery("tasks", broker="amqp://guest:guest@127.0.0.1:5672//")
celery_log = get_task_logger(__name__)


@celery.task
def request_data() -> list[dict]:
    """
    Request from epic store
    :return: list[dict]
    """
    request = requests.get(URL)
    data = request.json()
    data = data["data"]["Catalog"]["searchStore"]["elements"]

    def is_correct_data(dict_data: dict) -> bool:
        return dict_data["promotions"]

    filtered_data = list(filter(is_correct_data, data))
    celery_log.info("Request from epic api complete")
    return filtered_data
