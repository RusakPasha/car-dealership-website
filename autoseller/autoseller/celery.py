from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoseller.settings')

app = Celery('autoseller')

app.config_from_object('django.conf:settings', namespace='CELERY')

# автоматическое обнаружение и регистрация задач из приложений Django
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'delete_records_task': {
        'task': 'catalog.tasks.delete_records',
        'schedule': crontab(hour=21, minute=0),
    },
}

# ЗАПУСК БИТА celery -A autoseller beat --loglevel=INFO
# ЗАПУСК ВОРКЕРА celery -A autoseller worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

# --without-gossip: Отключает использование протокола Gossip для обмена информацией между рабочими процессами.

# --without-mingle: Отключает начальный объединенный хук, который вызывается после того, как все рабочие процессы инициированы.

# --without-heartbeat: Отключает проверку состояния сердца (heartbeat), которая позволяет обнаруживать зависание или другие проблемы с рабочими процессами.

# -Ofair: Означает, что для выравнивания нагрузки будет использоваться стратегия fair, которая позволяет избежать простаивания рабочих процессов и обеспечивает справедливое распределение задач.

# --pool=solo: Использует встроенный пул потоков solo. В нем каждая задача выполняется в своем собственном потоке, что позволяет избежать возможных взаимоблокировок между задачами.