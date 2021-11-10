from processing import process_sc

filename = input("Enter the SC file name: ")
try:
    with open(f"{filename}.sc", "rb") as f:
        print(f.name)
        data = f.read()
    process_sc(filename, data)
except Exception as e:
    print(f"{e}")