import pytest
import lib.intcode as intcode

def test__num_extractor():
    print(intcode._num_extractor([1,0,0,0,99], 0))

@pytest.mark.parametrize("code_list,answer_list", [
    ([1,0,0,0,99],[2,0,0,0,99]),
    ([2,3,0,3,99], [2,3,0,6,99]),
    ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
    ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
])
def test_intcode(code_list, answer_list):
    assert intcode.intcode(code_list) == answer_list