#Function that takes file name and line number and returns the line as a string.
#If file is not found, returns "File not found". If file is empty, returns "Empty file".
#If the line number is out of range, returns "IndexError".
def file_read(file_name, line_number):
    try:
        file = open(file_name, "r")
        file_lines = file.readlines()
        file.close()
        if len(file_lines) == 0:
            return "Empty file"
        else:
            return file_lines[line_number-1]
    except FileNotFoundError:
        return "File not found"
    except IndexError:
        return "IndexError"