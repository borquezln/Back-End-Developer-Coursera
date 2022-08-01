# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function
def mod(employee_list):
    temp = employee_list['name'] + "_" + employee_list["department"]
    return temp

# Modifies the employee list of dictionaries into list of employee-department strings
def to_mod_list(employee_list):
    name_dep_map = map(mod, employee_list)
    name_dep = []
    for x in name_dep_map:
        name_dep.append(x)
    return name_dep

    raise NotImplementedError()

# Generates a list of usernames 
def generate_usernames(mod_list):
    unames = [name.replace(" ", "_") for name in mod_list]
    return unames

    raise NotImplementedError()

# Maps employee id to first initial
def map_id_to_initial(employee_list):
    id_name_dict = {emp["name"][0] : emp["id"] for emp in employee_list}
    return id_name_dict

    raise NotImplementedError()

def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
    main()