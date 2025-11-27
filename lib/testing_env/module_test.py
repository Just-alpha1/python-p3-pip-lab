from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8

def requests_version():
    return "2.27.1"

def python_version()
    return "3.10.2" 

def pytest_version():
    return "7.1.3"
