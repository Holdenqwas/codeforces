import io
import pytest
import main


# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         (8, "YES"),
#         (7, "NO"),
#         (1, "NO"),
#         (100, "YES"),
#         (2, "NO"),
#     ],
# )
# def test_func(test_input, expected):
#     assert main.splite(test_input) == expected


def read_file(path: str = 'testcase.txt'):
    with open('testcase.txt', 'r') as f:
        a = f.readline()
        b = f.readline()
        f.readline()
        yield b
    
def test_main(capsys, monkeypatch):

    values = lambda: next(read_file())
    val = values()
    monkeypatch.setattr('sys.stdin', io.StringIO(f"1\n1\n{val[:-2]}"))
    # main.input = lambda: ["1\n", "1\n",f"{val[:-1]}"]
    # main.input = lambda: open('testcase.txt', 'r').read()
    main.main()

    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "YES\n" if val[-1].endswith('y\n') else "NO\n"
    assert captured.err == ""
