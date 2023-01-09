# Generated by Django 4.1 on 2022-09-12 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pages', '0002_alter_pages_author_alter_pages_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
