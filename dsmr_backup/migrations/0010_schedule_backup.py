# Generated by Django 3.0.4 on 2020-03-29 21:20

from django.db import migrations
from django.conf import settings


def migrate_forward(apps, schema_editor):
    ScheduledProcess = apps.get_model('dsmr_backend', 'ScheduledProcess')
    BackupSettings = apps.get_model('dsmr_backup', 'BackupSettings')

    backup_settings, _ = BackupSettings.objects.get_or_create()
    ScheduledProcess.objects.create(
        name='Create daily backup',
        module=settings.DSMRREADER_MODULE_DAILY_BACKUP,
        active=backup_settings.daily_backup
    )


def migrate_backward(apps, schema_editor):
    ScheduledProcess = apps.get_model('dsmr_backend', 'ScheduledProcess')
    ScheduledProcess.objects.filter(module=settings.DSMRREADER_MODULE_DAILY_BACKUP).delete()


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ('dsmr_backup', '0009_compression_level'),
    ]