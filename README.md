"# CBIBgroup" 
First make sure that the following is installed:
pip install django
pip install xhtml2pdf

To run the static file download CBIBsite folder and cd into the the folder so you have the following view:
CBIBsite
  - CBIBsite
  - media
  - nodes
  - papers
  - templates
  - users
  - db.sqlite3
  - manage.py
  - README.md
  
 The server can then be run with the following command:
 python manage.py runserver
 
 The static site will then be opened at http://127.0.0.1:8000. It can be stopped with CTRL-C.
 
 To run test:
    python manage.py test
 