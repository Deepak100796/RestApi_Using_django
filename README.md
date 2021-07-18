install django
go to -> backend folder

run command step by step:
    1. pip install -r requirements.txt
    2. python manage.py makemigrations
    3. python manage.py migrate
    4. python manage.py runserver



1: for upload file go to postman enter http://127.0.0.1:8000/app/upload_file  and in body  put filename = choose file pdf or jpg or png
				      and put dirname = directory name
 and hit now your file uploaded 
                  												
		http://127.0.0.1:8000/app/upload_file





2:: for checking all list dir enter  
					http://127.0.0.1:8000/app/list_of_file




3: for download any pic or pdf or png just change in the last pdf or png or jpg in google chrome 
	  
					http://127.0.0.1:8000/app/download_file/?path=pdffile1234/SC_B_nielit_Dec18.pdf&filetype=pdf



