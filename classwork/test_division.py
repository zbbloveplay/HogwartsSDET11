import allure
import pytest

# 商业需求决定测试用例
# 假设：1. 商业需求是能够完成整数和浮点数的除法
#      2. 输入范围：整数或者浮点数
from classwork.div import div


class TestDiv:
    @allure.suite("整数除法")
    @pytest.mark.parametrize("dividend, divisor, expect", {
        (1, 1, 1),
        (0, 1, 0),
        (10000000000000, 2, 5000000000000),
        (-10, 2, -5),
        (-20, -2, 10),
    })
    def test_div_int(self, dividend, divisor, expect):
        assert div(dividend, divisor) == expect

    @allure.suite("浮点数除法")
    @pytest.mark.parametrize("dividend, divisor, precision,expect", {
        (1.1, 1.1, 0, 1),
        (1.2, 2, 0.00000001, 0.6),
        (2.2, 4.4, 0.00000001, 0.5)
    })
    def test_div_float(self, dividend, divisor, precision, expect):
        assert precision >= abs(div(dividend, divisor) - expect)
        assert pytest.approx(expect) == div(dividend, divisor)  # pytest提供的近似判断方法(默认精度1e-6)

    @allure.suite("意外情况")
    @pytest.mark.parametrize("dividend, divisor, exception", {
        (1, 0, ZeroDivisionError),
        (0, 0, ZeroDivisionError),
    })
    def test_div_exception(self, dividend, divisor, exception):
        with pytest.raises(exception):
            div(dividend, divisor)
