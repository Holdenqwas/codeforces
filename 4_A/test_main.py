import pytest
import main


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (8, "YES"),
        (7, "NO"),
        (1, "NO"),
        (100, "YES"),
        (2, "NO"),
    ],
)
def test_func(test_input, expected):
    assert main.splite(test_input) == expected


def read_file(path: str = 'testcase.txt'):
    with open('testcase.txt', 'r') as f:
        line = f.readline()
        yield line
    
def test_main(capsys):
    main.input = lambda: next(read_file())
    # main.input = lambda: open('testcase.txt', 'r').read()
    main.main()

    captured = capsys.readouterr()
    assert captured.out == "YES\n"
    assert captured.err == ""
