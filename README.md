# geo-information-application-for-earthquake-data-based-prediction
A Django based project using Predictive Algorithm to forecast earthquakes based on Data fetched from postgres SQL

## Overview
This project uses **predictive learning** to forecast earthquakes using the **Django framework** and **GIS framework Leaflet.js**, in addition to basic interfacing. The data is stored and retrieved from a **Postgres database**, which is preprocessed to present the sites where earthquakes are likely to happen.

Using data from **1965-2016**, we train a model and predict potential earthquake sites in **2017**, along with expected magnitude and locations on a geo-spatial map.

## Installation

### 1. Clone the repository
```sh
git clone <This repository's link>


### 2. Create a virtual environment
my environment was amed "envquake"

python -m venv envquake
source envquake/bin/activate  # On macOS/Linux
envquake\Scripts\activate     # On Windows

### 3. Install dependencies
pip install -r requirements.txt

Note: Additional dependencies that may be needed:
gdal, django_admin_tools, pygdal, dj_database_url, dj_static, django_leaflet

### 4. Running the Project
You can run the project using:
python manage.py runserver
Then, open your browser and go to: 🔗 http://127.0.0.1:8000/

Output:
**(`output1.png` and `output2.png`)**

```sh
git add README.md
git commit -m "Added README file"
git push origin main



