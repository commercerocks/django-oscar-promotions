# Generated by Django 2.2.14 on 2020-08-10 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oscar_promotions', '0010_auto_20200706_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automaticproductlist',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='handpickedproductlist',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='image',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='multiimage',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='rawhtml',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='singleproduct',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='tabbedblock',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
    ]