from os import listdir
from shutil import rmtree


chrome_cache_dir = "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
mozilla_cache_dir = "\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\"
users_dir = "D:\\Users\\"
users_list = listdir(users_dir)



for user in users_list:
	try:
		rmtree (users_dir + user + chrome_cache_dir, ignore_errors=True) #This works!
	except FileNotFoundError:
		print("%s Chrome cache not found!" %user)
	print ("%s chrome cache deleted!" %user)
	try:
		for item in listdir(users_dir + user + mozilla_cache_dir):
			if item.endswith(".default"):
				mozilla_folder = item
			rmtree(users_dir + user + mozilla_cache_dir + mozilla_folder, ignore_errors=True)
			print("%s mozilla cache deleted!" %user)
	except FileNotFoundError:
		print("%s Mozilla cache not found!" %user)
