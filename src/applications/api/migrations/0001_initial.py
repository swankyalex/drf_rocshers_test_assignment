# Generated by Django 3.2.16 on 2022-11-23 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('state', models.CharField(choices=[('Running', 'running'), ('Broken', 'broken')], default='Running', max_length=10)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_broke', models.DateTimeField(blank=True, null=True)),
                ('x', models.IntegerField(default=100)),
                ('y', models.IntegerField(default=100)),
                ('z', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pointer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axis', models.CharField(choices=[('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=1)),
                ('distance', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
