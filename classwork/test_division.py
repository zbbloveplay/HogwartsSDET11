import pytest

from classwork.div import div


# pytest
# -[] 参数化
# -[] allure


class TestDiv:
    @pytest.mark.parametrize("dividend, divisor, expect", {
        (1, 1, 1),
        (0, 1, 0),
        (100000000, 1, 100000000),
        (10000000000000, 2, 5000000000000)
    })
    def test_div_int(self, dividend, divisor, expect):
        assert div(dividend, divisor) == expect

    @pytest.mark.parametrize("dividend, divisor, expect", {
        (1.1, 1.1, 1),
        (1.2, 2, 0.6),
        (2.2, 4.4, 0.5)
    })
    def test_div_float(self, dividend, divisor, expect):
        assert div(dividend, divisor) == expect

    @pytest.mark.parametrize("dividend, divisor, exception", {
        (1, 0, ZeroDivisionError),
        (0, 0, ZeroDivisionError),
    })
    def test_div_exception(self, dividend, divisor, exception):
        with pytest.raises(exception):
            div(dividend, divisor)
