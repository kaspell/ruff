# Errors

def test_this_is_a_test(a=1): ...
def testThisIsAlsoATest(a=1): ...

class TestClass:
    def test_this_too_is_a_test(self, a=1): ...
    def testAndOfCourseThis(self, a=1): ...


# No errors

def this_is_not_a_test(a=1): ...

class TestClassLookalike:
    def __init__(self): ...
    def test_this_is_not_a_test(self, a=1): ...
