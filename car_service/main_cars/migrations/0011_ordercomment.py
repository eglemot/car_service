# Generated by Django 4.1.7 on 2023-03-01 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_cars', '0010_car_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('comment', models.TextField(max_length=4000, verbose_name='comment')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_cars.order', verbose_name='order')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_comments', to=settings.AUTH_USER_MODEL, verbose_name='client')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]