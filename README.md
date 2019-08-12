# Neighbourhood
#### A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts, 09/08/2019


## Description
A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
#### Link to deployed site
https://jamesmutahineighbourhood.herokuapp.com/

## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Contributing](#contributing)
4. [Bugs](#bugs)
5. [Contact me](#support-and-contact-details)
6. [Licensing](#license)


## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/JamesMutahi/neighbourhood.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='rdtfyguihjohucbdsjnc'
DEBUG=True
DB_NAME= '<name of database>'
DB_USER='<your database username>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs
#### Known bugs
 - N/A
 -If any are experiences kindly [contact me](https://mutahijames0@gmail.com)



## Support and contact details
Contact [James Mutahi](https://mutahijames0@gmail.com) for further help/support

### License
[MIT LICENSE](LICENCE)

Copyright (c)2018 **James Mutahi**
