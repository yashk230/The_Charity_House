# Generated by Django 5.0.6 on 2024-08-09 18:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.IntegerField()),
                ('type', models.CharField(max_length=500)),
                ('items', models.CharField(max_length=5000)),
                ('Address', models.CharField(max_length=5000)),
                ('Status', models.CharField(default='UnResponded', max_length=50)),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.IntegerField()),
                ('Item', models.CharField(max_length=30)),
                ('Place', models.CharField(max_length=30)),
                ('Time', models.CharField(max_length=20)),
                ('Serving', models.CharField(max_length=50)),
                ('Expire', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=5000)),
                ('Status', models.CharField(default='UnResponded', max_length=50)),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.IntegerField(null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ngo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('n_id', models.ForeignKey(db_column='n_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ngo_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=5000)),
                ('category', models.CharField(max_length=30)),
                ('works', models.CharField(max_length=500)),
                ('awards', models.CharField(max_length=200)),
                ('pimage', models.ImageField(upload_to='ngo_images')),
                ('u_id', models.ForeignKey(db_column='u_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='connected_ngos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('n_id', models.ForeignKey(db_column='ngo', on_delete=django.db.models.deletion.CASCADE, to='myapp.ngo_details')),
            ],
        ),
        migrations.CreateModel(
            name='connected_donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ngo_id', models.ForeignKey(db_column='ngo', on_delete=django.db.models.deletion.CASCADE, to='myapp.ngo_details')),
            ],
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=5000)),
                ('d_id', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
