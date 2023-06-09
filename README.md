# Neo Bank Digital Experience App Backend


### Introduction uwu


This project is the backend for the Neo Bank Digital Experience App. The backend is developed using Django and Django REST Framework and utilizes a PostgreSQL database with the PostGIS extension for location-based features.

The API endpoints are created using Django REST Framework and are secured with JWT authentication using Django JWT. The backend implements the business logic for bank and offers related functionality.

The backend utilizes the current geo-location of the user, location of bank partners, and multiple offers to recommend users various stores and bank offers that they can utilize. The backend is deployed on AWS and provides a robust and scalable solution for the Neo Bank Digital Experience App.

This project is meant to provide a seamless user experience to the end-users of the Neo Bank Digital Experience App while providing the necessary security and performance measures.

### 🛠️Tools/Technology Used

- Django
- Django Rest Framework
- POSTGRES with POSTGIS Extension
- GeoDjango
- Django Rest Simple Jwt
- AWS RDS

### ⚙️Project Setup

```
git clone https://github.com/Parth442002/bucksApi
cd bucksApi
pip install -r requirements.txt
touch .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Api Endpoints
![](./apiEndpoints.png)
