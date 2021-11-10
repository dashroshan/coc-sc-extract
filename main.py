from processing import process_sc
import os

print("Reading the SC files...")
scfiles = os.listdir("./sc")

for scfile in scfiles:
	filename=scfile.split(".")[0]
	try:
		with open(f"sc/{filename}.sc", "rb") as f:
			print(f"\nExtracting : {filename}.sc")
			data = f.read()
		process_sc(filename, data)
	except Exception as e:
		print(f"{e}")

if len(scfiles)!=0:
	print("\nDone!")
else:
	print("No SC files found!")	