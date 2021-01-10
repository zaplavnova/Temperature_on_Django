
Use  worker.py to write new information in postgres table (get)
/************************************************************/

To run worker every 30 min:
	crontab -e
	nano
		*/30 * * * *  /path_to_file/worker.py

/************************************************************/
postgres table:

temp1 real
temp2 real
temp3 real
ts    time

/************************************************************/
File chart.py using to draw data on the http page 
File urls.py calling for chart.py (send)

/************************************************************/

To show the result:
	python3 manage.py runserver 
