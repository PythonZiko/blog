# Generated by Django 4.2.7 on 2023-12-04 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
        migrations.AddField(
            model_name='blog',
            name='avtor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='rasm',
            field=models.ImageField(help_text='Maqola uchun rasm', upload_to='blog_rasmlari/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='sarlavha',
            field=models.CharField(help_text='Bu yerga maqola sarlavhasini kiritasiz.', max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tanasi',
            field=models.TextField(help_text='Maqolaning matni.'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='vaqt',
            field=models.DateTimeField(help_text='Maqolaning vaqti'),
        ),
    ]
