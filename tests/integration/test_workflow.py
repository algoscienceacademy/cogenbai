import unittest
from cogenbai import CogenBAI, CodeAnalyzer, LanguageGenerator

class TestIntegrationWorkflow(unittest.TestCase):
    def setUp(self):
        self.model = CogenBAI()
        self.analyzer = CodeAnalyzer()
        self.generator = LanguageGenerator()

    def test_complete_workflow(self):
        # Generate code
        code = self.model.generate_code(
            "Create a function to sort a list",
            "python"
        )
        self.assertIsNotNone(code)

        # Analyze generated code
        issues = self.analyzer.analyze_python(code)
        self.assertIsInstance(issues, list)

        # Check language support
        config = self.generator.get_language_config("python")
        self.assertIsNotNone(config)
        self.assertIn("frameworks", config)

if __name__ == '__main__':
    unittest.main()
