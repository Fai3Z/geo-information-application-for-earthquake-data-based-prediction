from django.db import models

# Create your models here.
# defining fields for our table through a class (next we move on creating the django model (we create a model in django and convert that model into a table))
class Quake(models.Model):
    Date=models.CharField(max_length=100)
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    Type=models.CharField(max_length=100)
    Depth=models.FloatField()
    Magnitude=models.FloatField()
    Magnitude_Type=models.CharField(max_length=100)
    ID=models.CharField(max_length=100)
    
    
    # meta data information (group each record by ID)
    def __str__(self):
        return self.ID
    
    class Meta:
        verbose_name_plural  ='Quake' # class within a class!
# now that we have made the model, we need to run the migrations that will create sql table format for our model in postgresql 
# running commnds in terminal python .\manage.py make migrations
# appply migrations (create table for us in postgres sql) python .\manage.py migrate



# make model for predictions (This is ML based model i.e random forest regressor):
class Quake_Predictions(models.Model): 
   # we will define attributes of our model which will be converted to fields of the table (dataframe) 
   Latitude=models.FloatField()
   Longitude=models.FloatField()
   Depth=models.FloatField()
   Magnitude=models.FloatField()
   # adding a score field as it was present in our ML models final dataframe
   Score=models.FloatField()
   
   class Meta:
       verbose_name_plural='Quake_Predictions'
       
    # next thing to do is to make migrations after adding our secod model
    # this will allow django to create a sql table for us in postgres sql
    # this will be done using python .\manage.py makemigrations
    # apply migrations using python .\manage.py migrate
   
   
   