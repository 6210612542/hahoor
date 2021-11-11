# Generated by Django 3.2.6 on 2021-11-11 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('content', markdownx.models.MarkdownxField()),
                ('seen', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='static/dormitorys/icon')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('report', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reviewto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormitory.dormitory')),
            ],
        ),
        migrations.AddField(
            model_name='dormitory',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='dormitory.Review'),
        ),
    ]
