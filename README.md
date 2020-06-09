# Awwards

# Author
By Tabitha Wanjiku,

# Description
This is an application that allows users to upload their personal projects which they have been working on. These projects can then be rated by the other users. The other users can also sign up and post their own personal projects too.

# User Stories
As a user I would like:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

### BDD Specifications Table
|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| Sign Up/Login                            | To create a new account, click on the sign| If login is successful, the user is      |
|                                          | up link and fill in the form details. To  | redirected to the home page              |
|                                          | login, fill in the details                |                                          |
| Add a new project                        | Click on the submit new project tab on the| You will be navigated to a page which    |
|                                          | navbar and submit the project details     | has a form to submit the project         |
| Review a project                         | Click on the Review button                | You will be navigated to a page where you|
|                                          |                                           | can post your review                     |
| Create a profile                         | Click on the profile tab then Edit Profile| A new profile for the user will be       |
|                                          | button                                    | created                                  |
| Search for a project                     | Enter the project's name into the search  | You will be redirected to a page with all||                                          | bar in the navbar                         | results matching your search. You can    |
|                                          |                                           | then click on the project you want       |
| Log out                                  | Click on the Account button and select    | You will be logged out                   ||                                          | log out                                   |                                          |


# Setup/Installation Requirements
## Prerequisites
* Python 3.6.5
* Virtual environment
* PostgreSQL

## Installation Process
* open my GitHub
* find my repo PhotoBooth
* run git clone REPO-URL in your terminal
* write cd Awwards
* create a virtual environment with python3.6 -m venv virtual
* activate the virtual environment :source virtual/bin/activate
* run pip install -r requirements.txt
* create Postgres Database
* run (python3.6 manage.py runserver) to run the application



# Technologies Used
* Python ( ver 3.6 )
* Django ( ver 3.0.6 )
* Django Bootstrap 3
* PostgreSQL
* Heroku

# Acknowledgements
* W3Schools
* Stack Overflow
* Google

## KNOWN BUGS:
Any bugs noted you can email me for clarification.


## CONTACT INFO:
You can email at:mwangitabitha2020@gmail.com

## LICENSE:
MIT License

Copyright (c) [2020] Tabitha Wanjiku]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.