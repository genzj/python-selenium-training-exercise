import unittest
from oktest import test, ok, NG

def fn():
    raise RuntimeError()


class FooTest(unittest.TestCase):

   @test("1 + 1 should be 2")
   def _(self):
        ok (1+1) == 2          # same as assertEqual(2, 1+1)

   @test("other examples")
   def _(self):
        s = 'foo'
        ok (s) == 'foo'        # same as assertEqual(s, 'foo')
        s = 'bar'
        ok (s) != 'foo'        # same as assertNotEqual(s, 'foo')
        n = 100
        ok (n) > 0             # same as assertTrue(n > 0)
        ok (fn).raises(RuntimeError)  # same as assertRaises(Error, fn)
        ok ([]).is_a(list)     # same as assertTrue(isinstance([], list))
        NG ([]).is_a(tuple)    # same as assertTrue(not isinstance([], tuple))
        ok ('test_sample.py').is_file() # same as assertTrue(os.path.isfile('A.txt'))
        NG ('test_sample.py').is_dir()  # same as assertTrue(not os.path.isdir('A.txt'))

