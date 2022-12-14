import readtime

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse
from django.utils.text import slugify 
from django.utils.translation import gettext_lazy as _

from movie.managers import MovieManager

from ckeditor.fields import RichTextField
from hitcount.models import HitCount
from star_ratings.models import Rating
from taggit.managers import TaggableManager


class Movie(models.Model):
    """ Model definition for Movies. """

    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    author = models.ForeignKey('accounts.User', null=True, on_delete=models.CASCADE, related_name='movie')
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, allow_unicode=True, unique=True)
    description = RichTextField(_('Description'), null=True)
    director = models.ForeignKey('movie.Actor', null=True, blank=True, on_delete= models.CASCADE, related_name='director')
    actor = models.ForeignKey('movie.Actor', null=True, blank=True, on_delete= models.CASCADE, related_name='actor')
    pub_date = models.DateField(_('Published Date'), null=True)
  
    imdb_rating = models.FloatField(_('IMDB Rating'), default=0, null=True)
    budget = models.DecimalField(_('Movie Budget'), decimal_places=3, max_digits=6, default=0, null=True)
    trailer = models.FileField(_('Trailer'), null=True, blank=True)
    thumbnail = models.ImageField(_('Thumbnail'), upload_to="movie/images/", null=True)

    ratings = GenericRelation(Rating, related_query_name='ratings')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    
    status = models.CharField(_('Status'), max_length=1, default='D', choices=STATUS_CHOICES)
    
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
 
    tags = TaggableManager()
 
    class Meta:
        """ Meta definition of Movies. """
        # db_index = True
        # order_insertion_by = ['title']
        # unique_together = ('movie', 'genre')
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
        ordering = ['-created_at']
        
    def __str__(self):
        """ Unicode representation of Movies. """
        return self.title

    def __repr__(self):
        return self.__str__()

    def get_readtime(self):
        """ Calculates the time description takes the average human to read. """ 
        result = readtime.of_text(self.description)
        return result.text
    
    def get_description(self):
        """ Returns the description of the movie. """
        return self.description.lower()

    def get_absolute_url(self):
        return reverse('movie:detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    objects = MovieManager()
    