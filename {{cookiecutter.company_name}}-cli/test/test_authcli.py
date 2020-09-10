from {{cookiecutter.company_name}}software.cli.main import cli


def test_login_works(runner):
    result = runner.invoke(cli, ["auth", "login"], input="farooq\n1234\n")
    assert "User 'farooq' is logged in." in result.output

def test_logout_works(runner):
    result = runner.invoke(cli, ["auth", "logout"], input="y\n")
    assert "Logged out user 'farooq'." in result.output