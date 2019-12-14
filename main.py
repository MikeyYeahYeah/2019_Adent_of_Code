from lib.fuel import calculator

def convert_list_to_ints(string_list):
    """Converts a list of strings into a list of ints"""
    return [int(i) for i in string_list]

#=======================
#        MAIN
#=======================

if __name__ == "__main__":
    f = open("files/day1.txt", "r")
    module_mass_list = convert_list_to_ints(f.read().splitlines())
    
    fuel_req_list = [calculator(i) for i in module_mass_list]
    fuel_req_all_modules = sum(fuel_req_list)
    print(fuel_req_all_modules)

    
