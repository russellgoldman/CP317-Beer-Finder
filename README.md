# CP317 Beer Finder Web App

## Author Information:
- **Designed by:** CP317 Software Engineering Students
- **Date Started:** May 5th, 2018
- **Date Completed:** August 14th, 2018

## Inspiration:
Have you ever had an idea of what kind of beer you wanted, maybe a dark yellow beer with a medium body and an approximately 5% alcohol content, but you didn’t know what brand would be best linked to your criteria?

Our web application hopes to solve this by asking for user search criteria and returning a list of beers that match their specifications in order from ***most alike*** to ***least alike***.

## Tools:
#### Front-end:
* **Scripting:** Django templating language (DTL) / JavaScript
* **Structure:** HTML
* **Styling:** CSS / Bootstrap

#### Back-end:
* **Server:** Heroku
* **Database:** PostgreSQL (built-in with Django)
* **API:** Flask definitions for accessing/modifying database content
* **Data Structures:** List, Queue, Stack

#### Connection between Front and Back-ends:
* Django has a templating system called Jinga which allows for the dynamic conditional rendering of HTML files
* All CSS and JS files are contained in a special folder named *static* where they can be referenced within the HTML file
* Django is responsible for hosting the web application, accessing and modifying our PostgreSQL database, and with the Flask Framework, it can handle API requests so the front-end client can access/modify data from our back-end
* JS is responsible for further manipulation of the HTML Document Object Model (DOM) that cannot be handed by DTL
* CSS and Bootstrap are used for styling

## Backend API:
[Backend API repository](https://github.com/russellgoldman/CP317-Beer-Finder-API)

## Team Members
[Contributions Document](https://docs.google.com/spreadsheets/d/1OM_BYqcARu_l3H8tbjbGLzDzcIXs0oqbfTc1smgX3_c/edit?usp=sharing)

### Lead Developers
- Russell Goldman
- Tauqeer Choudhry
- Don Vo

### Django Templates
- Abdullahi Abdullahi
- Ziheng Wang (Isaac)
- Zhixian Li (Catherine)
- Abdisalan Mohamed Abdi

### Bootstrap / CSS Styling
- Ni Yang (Nina)
- Yuting He
- Franchesco Livado

### Modellers and Database
- Yanda Tao
- David Moreno
- Sirong Liu
- Yu He
- Peiyu Lu (Lucy)

### Views and Routing
- ~Abraham Banka~ (Dropped the course)
- ~Zizheng Huang~ (Dropped the course)
- ~Mengdan Wan~ (Dropped the course)
- ~Jerry Haq~ (Dropped the course)

### API Developers
- Jeremy Lickers
- Matthew Wong
- Huai Yao Hu (Walter)
- Wen Han Tang

## Requirements Document
- [Requirements document](https://russellgoldman.github.io/CP317-Requirements-Document/)
- [GitHub repository](https://github.com/russellgoldman/CP317-Requirements-Document)

## Analysis Document
- [Analysis document](https://russellgoldman.github.io/CP317-Analysis-Document/)
- [GitHub repository](https://github.com/russellgoldman/CP317-Analysis-Document)

## Design Document
- [Design document](https://russellgoldman.github.io/CP317-Design-Document/)
- [GitHub repository](https://github.com/russellgoldman/CP317-Design-Document)

## Installation
Clone this Git repository and unfreeze the requirements.txt file to gain access to a venv depencency folder.
```shell
source venv/bin/activate
pip3 install -r requirements.txt
```

## Updating Dependencies
After updating dependencies on your venv, you **MUST** re-freeze the requirements.txt file.
```shell
source venv/bin/activate
pip3 freeze > requirements.txt
```

## Running the Localhost Server
Open a Console program such as Terminal (Mac / Linux) or Windows Powershell (Windows). Use the *cd* (change directory) and *ls* (short listing) commands to move into the Git repository. From the root of the project, enter
 ```shell
 cd projectRoot
 source venv/bin/activate
 python3 manage.py runserver
 ```
This will activate the localhost server and you will be able to view the application on the port displayed in the Console script.

**Note**: For this to work, you must have *python3* installed on your local machine path.
