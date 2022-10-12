# Reads in a file.
def read_file(file_name):
    file = open(file_name, "r")
    content = file.read()
    print(content)
    file.close
    return content

# Reads in a file and stores each line as an element in a list
def read_file_into_list(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close
    return lines

# Writes the first line of a string to a file.
def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split("\n")[0]
    file = open(output_filename, "w")
    file.write(first_line)
    file.close
    return

# Reads in the even numbered lines of a file
def read_even_numbered_lines(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    even_lines = []
    for i in range(len(lines)):
        if i % 2:
            even_lines.append(lines[i])
    return even_lines

# Reads a file and returns a list of the lines in reverse order
def read_file_in_reverse(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    reverse = []
    for i in range(len(lines)):
        reverse.insert(0,lines[i])
    return reverse

# Main function
def main():
    file_contents = read_file('sampletext.txt')
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()