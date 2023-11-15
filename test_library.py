from library import cm_to_inch


def test_float_cm_to_inch():
    cm = 5.2
    expected_result = 2.047244094488189
    actual_result = cm_to_inch(cm)
    assert expected_result == actual_result


def test_int_cm_to_inch():
    cm = 2
    expected_result = 0.7874015748031495
    actual_result = cm_to_inch(cm)
    assert expected_result == actual_result


def test_super_float_cm_to_inch():
    cm = 0.003
    expected_result = 0.0011811023622047244
    actual_result = cm_to_inch(cm)
    assert expected_result == actual_result


def test_negative_cm_to_inch():
    cm = -4
    expected_result = -1.574803149606299
    actual_result = cm_to_inch(cm)
    assert expected_result == actual_result


def test_negative_float_cm_to_inch():
    cm = -6.7
    expected_result = -2.6377952755905514
    actual_result = cm_to_inch(cm)
    assert expected_result == actual_result


def test_round_float_cm_to_inch():
    cm = 30.7
    expected_result = 12.09
    actual_result = cm_to_inch(cm, True)
    assert expected_result == actual_result


def test_round_int_cm_to_inch():
    cm = 25
    expected_result = 9.84
    actual_result = cm_to_inch(cm, True)
    assert expected_result == actual_result


def test_null_cm_to_inch():
    cm = 0
    expected_result = 0
    actual_result = cm_to_inch(cm)
    assert expected_result == actual_result


def test_round_null_cm_to_inch():
    cm = 0
    expected_result = 0.0
    actual_result = cm_to_inch(cm, True)
    assert expected_result == actual_result
