from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('articles', 'Articles'), ('events', 'Events'), ('top_picks', "Editor's Top Picks"), ('art', 'Art')], db_index=True, max_length=16)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('author', models.CharField(blank=True, max_length=120)),
                ('published_at', models.DateField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True)),
                ('link_url', models.URLField(blank=True)),
                ('tags', models.CharField(blank=True, help_text='Comma-separated labels shown on the card.', max_length=255)),
                ('is_published', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ('display_order', '-published_at', '-id')},
        ),
    ]

