from test import process_sc

try:
	with open("a.sc", "rb") as f:
		print(f.name)
		data = f.read()
	process_sc("a", data, "", False)
except Exception as e:
	print(f"{e}")