# geo-information-application-for-earthquake-data-based-prediction
A Django based project using Predictive Algorithm to forecast earthquakes based on Data fetched from postgres SQL

## Overview
This project uses **predictive learning** to forecast earthquakes using the **Django framework** and **GIS framework Leaflet.js**, in addition to basic interfacing. The data is stored and retrieved from a **Postgres database**, which is preprocessed to present the sites where earthquakes are likely to happen.

Using data from **1965-2016**, we train a model and predict potential earthquake sites in **2017**, along with expected magnitude and locations on a geo-spatial map.

## Installation

#### Note: Python version 3.7.4-3.7.6 recommended

### 1. Clone the repository
```sh
git clone https://github.com/Fai3Z/geo-information-application-for-earthquake-data-based-prediction.git
```

### 2. Setting Up a Virtual Environment
Before installing dependencies, create a virtual environment:
Windows (my environment was named "envquake":

```sh
python -m venv envquake
envquake\Scripts\activate
```

### 3. Installing Dependencies
Run the following command to install required packages:

```sh
pip install -r requirements.txt
```
#### Some additional packages that may need to be installed:
```sh
pip install gdal django_admin_tools pygdal dj_database_url dj_static django_leaflet
```

### 4. Running the Project
Once dependencies are installed, start the Django server:

```sh
python manage.py runserver
```
Now, open your browser and visit: 🔗 http://127.0.0.1:8000/

### Expected Output
![Description of Image](https://raw.githubusercontent.com//Fai3Z/geo-information-application-for-earthquake-data-based-prediction/main/output1.png)
#### With markers
![Description of Image](https://raw.githubusercontent.com//Fai3Z/geo-information-application-for-earthquake-data-based-prediction/main/output2.png)






