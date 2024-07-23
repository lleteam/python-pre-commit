from mock_sum import mock_sum, mock_prod, mock_env_var, mock_secret_var

def test_mock_sum():
    assert mock_sum(1, 2) == 3

def test_mock_prod():
    assert mock_prod(1, 2) == 2

def test_mock_env_var():
    assert mock_env_var() == "foo"

def test_mock_secret_var():
    assert mock_secret_var() == "bar"

