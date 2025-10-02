# 🧹 Pylint Setup and Usage Guide

- This document explains how to configure and run `pylint` and `pytest` to check for code quality in a Python FastAPI project

## 1. Install Pylint

```ini
uv add pylint
```

## 2. Generate a Pylint Configuration File

- This is  an optional task
- We can generate a default configuration file for customization:

    ```ini
    pylint --generate-rcfile > .pylintrc
    ```

- Adjust max line length:

    ```ini
    [FORMAT]
    max-line-length=88
    ```

- Ignore missing docstring warnings (not recommended):

    ```ini
    [MESSAGES CONTROL]
    disable=C0114,C0115,C0116
    ```


## 3. Run Pylint on API and Test files

- Use this command ot lint our main api and test files
- This shows the output in the terminal and save it into a file

```ini
source .venv/bin/activate
pylint app/main.py tests/ | tee lint-results.txt
```

- `main.py`: our FastAPI source file
- `tests/`: our test folder
- `tee`: shows the output and saves it to file called `lint-results.txt`
- Add `lint-results.txt` to `.gitignore`


## Notes:

- Fix high priority issues: unused imports, wrong indentation
- Use docstrings to suppress missing docstring warnings
- Review and refactor based on suggestions to maintain high code quality


# 🧪 PyTest Setup and Usage Guide

- This document provides a structured overview for setting up and running unit tests using `pytest` in a python project

## 1. Install the required packages

- Intall the main package:

    ```ini
    uv add pytest
    ```

- For FastAPI testing, we need to install this:

    ```ini
    uv add httpx
    ```

## 2. Project Structure

```markdown
project/
├── app/
│   ├── __init__.py
│   └── main.py
├── scripts/
│   └── run_tests.sh
├── tests/
│   └── test_main.py
├── pytest.ini
├── pyproject.toml
```

## 3. Create a Pytest config file: `pytest.ini`

```ini
# pytest.ini
[pytest]
addopts = -v --junitxml=results.xml
testpaths = tests
```

## 4. Add your test cases:

- Here is a sample test case:

    ```python
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    def test_read_root():
        response = client.get("/")
        assert response.status_code == 200
        assert response.text == "Hello, World! Status: OK"
    ```

## 5. Running Tests

- Run the command from the root directory

    ```ini
    PYTHONPATH=. pytest --color=yes | tee test-results.txt
    ```

- `PYTHONPATH=.`: ensures the app package is discoverable
- `--color=yes`: keeps the green/red output
- `tee`: displays results in terminal and saves them to a file

## 6. Output Files

- `test-results.txt`: Plain text results with terminal color codes
- `results.xml`: Machine-readable test report (useful in CI/CD)

## Notes:

- All test filenames should begin with `test_`
- All test functions should also begin with `test_`
- Use `pytest -k <test_name>` to run a specific test
- Use `pytest --maxfail=1`  to stop after first failure