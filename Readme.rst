Chamomile
=========

Chamomile makes it more pleasant to make assertions inside your Python unit
tests. It borrows heavily from Jasmine_'s assertion syntax. Take a look::

    import chamomile

    class ExampleTest(chamomile.Test):
        def test_simple_assertions(self):
            self.expect(12).to_equal(12)
            self.expect(False).to_not_be(0)

            with self.expect(ZeroDivsionError):
                4 / 0

You can easily browse the full list of available assertions in the source_.

.. _Jasmine: http://pivotal.github.com/jasmine/
.. _source: https://github.com/enaeseth/chamomile/blob/master/chamomile/test.py
