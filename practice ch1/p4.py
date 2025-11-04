import os

def print_directory_files(path="."):
    """
    Prints all files (not directories) in the given directory.
    Defaults to the current working directory if no path is given.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return

    files = [f for f in entries if os.path.isfile(os.path.join(path, f))]
    print(f"Files in '{path}':")
    for filename in files:
        print(" -", filename)

if __name__ == "__main__":
    directory = input("Enter directory path (leave blank for current directory): ").strip() or "."
    print_directory_files(directory)
