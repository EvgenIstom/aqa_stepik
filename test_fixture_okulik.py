# Разбираюсь с фикстурами https://www.youtube.com/watch?v=FNQil1Qzghk&t=33s&ab_channel=SeniorTester%7C%D0%95%D0%B2%D0%B3%D0%B5%D0%BD%D0%B8%D0%B9%D0%9E%D0%BA%D1%83%D0%BB%D0%B8%D0%BA

import pytest

@pytest.fixture()
def separator():
    print('\n'+'=' * 100)
    yield 'Hello'
    print('\n test finished')

@pytest.fixture(scope='session')
def all_test():
    print('before all')
    yield
    print('after all')

def test_one_is_one(separator):
    print(separator)
    assert 1==1

def test_two_is_two(all_test):
    assert 2==2

def test_three_is_three(separator):
    assert 3==3