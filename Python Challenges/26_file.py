# Program to Read Text from a File and Write into Another File


# Open the source file in read mode and destination file in write mode
try:
    with open("26_source.txt", "r") as source_file:
        content = source_file.read()  # Read content from source file

    with open("26_destination.txt", "w") as destination_file:
        destination_file.write(content)  # Write content to destination file

    print("File content copied successfully!")

except FileNotFoundError:
    print("Error: The source file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
