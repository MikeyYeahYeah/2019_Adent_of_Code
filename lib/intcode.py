def num_extractor(code_list, op_code_position):
    pos_list = code_list[op_code_position + 1:4]
    value_list = [code_list[i] for i in pos_list]
    return value_list

def intcode(codes_list):
    OP_CODE_POSITION = 0
    op_code = codes_list[OP_CODE_POSITION]

    while op_code == 1 or op_code == 2:
        if op_code == 1:
            first_num_pos = codes_list[OP_CODE_POSITION + 1]
            second_num_pos = codes_list[OP_CODE_POSITION + 2]
            third_num_pos = codes_list[OP_CODE_POSITION + 3]

            first_num = codes_list[first_num_pos]
            second_num = codes_list[second_num_pos]
            codes_list[third_num_pos] = first_num + second_num
            OP_CODE_POSITION += 4
            op_code = codes_list[OP_CODE_POSITION]
        
        if op_code == 2:
            first_num_pos = codes_list[OP_CODE_POSITION + 1]
            second_num_pos = codes_list[OP_CODE_POSITION + 2]
            third_num_pos = codes_list[OP_CODE_POSITION + 3]

            first_num = codes_list[first_num_pos]
            second_num = codes_list[second_num_pos]
            codes_list[third_num_pos] = first_num * second_num
            OP_CODE_POSITION += 4
            op_code = codes_list[OP_CODE_POSITION]
    
    return codes_list