# Generated by Django 2.0.2 on 2018-12-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181101_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='heading',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='model_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='para1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='plan_of_attack',
            field=models.TextField(null=True),
        ),
    ]
