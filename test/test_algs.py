import numpy as np
from Homework1sub import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))


def test_insertionsort():
    # Actually test insertionsort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1]).tolist()
    rho = [100,84.5,9,0.0045]
    epsilon = []
    sigma = [1]
    delta = [9, 9, 8, 8, 7, 7, 1, 2, 1]
    omega = [5, 4, 3, 2, 1]
    alpha = [0, 9, 8, 1]
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    algs.insertionsort(x)
    assert np.array_equal(algs.insertionsort(rho), np.array([0.0045, 9, 84.5, 100]).tolist())
    assert np.array_equal(algs.insertionsort(epsilon), np.array([]).tolist())
    assert np.array_equal(algs.insertionsort(sigma), np.array([1]).tolist())
    assert np.array_equal(algs.insertionsort(delta), np.array([1, 1, 2, 7, 7, 8, 8, 9, 9]).tolist())
    assert np.array_equal(algs.insertionsort(omega), np.array([1, 2, 3, 4, 5]).tolist())
    assert np.array_equal(algs.insertionsort(alpha), np.array([0, 1, 8, 9]).tolist())
    
    
def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1])
    rho = [100,84.5,9,0.0045]
    epsilon = []
    sigma = [1]
    delta = [9, 9, 8, 8, 7, 7, 1, 2, 1]
    omega = [5, 4, 3, 2, 1]
    alpha = [0, 9, 8, 1]
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    algs.bubblesort(x)

def test_quicksort():

    x = np.array([1,2,4,0,1]).tolist()
    rho = [100,84.5,9,0.0045]
    epsilon = []
    sigma = [1]
    delta = [9, 9, 8, 8, 7, 7, 1, 2, 1]
    omega = [5, 4, 3, 2, 1]
    alpha = [0, 9, 8, 1]
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quicksort(x)
