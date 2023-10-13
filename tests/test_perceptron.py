import pytest
from bin.perceptron import Perceptron
import sys
import os
sys.path.append(".")

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) == 1, "[1,1] Test Failed"
    assert the_perceptron.predict([1,0]) == 1, "[1,0] Test Failed"
    assert the_perceptron.predict([0,1]) == 1, "[0,1] Test Failed"
    assert the_perceptron.predict([0,0]) == 0, "[0,0] Test Failed"


@pytest.mark.xfail(reason="Negative Test")
def test_fail_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) == 0, "[1,1] Test Failed"

@pytest.mark.skipif(os.uname().sysname != 'Linux', reason="Only Supported on Linux")
def test_os_perceptron():
    total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])

    assert total_memory >= 5, "Not enough total memory"
    assert used_memory > 100, "Too much used memory"
    assert free_memory < 100, "Not enough free memory"

@pytest.mark.skip(reason="This test is not ready for prime time")
def test_skip_perceptron():
    x = 1

    assert x == 5, "Bogus Test"

@pytest.mark.parametrize(
    "trainingset, labels, expected",
    [
        ([[1,1],[1,0],[0,1],[0,0]], [1,1,1,0], [1,1,1,0]),
        ([[1,2],[1,2],[0,3],[0,4]], [1,1,1,1], [1,1,1,1]),
        ([[2,2],[3,2],[1,3],[0,4]], [1,1,1,1], [1,1,1,1]),
        ([[1,3],[0,5],[1,4],[0,4]], [1,1,1,1], [1,1,1,1]),
        ([[1,1],[2,2],[3,3],[3,4]], [1,0,0,1], [1,0,0,1]),
        ([[1,1],[3,3],[2,2],[4,4]], [1,1,1,1], [1,1,1,1]),
    ]
)
def test_param_perceptron(trainingset, labels, expected):
    the_perceptron = Perceptron()
    the_perceptron.train(trainingset,labels)

    predicted = []
    for my_input in trainingset:
        predicted.append(the_perceptron.predict(my_input))
    
    assert predicted == expected, "Predicted values did not match expected values"



