# Generated by Django 4.1.7 on 2023-02-21 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=50, verbose_name='car number')),
                ('vin_number', models.CharField(max_length=50, verbose_name='vin number')),
                ('client', models.TextField(max_length=500, verbose_name='client name and surname')),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='brand')),
                ('model', models.CharField(max_length=50, verbose_name='model')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_sum', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_cars.car')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_cars.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_cars.service')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_lines',
            field=models.ManyToManyField(to='main_cars.orderline'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car', to='main_cars.cartype', verbose_name='car type'),
        ),
    ]