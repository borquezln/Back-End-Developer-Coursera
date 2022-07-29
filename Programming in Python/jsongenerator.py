import json
from employee import details, employee_name, age, title

# Creates a dictionary that stores an employee's information
def create_dict(name, age, title):
    employee_dict = {}
    employee_dict["first_name"] = name
    employee_dict["age"] = int(age)
    employee_dict["title"] = title

    return employee_dict

# Writes json string to file
def write_json_to_file(json_obj, output_file):
    file = open(output_file, "w")
    file.write(json_obj)
    file.close
    return

# Main function
def main():
    # Print the contents of employee.details()
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    # Create the json object
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()