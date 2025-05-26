import Lab2 as LAB2


def test_find_min_max():
    datalist = [1, 5, 3, 6, 8, 2, 4]
    expected_result = [1, 8]
    test_result = LAB2.find_min_max(datalist)
    assert (test_result == expected_result)


def test_calc_averge():
    datalist = [1, 5, 3, 6, 8, 2, 4]
    expected_result = 4.14
    test_result = LAB2.calc_averge(datalist)
    test_result = round(test_result, 2)
    assert (test_result == expected_result)


def test_calc_median_temperature():
    datalist = [1, 5, 3, 6, 8, 2, 4]
    expected_result = 4.0
    test_result = LAB2.calc_median_temperature(datalist)
    assert (test_result == expected_result)