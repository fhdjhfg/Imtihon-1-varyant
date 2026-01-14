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

class User_word_history(models.TextChoices):
    user='user','user'
    word='word','word'
    learning_alghoritm='learning_alghoritm','learning_alghoritm'
    from_lang='from_lang','from_lang'
    to_lang='to_lang','to_lang'
    memorize_status='memorize_status','memorize_status'
    word_uz=models.CharField(max_length=255)
    word_en=models.CharField(max_length=255)
    image=models.ImageField(upload_to='word_images/',null=True,blank=True)
    Synonyms=models.TextField(null=True,blank=True)
    Antonyms=models.TextField(null=True,blank=True)
    meaning=models.TextField(null=True,blank=True)

    def str(self):
        return self.word_uz

