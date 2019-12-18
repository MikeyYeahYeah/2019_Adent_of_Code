from lib import fuel, intcode

def convert_list_to_ints(string_list):
    """Converts a list of strings into a list of ints"""
    return [int(i) for i in string_list]

#=======================
#        MAIN
#=======================

if __name__ == "__main__":
    f = open("files/day1.txt", "r")
    module_mass_list = convert_list_to_ints(f.read().splitlines())

    day2_file = open("files/day2.txt")
    day2_list = day2_file.read().split(",")
    
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

    #Day 2 Part 1
    d2_p1_list = convert_list_to_ints(day2_list)
    d2_p1_list[1] = 12
    d2_p1_list[2] = 2
    d2_p1_result = intcode.intcode(d2_p1_list)
    print(f"DAY 2 PART 1:  {d2_p1_result[0]}")
  

    
