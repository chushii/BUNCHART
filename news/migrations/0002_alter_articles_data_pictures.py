# Generated by Django 5.0.6 on 2024-06-12 13:33

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 12, 16, 33, 42, 98218), verbose_name='Дата публикации'),
        ),
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь')),
                ('data', models.DateTimeField(default=datetime.datetime(2024, 6, 12, 16, 33, 42, 99219), verbose_name='Дата публикации')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'картинки',
            },
        ),
    ]
