#---- define function to read and modify the file

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()
            
        #  modification: uppercase the content
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified file written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#----created an empty input.txt in my plp-python folder for purpose of demonstration
modify_file("input.txt", "output.txt")

#---- define function to read file from user and  handle errors 

def read_file():
    filename = input("Enter a filename to read: ")

    try:
        with open(filename, "r") as f:
            print("\nFile content:\n")
            print(f.read())

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file()
