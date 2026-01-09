from django.db import models
from.models import Word
# Create your models here.
class Word(models.Model):
    class Word_Category(models.TextChoices):
        name_uz='name_uz','name_uz'
        name_en='name_en','name_en'
        is_active='is_active','is_active'
        created_at='created_at','created_at'

class word_type(models.TextChoices):
    subject='subject','subject'
    object='object','object'
    Noun='Noun','Noun'
    Verb='Verb','Verb'
    adjective='adjective'='adjective'
    adverb='adverb','adverb'
    pronoun='pronoun','pronoun'
    preposition='preposition','preposition'
    conjunction='conjunction','conjunction'
    interjection=' interjection',' interjection'
    determiner='determiner','determiner'
class grammar_roles(models.TextChoices):
    subject='subject','subject'
    object='object','object'
    predicate='predicate', 'predicate'
    complement='complement','complement'
    modifier='modifier','modifier'    
class soz_shakillari(models.TextChoices):
    base_form='base','base'
    past_simple='past_simple','past_simple'
    past_participle='past_participle','past_participle'
    present_participle='present_participle','present_participle'
    plural_form='plural_form','plural_form'