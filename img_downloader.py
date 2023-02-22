"""photo downloader
the name of the downloaded photo will be time like this formate:21:02:47
change the number in the parenthesis after manypic 
so that you can download imgs as many as you want
"""
import requests
from datetime import datetime

url = 'https://api.vvhan.com/api/view'
#public api to invoke

def filename():
	#use strftime as filename
	current_time = datetime.now().strftime("%X")
	return current_time

def downloader(url,filename):
	#function to download img
	r = requests.get(url)
	with open(f'./{filename}.png','wb') as f:
		f.write(r.content)    #wrtite into the file
	print(f'{filename}.png downloaded!\n')   #success info

def manypic(number):
	#download as many img as you want 
	for i in range(number):
		downloader(url,filename())

def order():
	print('How many imgs would you like to download?')
	number = input()
	number = int(number)
	manypic(number)

order()

