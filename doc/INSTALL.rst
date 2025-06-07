#####################################
Timehack Documentation
#####################################
*************************************
Install
*************************************

1. Download the code from: https://github.com/sergiolonzi/timehack/tree/main
2. Extract to any folder.
3. Go to the folder timehack/src/timehack/:

.. code-block:: bash
   :number-lines:
   
   cd timehack/src/timehack/
   
4. Create and activate a Python virtual enviroment:

.. code-block:: bash
   :number-lines:
   
   python3 -m venv .venv
   source .venv/bin/activate
   
5. Install the requirements:

.. code-block:: bash
   :number-lines:
   
   python -m pip install -r requirements.txt

5. Make the migrations (only sqlite supported now):

.. code-block:: bash
   :number-lines:
   
   python manage.py migrate

6. Run the server:

.. code-block:: bash
   :number-lines:
   
   python manage.py runserver
   
6. Go to the url: http://127.0.0.1:8000/tasks/index.html

   
