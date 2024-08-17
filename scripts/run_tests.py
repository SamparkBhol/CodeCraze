# run_tests.py

import os
import subprocess
import unittest

def discover_and_run_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_dir = os.path.join(os.path.dirname(__file__), '../tests')
    suite.addTests(loader.discover(test_dir))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("All tests passed successfully!")
    else:
        print(f"Tests failed: {len(result.failures)} failures, {len(result.errors)} errors.")

def run_lint():
    print("Running linting with flake8...")
    subprocess.run(["flake8", "--max-line-length=120", "src", "tests", "scripts"])

def run_coverage():
    print("Generating test coverage report...")
    subprocess.run(["coverage", "run", "--source=src", "-m", "unittest", "discover", "-s", "tests"])
    subprocess.run(["coverage", "report", "-m"])
    subprocess.run(["coverage", "html"])

if __name__ == "__main__":
    print("Running all unit tests...")
    discover_and_run_tests()

    print("\nRunning lint checks...")
    run_lint()

    print("\nRunning test coverage...")
    run_coverage()

    print("\nAll checks complete.")
