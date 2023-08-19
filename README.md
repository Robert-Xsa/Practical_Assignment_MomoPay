To run the codes of this repository follow the following steps;
-  Install python in your computer
-  Create a folder on your local computer and inside it create a virtual environment by runing the following command; python -m venv myenv
-  Activate your virtual environment by running; myenv\Scripts\activate
-  Install the dependencies listed in a requirements.txt file by running the following command; pip install -r requirements.txt
-  Runserver by the following command; python manage.py runserver
-  When the server is running, open browser and enter; http://127.0.0.1:8000/
-  To login to the admin dashboard enter; http://127.0.0.1:8000/admin/
-  To simulate printing of the invoice run the following command; python manage.py generate_invoices
Ensure that the server is stopped when simulating the printing of the invoice generated.
Python script that generates invoices based on completed purchase orders is found in the file which located inside the; medicine_managements\purchases\management\commands
