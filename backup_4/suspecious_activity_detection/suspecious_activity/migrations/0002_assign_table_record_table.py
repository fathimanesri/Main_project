# Generated by Django 3.2.24 on 2024-02-22 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suspecious_activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='record_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('policeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suspecious_activity.police_table')),
            ],
        ),
        migrations.CreateModel(
            name='assign_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('policeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suspecious_activity.police_table')),
            ],
        ),
    ]
