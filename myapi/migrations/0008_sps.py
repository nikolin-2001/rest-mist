# Generated by Django 4.0.1 on 2022-01-05 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pzh', models.CharField(max_length=200)),
                ('sps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.pk')),
            ],
        ),
    ]