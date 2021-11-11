#This script read the files present in the sc folder and passes the data of each of them one-by-one to the processing.py file

from processing import process_sc
import os

print("Reading the SC files...")
scfiles = os.listdir("./sc") #List of names of all the files present in the sc directory along with their extensions

for scfile in scfiles:
	filename=scfile.split(".")[0] #Stripping out the extension
	if filename=="": #To avoid the .ignore file I am using to keep the sc folder active on this github repo
		continue
	try:
		with open(f"sc/{filename}.sc", "rb") as f:
			print(f"\nExtracting : {filename}.sc")
			data = f.read()
		process_sc(filename, data) #Imported from the processing.py file
	except Exception as e:
		print(f"{e}")

if len(scfiles)!=1: #1 and not 0 because of the .ignore file
	print("\nDone!")
else:
	print("No SC files found!")	
