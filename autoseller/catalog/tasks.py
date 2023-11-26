from celery import shared_task
from django.utils import timezone
from .models import TestDrive
import logging

logger = logging.getLogger(__name__)


# удаляем прошедшие тест-драйвы
@shared_task
def delete_records():
    try:
        logger.info('Deleting records...')
        testdrives_to_delete = TestDrive.objects.filter(test_date__lt=timezone.now())
        testdrives_to_delete.delete()
        logger.info('Records deleted.')
    except Exception as e:
        logger.error(f'Error deleting records: {e}', exc_info=True)
