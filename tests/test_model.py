import pytest
from cogenbai.core.model import CogenBAI

def test_model_initialization():
    model = CogenBAI()
    assert model is not None
    assert model.device in ["cuda", "cpu"]

def test_code_generation():
    model = CogenBAI()
    prompt = "def calculate_fibonacci(n):"
    result = model.generate_code(prompt)
    assert isinstance(result, str)
    assert len(result) > 0

import unittest
from cogenbai.core.model import CogenBAI

class TestCogenBAI(unittest.TestCase):
    def setUp(self):
        self.model = CogenBAI()
        
    def test_generate_code(self):
        prompt = "Create a function that adds two numbers"
        language = "python"
        result = self.model.generate_code(prompt, language)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
