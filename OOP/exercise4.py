def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content is here")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist")
    
file_name = input("Enter the name of the file: ")
read_file(file_name)