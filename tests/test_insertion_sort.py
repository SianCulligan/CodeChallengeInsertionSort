from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort

def test_version():
    assert __version__ == '0.1.0'


# ******************** HAPPY PATH ********************
def test_can_successfully_sort_an_unsorted_list():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertion_sort([8,4,23,42,16,15])
    assert expected == actual

# ******************** EDGE CASE ********************
def test_can_successfully_sort_a_list_with_negative_nubmers():
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort([20,18,12,8,5,-2])
    assert expected == actual

# ******************** EXPECTED FAIL ********************
def test_will_fail_when_passed_letters():
    expected = "Error"
    actual = insertion_sort(["a", "z", "g", "w", "y", "s", "t"])
    assert expected == actual