from solutions.HLO import hello_solution

def test_hello():
    assert hello_solution.hello("test_input") == "Hello, test_input!"