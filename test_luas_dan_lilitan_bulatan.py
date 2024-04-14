import luas_dan_lilitan_bulatan
import pytest

def test_luas_dan_lilitan_bulatan(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    luas_dan_lilitan_bulatan.main()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Luas bulatan ialah     cm2.
                                    Ukuran lilitan ialah    cm"
