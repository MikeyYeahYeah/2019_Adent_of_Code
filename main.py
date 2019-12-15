from lib import fuel

def convert_list_to_ints(string_list):
    """Converts a list of strings into a list of ints"""
    return [int(i) for i in string_list]

#=======================
#        MAIN
#=======================

if __name__ == "__main__":
    f = open("files/day1.txt", "r")
    module_mass_list = convert_list_to_ints(f.read().splitlines())
    
    print("=" * 30)
    print(" " * 11 + "Results")
    print("=" * 30)

    # Day 1 Part 1
    d1_p1_fuel_req_list = [fuel._calculation(i) for i in module_mass_list]
    d1_p1_total = sum(d1_p1_fuel_req_list)
    print(f"DAY 1 PART 1:  {d1_p1_total}")

    # Day 1 Part 2
    d1_p2_fuel_req_list = [fuel.total(i) for i in module_mass_list]
    d1_p2_total = sum(d1_p2_fuel_req_list)
    print(f"DAY 1 PART 2:  {d1_p2_total}")
  

    
