from __future__ import with_statement

"""
Test Chamomile tests themselves. A bit meta.
"""

import sys

import chamomile

class TestTest(chamomile.Test):
    def __init__(self, *args, **kwargs):
        chamomile.Test.__init__(self, *args, **kwargs)

        self.before_calls = 0
        self.after_calls = 0

        self.after_checks = 0

    def before(self):
        self.before_calls += 1

    def after(self):
        self.after_calls += 1

    def test_before(self):
        self.assertGreater(self.before_calls, 0)

    # after() is tricky to test without making assumptions about what order
    # the tests will be run in. With just one test for it, that test could
    # be the test which is run first, i.e., before after() is called. So
    # we try the test twice, because at least one attempt will not be the
    # first test.
    def test_after_1(self):
        self._test_after()

    def test_after_2(self):
        self._test_after()

    def _test_after(self):
        if self.after_checks > 0:
            self.assertGreater(self.after_calls, 0)
        self.after_checks += 1

    def test_assertions(self):
        self.expect(1).to_equal(1)
        self.expect(1).to_not_equal(2)
        self.expect(True).to_be(True)
        self.expect([1, 2]).to_not_be([1, 2])
        self.expect(1).to_be_true()
        self.expect(0).to_be_false()
        self.expect(None).to_be_none()
        self.expect('hi').to_not_be_none()
        self.expect('hello').to_contain('e')
        self.expect('hello').to_not_contain('x')
        self.expect('hello').to_be_a(str)
        self.expect('hello').to_not_be_a(float)
        self.expect(1).to_be_an(int)
        self.expect('hi').to_not_be_an(int)

        with self.expect(ValueError):
            raise ValueError('test')

        try:
            with self.expect(ValueError):
                raise RuntimeError('test')
        except RuntimeError:
            self.success()
        else:
            self.fail('Should have raised RuntimeError')

    def test_assertion_failures(self):
        with self.expect(AssertionError):
            self.expect(0).to_equal(1)
        with self.expect(AssertionError):
            self.expect(0).to_not_equal(0)
        with self.expect(AssertionError):
            self.expect(True).to_be(False)
        with self.expect(AssertionError):
            self.expect(True).to_not_be(True)
        with self.expect(AssertionError):
            self.expect(0).to_be_true()
        with self.expect(AssertionError):
            self.expect(1).to_be_false()
        with self.expect(AssertionError):
            self.expect(False).to_be_none()
        with self.expect(AssertionError):
            self.expect(None).to_not_be_none()
        with self.expect(AssertionError):
            self.expect('hello').to_contain('x')
        with self.expect(AssertionError):
            self.expect('hello').to_not_contain('e')
        with self.expect(AssertionError):
            self.expect('hello').to_be_a(float)
        with self.expect(AssertionError):
            self.expect('hello').to_be_an(int)
        with self.expect(AssertionError):
            self.expect('hello').to_not_be_a(str)
        with self.expect(AssertionError):
            self.expect(1).to_not_be_an(int)

        with self.expect(AssertionError):
            with self.expect(Exception):
                pass

    def test_custom_message(self):
        message = 'the tuba is made of brass'

        try:
            self.expect(0).to_equal(1, message)
        except AssertionError:
            error = sys.exc_info()[1]
            self.expect(str(error)).to_contain(message)

if __name__ == '__main__':
    chamomile.main()
