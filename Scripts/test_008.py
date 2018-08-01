import pytest
import allure
class Test_008():
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="hell0")
    def test_008(self):
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="你好")
    def test_008a(self):
        allure.attach("八嘎","gameover")
        allure.attach("yikesou", "sayolala")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="阿达")
    def test_008b(self):
        assert 0