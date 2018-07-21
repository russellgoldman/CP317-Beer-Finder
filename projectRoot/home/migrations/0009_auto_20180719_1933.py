# Generated by Django 2.0.5 on 2018-07-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180713_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colourNum', models.IntegerField(default=0)),
                ('colourHex', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='beer',
            name='colourHex',
        ),
        migrations.AddField(
            model_name='beer',
            name='beerPhoto',
            field=models.ImageField(blank=True, upload_to='beers'),
        ),
        migrations.AddField(
            model_name='beer',
            name='colour',
            field=models.ManyToManyField(blank=True, to='home.Colour'),
        ),
    ]