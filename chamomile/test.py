"""
Chamomile provides a cleaner, Jasmine-style assertion interface for
unittest tests.
"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest

main = unittest.main

class Test(unittest.TestCase):
    """
    Public: Provides a cleaner, Jasmine-style assertion interface than
    unittest itself does. The assertion style exposed here through
    expectations makes it clearer in a test what is the expected value
    and what is the observed value, and allows convenient chaining to
    make multiple assertions about the same value.
    """

    def expect(self, value):
        """
        Public: Create an expectation about a particular value.

        value - Any value that you want to make assertions with.

        Returns an `Expectation`.
        """

        return Expectation(value, self)

    def success(self, message=None):
        """
        Public: Record a successful test result that was not determined
        by one of the Expectation methods.

        message - An optional string explaining what succeeded.

        Returns nothing.
        """

        self.assertTrue(True, message)

    @classmethod
    def setUpClass(cls):
        """
        Internal: Effectively installs the test's `before_all` method (if any)
        at the name where unittest expects to find it.
        """

        if hasattr(cls, 'before_all'):
            cls.before_all()

    def setUp(self):
        """
        Internal: Effectively installs the test's `before` method (if any)
        at the name where unittest expects to find it.
        """

        if hasattr(self, 'before'):
            self.before()

    def tearDown(self):
        """
        Internal: Effectively installs the test's `after` method (if any)
        at the name where unittest expects to find it.
        """

        if hasattr(self, 'after'):
            self.after()

    @classmethod
    def tearDownClass(cls):
        """
        Internal: Effectively installs the test's `after_all` method (if any)
        at the name where unittest expects to find it.
        """

        if hasattr(cls, 'after_all'):
            cls.after_all()

class Expectation(object):
    """
    Public: Used to check expectations (i.e., make assertions).

    Expectation objects are produced by Test's `expect` method.
    """

    def __init__(self, value, test):
        """
        Internal: Initialize an Expectation.

        value - The observed value about which assertions will be made.
        test  - The underlying `Test` object.
        """

        self.value = value
        self.test = test

    def to_equal(self, expected, message=None):
        """
        Public: Asserts that the observed value is equal to the given value.

        expected - The value you are expecting to observe.
        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value is not equal to the
          expected value.
        """

        self.test.assertEqual(expected, self.value)
        return self

    def to_not_equal(self, expected):
        """
        Public: Asserts that the observed value is not equal to the given
        value.

        expected - The value you are not expecting to observe.
        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value not equal to the
          expected value.
        """

        self.test.assertNotEqual(expected, self.value)
        return self

    def to_be(self, expected):
        """
        Public: Asserts that the observed value is the same object as the
        given value.

        expected - The exact object you are expecting to observe.
        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value `is not` the
          expected value.
        """

        self.test.assertIs(expected, self.value)
        return self

    def to_not_be(self, expected):
        """
        Public: Asserts that the observed value isn't the same object as
        the given value.

        expected - An object you are not expecting to observe.
        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value `is` the
          expected value.
        """

        self.test.assertIsNot(expected, self.value)
        return self

    def to_be_true(self):
        """
        Public: Asserts that the observed value is considered to be true
        by Python.

        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value is considered a false
          value in Python.
        """

        self.test.assertTrue(self.value)
        return self

    def to_be_false(self):
        """
        Public: Asserts that the observed value is considered to be false
        by Python.

        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value is considered a true
          value in Python.
        """

        self.test.assertFalse(self.value)
        return self

    def to_be_none(self):
        """
        Public: Asserts that the observed value `is None`.

        This is shorthand for `to_be(None)`.

        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value `is not None`.
        """

        self.test.assertIsNone(self.value)
        return self

    def to_not_be_none(self):
        """
        Public: Asserts that the observed value `is not None`.

        This is shorthand for `to_not_be(None)`.

        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value `is None`.
        """

        self.test.assertIsNotNone(self.value)
        return self

    def to_contain(self, expected):
        """
        Public: Asserts that the given value is `in` the observed value.

        expected - A value you are expecting to be in the observed value.
        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the given value is not in the observed
          value.
        """

        self.test.assertIn(expected, self.value)
        return self

    def to_not_contain(self, expected):
        """
        Public: Asserts that the given value is `not in` the observed value.

        expected - A value you are expecting to not be in the observed value.
        message  - An optional string that will be associated with any
                   assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the given value is in the observed
          value.
        """

        self.test.assertNotIn(expected, self.value)
        return self

    def to_be_a(self, expected_type):
        """
        Public: Asserts that the observed value is an instance of the given
        type.

        expected_type - A type that you are expecting the observed value
                        to be an instance of
        message       - An optional string that will be associated with
                        any assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value is not an instance of
          the given type.
        """

        self.test.assertIsInstance(self.value, expected_type)
        return self

    to_be_an = to_be_a

    def to_not_be_a(self, expected_type):
        """
        Public: Asserts that the observed value is not an instance of the
        given type.

        expected_type - A type that you are expecting the observed value
                        to not be an instance of
        message       - An optional string that will be associated with
                        any assertion errors (default: none).

        Returns this Expectation.
        Raises AssertionError if the observed value is an instance of
          the given type.
        """

        self.test.assertNotIsInstance(self.value, expected_type)
        return self

    to_not_be_an = to_not_be_a

    def __enter__(self):
        """
        Public: Asserts that the body of the `with` block will raise an
        exception of the type passed to `expect()`.

        Examples

          def test_zero_division(self):
              with self.expect(ZeroDivisionError):
                  4 / 0

        Raises TypeError if `expect()` was not passed an exception type.
        """

        if not issubclass(self.value, BaseException):
            raise TypeError(
                'expect() should have been passed an exception type, '
                'not %r' % self.value
            )

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, self.value):
            self.test.success(
                'block raised a %s' % _qualified_name(self.value)
            )
            return True # suppress the exception
        else:
            if exc_type is None:
                self.test.fail('expected a %s' % _qualified_name(self.value))

            # If another exception was raised, let it propagate, so that
            # it can be recorded as a test error instead of failure.

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.value)

def _qualified_name(exception_type):
    """
    Internal: Return a qualified name for the given type.
    """

    if hasattr(exception_type, '__qualname__'):
        return exception_type.__qualname__
    else:
        module = getattr(exception_type, '__module__', None)
        name = exception_type.__name__

        return (
            '%s.%s' % (module, name)
            if module and module != 'exceptions'
            else name
        )
