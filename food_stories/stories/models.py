from django.db import models


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
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/categories/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Story(AbsrtactModel):
    category = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/story_images/')
    cover_image = models.ImageField(upload_to='media/story_cover_images/')
    content = models.TextField()




