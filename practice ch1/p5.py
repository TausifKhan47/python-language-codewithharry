import os   # Import the built-in os module to work with the operating system

def print_directory_files(path="."):
    """
    Prints all files (not directories) in the given directory.
    Defaults to the current working directory if no path is given.
    """

    try:
        # Get the list of all entries (files + folders) inside the given directory
        entries = os.listdir(path)
    except FileNotFoundError:
        # If the path does not exist, print an error
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        # If the path provided is not a folder, print an error
        print(f"Error: '{path}' is not a directory.")
        return
    except PermissionError:
        # If the program does not have permission to open the directory
        print(f"Error: Permission denied to access '{path}'.")
        return

    # Filter out only files (remove directories) using os.path.isfile
    files = [f for f in entries if os.path.isfile(os.path.join(path, f))]

    # Print the result
    print(f"Files in '{path}':")
    for filename in files:
        print(" -", filename)   # Print each file with a bullet

# This block runs only if the script is executed directly
if __name__ == "__main__":
    # Ask the user for a directory path
    # If left blank, it will use the current directory "."
    directory = input("Enter directory path (leave blank for current directory): ").strip() or "."
    
    # Call the function with the provided directory
    print_directory_files(directory)
