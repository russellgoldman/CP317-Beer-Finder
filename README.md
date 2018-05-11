# CP317 Beer Finder Web App

## Inspiration
Have you ever had an idea of what kind of beer you wanted, maybe a lighter beer with hops and a low alcohol content, but you didn’t know what brand would be best linked to your criteria?

Our web application hopes to solve this by asking for user search criteria and returning a list of beers that match their specifications in order from ***most alike*** to ***least alike***.

## Tools
### Front-end:
* **Scripting:** JavaScript
* **Structure:** HTML
* **Styling:** CSS / Bootstrap

### Back-end:
* **Server:** Django server routes in Python
* **Database:** PostgreSQL (built-in with Django) OR connection to a MySQL database
* **API:** Django GET and POST definitions for accessing/modifying database content
* **Data Structures:** List, Queue, Stack

### Connection between Front and Back-ends:
* Django has a templating system which allows for the inclusion and rendering of HTML files to our server
* All CSS and JS files are contained in a special folder named *static* where they can be referenced within the HTML file
* Django is responsible for hosting the web application, accessing and modifying our PostgreSQL database, and handling API GET and POST requests from the JS front-end client to access/modify data in the back-end
* JS is responsible for manipulating the HTML Document Object Model (DOM) and formulating front-end logic
* CSS and Bootstrap are used for styling

## Installation
To run the program, you will need to unfreeze the virtual environment from the requirements.txt file and install it on your local system. To do so, enter the following in the terminal.
```shell
pip3 install -r requirements.txt
```
