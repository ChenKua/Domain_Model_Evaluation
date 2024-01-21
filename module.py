import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py arg1 arg2")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

file_path = "test_1"
with open(file_path, "w") as file:
    # Write the content to the file
    file.write(str(arg1) + str(arg2))
