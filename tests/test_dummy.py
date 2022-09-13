from src.dummy import dummy 

def test_dummy()->None:
    assert(dummy() == "hello, world!")