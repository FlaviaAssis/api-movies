import csv
import json
import requests

jsfile = file('movies.json', 'w') #
jsfile.write('[\r\n')

generos  = [
'unknown',       #0
'Action',        #1
'Adventure',     #2
'Animation',     #3
'Children',      #4
'Comedy',        #5
'Crime',         #6 
'Documentary',   #7
'Drama',         #8
'Fantasy',       #9
'Film-Noir',     #10
'Horror',        #11
'Musical',       #12
'Mystery',       #13
'Romance',       #14
'Sci-Fi',        #15
'Thriller',      #16
'War',           #17
'Western'        #18
]

 
with open('/home/flavia/Documentos/u.item','r') as f: #INSERIR PATH PARA ARQUIVO
	
	line = f.readline()

	while line:
    
    		lineMovies = line.split('|')

    		if(lineMovies[1] != 'unknown'):
	    		jsfile.write('\t{\r\n')

	        n = '\t\t\"title\": \"' + lineMovies[1][:-7] + '\",\r\n'
	        i = '\t\t\"year\": ' + lineMovies[2][7:] + ',\r\n'


	        if(lineMovies[1] != 'unknown'):
		        jsfile.write(n)
		        jsfile.write(i)



	        d = '\t\t\"genres": ['

	        x = 0
	        cont = 0
	        lineSize = len(line)

	   
		while(x < 19):
			if (lineMovies[x+5]=='1' ):
					cont+= 1
					palavra = generos[x]
					if(cont>1):
						d = d + ",\"" + palavra + "\""
						#jsfile.write(palavra)
					else:
						d = d + "\"" + palavra + "\""
			x = x + 1

		if(line[lineSize-2] == '1'):
			cont+= 1
			palavra = generos[18]
			if(cont>1):
				d = d + ",\"" + palavra + "\""
				#jsfile.write(palavra)
			else:
				d = d + "\"" + palavra + "\""
		    
       	
   	 	d = d+'],\r\n'

   	 	if(lineMovies[1] != 'unknown'):
			jsfile.write(d)

		movie = lineMovies[1][:-7]
		site = 'http://www.omdbapi.com/?apikey=860e63cd&t='+movie

		r = requests.get(site)
		if r.status_code == 200:
    			reddit_data = json.loads(r.content)

    	
		l = ""
		if reddit_data['Response'] == 'True':
			l = reddit_data['Director'].encode('utf-8')

		
		e = '\t\t\"director": \"'+l+'\"\r\n'
		if(lineMovies[1] != 'unknown'):
			jsfile.write(e)


		line = f.readline()
		if(line == ''):
			if(lineMovies[1] != 'unknown'):
				jsfile.write('\t}\n')
		else:
			if(lineMovies[1] != 'unknown'):
				jsfile.write('\t},\n')
		

jsfile.write(']')
jsfile.close()
