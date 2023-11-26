# CarsForSelling Website

you can check all technologies in "requirements.txt" file.

User registration and authorization is implemented. For super-user there is a function of adding/deleting/modifying data
in the database (sqlite3). Using celery, obsolete records are deleted from the database daily (00:00 UTC). For all kinds
of users you can customize your personal account (change personal data and avatar), as well as view information about
cars from the catalog and take them for a test drive. Added sorting in the car catalog.

Running celery beat:

celery -A autoseller beat--loglevel=INFO

worker:

celery -A autoseller worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

