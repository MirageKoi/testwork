## DRF-Testwork

Project where you can create and manage teams and members.

### API Endpoints

#### Members

* **/api/members/** (Member create and list endpoint)
* **/api/members/{member-id}/** (Member retrieve, update and destroy endpoint)

#### Team

* **/api/teams/** (Team create and list endpoint)
* **/api/teams/{team-id}/** (Team retrieve, update and destroy endpoint)

#### API Documentation

* **/api/schema/swagger-ui/** (Browsable API Docs Swagger)
* **/api/schema/** (yaml)
* **/api/schema/redoc/** (Browsable API Docs Redoc)

### Install

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate

### Usage

    python manage.py runserver
