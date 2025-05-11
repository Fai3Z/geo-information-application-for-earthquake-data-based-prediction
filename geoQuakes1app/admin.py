from django.contrib import admin
from datetime import datetime
import pandas as pd
from geoQuakes1app.models import Quake
import numpy as np
from geoQuakes1app.models import Quake, Quake_Predictions
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Quake is class in model.py file within geoQuakes1app project/directory

# Register your models here.
admin.site.register(Quake)
# register our second model here
admin.site.register(Quake_Predictions) 


# now that we have downloaded the dataset, we need to clean it and transform it into the format we need

# if dataset emplty i.e select statement returns 0 rows then load dataset,otherwise dont load as it will slow down our app
if Quake.objects.all().count()==0:
    # add the dataset as a dataframe so we can model our data according to ML model requirements and store in our database to train model
    df=pd.read_csv(r"C:\Users\Pc\Documents\database.csv")
    
    # preview df
    print(df.head())
    
    # transform dataframe by editing fields we dont need
    df_load=df.drop(['Depth Error', 'Time', 'Depth Seismic Stations', 'Magnitude Error', 'Magnitude Seismic Stations', 'Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square', 'Source', 'Location Source', 'Magnitude Source', 'Status'], axis=1)
    
    # preview df load
    #print (df_load.head())
    
    # rename fields with spaces so one column dont become 2 columns in some tools
    df_load=df_load.rename(columns={"Magnitude Type":"Magnitude_Type"})
    
    # preview df_load
    #print(df_load.head())
    
    # now we use for loop to iterate through each entry of cleaned table and load that table into postgres DB
    # loading into Quake1 model/table in postgres
    for index, row in df_load.iterrows():
        Date=row['Date']
        Latitude=row['Latitude']
        Longitude=row['Longitude']
        Type=row['Type']
        Depth=row['Depth']
        Magnitude=row['Magnitude']
        Magnitude_Type=row['Magnitude_Type']
        ID=row['ID']
    # mapping bacedn cleaned df rows to rows in database (probably using the ODBC driver)
    
        # save statmet (insert statement)
        Quake(Date=Date, Latitude=Latitude, Longitude=Longitude,
              Type=Type, Depth=Depth, Magnitude=Magnitude,
              Magnitude_Type=Magnitude_Type, ID=ID).save()
        # row saved to quake model and Quake model will create SQL command to populate table in postgres
        
        # data inserted in DB (goto quake1>schemas>tables>geoQuakes1app_quake (rightclick>scripts>select script) and run it)
        
# we will add our machine learning code (random forest regressor) in the admin.py file

# important: if Quake_Predictions table is empty then run our ML (random forest regressor) code otherwise dont run ML code

if Quake_Predictions.objects.all().count()==0:
    # Add the 2017 test data annd 1965-2016 training data
    df_test=pd.read_csv(r"https://raw.githubusercontent.com/EBISYS/WaterWatch/refs/heads/master/earthquakeTest.csv") # potential bug is that we should download dataset and include path here
    df_train=pd.read_csv(r"C:\Users\Pc\Documents\database.csv")
    
    # we are simply following the same things we did (proved to work) in colab notebook
    df_train_load=df_train.drop(['Depth Error', 'Time', 'Depth Seismic Stations', 'Magnitude Error', 'Magnitude Seismic Stations', 'Azimuthal Gap', 'Horizontal Distance', 'Horizontal Error', 'Root Mean Square', 'Source', 'Location Source', 'Magnitude Source', 'Status'], axis=1)
    df_test_load=df_test[['time', 'latitude', 'longitude', 'mag', 'depth']]

    df_train_load=df_train_load.rename(columns={'Magnitude Type':'Magnitude_Type'})
    df_test_load=df_test_load.rename(columns={'time':'Date', 'latitude':'Latitude', 'longitude':'Longitude', 'mag':'Magnitude', 'depth':'Depth'})
    
    # creating training and testing dataframe (same to same what was done in colab notebook in faiezwebback)
    df_train_data=df_train_load[['Latitude', 'Longitude', 'Magnitude', 'Depth']]
    df_test_data=df_test_load[['Latitude', 'Longitude', 'Magnitude', 'Depth']]
    
    df_train_data.dropna()
    df_test_data.dropna()
    
    X=df_train_data[['Latitude', 'Longitude']]
    y_pred=df_train_data[['Magnitude', 'Depth']]

    X_new=df_test_data[['Latitude', 'Longitude']]
    Y_new_pred=df_test_data[['Magnitude', 'Depth']]
    
    X_train, X_test, y_train, y_test=train_test_split(X,y_pred,test_size=0.2, random_state=42)
    
    model_1=RandomForestRegressor(random_state=42)
    model_1.fit(X_train, y_train)
    model_1.predict(X_test)
    # score=model_1.score(X_test,y_test)*100
    
    # we will improve the model accuracy by automating hyperparameter tuning
    parameters={'n_estimators': [10,20,50,100,200,500]}

    grid_obj=GridSearchCV(model_1, parameters) # Note: grid search object will pass list of parameters to model and give us the best performing parameter model (using various hyperparameter values of a model in an automated manner to find best value of parameter)

    grid_fit=grid_obj.fit(X_train,y_train)

    best_fit=grid_fit.best_estimator_

    results=best_fit.predict(X_test)
    
    # preview the score
    score=best_fit.score(X_test, y_test)*100
    #print(score)
    
    # the running of code took too long i.e 5 mins due to training, we want to run this model only once when table is empty, dont run it the second time unless some change has been made
    
    # use this model to make predictions on 2017 data
    final_results=best_fit.predict(X_new)
    
    # evaluate model score
    final_score=best_fit.score(X_new, Y_new_pred)*100
    
    # store prediction results into a list
    lst_Magnitudes=[]
    lst_Depth=[]
    i=0

    # iterate over predicted data and store in lists above

    for r in final_results.tolist():
        lst_Magnitudes.append(final_results[i][0]) # list of list so store in it
        lst_Depth.append(final_results[i][1]) # same story
        i+=1

        # create new dataframe containing X_new fields (Latitude and Longitude), magnitude and depth values from the lists above (predicted values)

    df_results=X_new[['Latitude', 'Longitude']]
    # create new filds in the new Dataframe
    df_results['Magnitude']=lst_Magnitudes
    df_results['Depth']=lst_Depth
    df_results['Score']=final_score
    
    # preview prediction dataset
    #print(df_results.head())
    
    # now we are ready to load this table in our sql table
    
    for index,row in df_results.iterrows():
        Latitude=row['Latitude']
        Longitude=row['Longitude']
        Magnitude=row['Magnitude']
        Depth=row['Depth']
        Score=row['Score']
        
        Quake_Predictions(Latitude=Latitude, Longitude=Longitude, Magnitude=Magnitude, Depth=Depth, Score=Score).save()
        
        
        # Note: optimize this shit it takes too long to run by giving gpt full files context and asking it to improve upon it look up approaches on your end as well.
        
# next we have to create a URL endpoint for our prediction dataset we stored in our Quake1 DB in postgresql. for this we will eed to modify the views.py file


        
        