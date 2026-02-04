from fairsharer import my_module


def test_fair_sharer_one_iteration():
    values = [0, 1000, 800, 0]
    result = my_module.fair_sharer(values, 1)
    assert result == [100, 800, 900, 0]


def test_fair_sharer_two_iterations():
    values = [0, 1000, 800, 0]
    result = my_module.fair_sharer(values, 2)
    assert result == [100, 890, 720, 90]


def test_no_iterations():
    values = [1, 2, 3]
    result = my_module.fair_sharer(values, 0)
    assert result == values
