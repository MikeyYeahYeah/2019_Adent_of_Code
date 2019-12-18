def _num_extractor(code_list, op_code_position):
    """Provided a list and a starting position, seeks the position and 
       corresponding value for the first 2 elements and the position
       of the last.  Returns a list."""
    pos_list = code_list[op_code_position + 1 :op_code_position + 4]
    value_list = [
        code_list[pos_list[0]],
        code_list[pos_list[1]],
        pos_list[2]
    ]
    return value_list

def intcode(codes_list):
    """Given a list of numbers, will decode using elf intcode logic."""
    OP_CODE_POSITION = 0
    op_code = codes_list[OP_CODE_POSITION]

    while op_code == 1 or op_code == 2:
        value = _num_extractor(codes_list, OP_CODE_POSITION)
        if op_code == 1:
            codes_list[value[2]] = value[0] + value[1]
        if op_code == 2:
            codes_list[value[2]] = value[0] * value[1]
        OP_CODE_POSITION += 4
        op_code = codes_list[OP_CODE_POSITION]
    
    return codes_list