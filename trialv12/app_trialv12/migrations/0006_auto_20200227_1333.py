# Generated by Django 3.0.3 on 2020-02-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_trialv12', '0005_auto_20200227_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='jumlah_kasus',
            name='jumlah_baru_p',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jumlah_kasus',
            name='jumlah_lama_l',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jumlah_kasus',
            name='jumlah_lama_p',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
