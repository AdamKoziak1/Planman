# Planman.ca

Planman is an online project planner and organizer. It will be developed by two high school students over a period of 3 months. The team will be formed by a front-end developer who will mainly handle client-side interactions such as the html, CSS, and javascript, who is will be (Adam) and a backend developer who will mainly handle server-side interact such as authentication and database management (Youssef).

# Planman.ca is still a work in progress!



# PlanMan user guide

When entering planman.ca for the first time, the user is greeted to our homepage.

The homepage includes all sorts of information about Planman, as well as contact information. Once the user decides to use Planman, they can sign in with google. As soon as the user is signed in, they are redirected to their projects page.

The projects page will now act as the landing page for Planman, as long as the user is logged into google. The page is initially empty, but the user is prompted to create a project. Clicking the ‘create project’ button redirects you to the ‘create a project’ page.

Here, the user can fill in any information they need for their project. Once they are finished, the ‘save project’ button redirects them back to their projects page, now with their new project visible. When the user clicks on a project, they are redirected to a dedicated page for that project.

All the information they filled in is present, and they now have access to some more features within that project. They can create tasks for this project, which can help them structure the different parts the project consists of. Creating and editing tasks is a similar procedure to creating projects. If the user wishes to collaborate on the project with another user, they can do so through the ‘add users’ button.

The first page they see contains a list of all users logged into planman. If the person they wish to collaborate with isn’t there, they can click the button at the top to invite them by email.


If the user enters an email and clicks the ‘invite user’ button, an automated email will be sent to that email notifying them that they have been granted access to the project. If someone logs into Planman using a google account with that email, they will have that project in their ‘projects’ page.

If you are the owner of a project, you have complete freedom to do anything with that project. You can edit or delete it, manipulate tasks, or invite more users. However, if you have been invited to a project and do not own it, you only have access to creating new tasks.

When the user is on the page for a certain project, they have the option to enter ‘Gantt chart’ mode.



This generates an automated gantt chart based off the start and end dates for the tasks within that project, allowing them to see visually the timelines they have to work with.




Once a project or task is completed or not needed anymore, the project owner has the option to delete it. This will bring up the delete confirmation page



This page is there to ensure that the user is certain they want to delete the task or project, as it is an irreversible action.




# Requirements :
$ pip install django

$ pip install django-admin

$ pip install social-auth-app-django

$ pip install python-social-auth

$ pip install psycopg2

