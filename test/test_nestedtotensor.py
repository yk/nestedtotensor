import nestedtotensor as ndt


def test_simple1():
    l = [1, 2, 3]
    l2 = ndt.nested_to_tensor(l, 5)
    assert(len(l) == 3)
    assert(len(l2) == 5)


def test_nested():
    l = [[1, 2], [3, 4, 5]]
    l2 = ndt.nested_to_tensor(l, [4, 2])
    assert(l2[2][1] == 4)
    assert(len(l2) == 4)
    assert(len(l2[2]) == 2)
    l3 = ndt.nested_to_tensor(l, [-1, 5])
    assert(len(l3) == len(l))
    assert(len(l3[0]) == 5)
    assert(l3[0][0] == 1)
    assert(l3[0][1] == 1)
    assert(l3[0][2] == 1)
    assert(l3[0][3] == 2)
    assert(l3[0][4] == 2)
