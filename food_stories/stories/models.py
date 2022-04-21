from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()


class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbsrtactModel):
    SUBJECT_CHOICES = (
        (1, 'Sayt islemir'),
        (2, 'Menimle elaqe saxlayin'),
    )
    name = models.CharField('Ad', max_length=50)
    email = models.EmailField('E Poct', max_length=40)
    subject = models.SmallIntegerField('Movzu', choices=SUBJECT_CHOICES)
    message = models.TextField('Mesaj', help_text='Buraya mesajinizi yazin')

    def __str__(self):
        return self.name


class Category(AbsrtactModel):
    title = models.CharField(max_length=30, help_text='skdfnl')
    image = models.ImageField(upload_to='categories/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    @property
    def story_count(self):
        return self.stories.count()


class Tag(AbsrtactModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Story(AbsrtactModel):
    category = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='story_images/')
    cover_image = models.ImageField(upload_to='story_cover_images/')
    content = models.TextField()

    def get_absolute_url(self):
        return reverse_lazy('story_detail', kwargs={
            'pk': self.id
        })

    class Meta:
        ordering = ('-created_at', )

    

# story = Story.objects.create(category=category, author=user, title='story', image='image.png', cover_image='image.png', content='skjdfdsjkf')
