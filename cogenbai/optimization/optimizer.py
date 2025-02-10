from typing import List, Dict, Any
import ast
import autopep8
import black
from yapf.yapflib.yapf_api import FormatCode

class CodeOptimizer:
    def __init__(self):
        self.formatters = {
            'python': self._optimize_python,
            'javascript': self._optimize_javascript
        }

    def optimize(self, code: str, language: str) -> str:
        optimizer = self.formatters.get(language.lower())
        if not optimizer:
            return code
        return optimizer(code)

    def _optimize_python(self, code: str) -> str:
        # First pass: Basic PEP 8 formatting
        code = autopep8.fix_code(code)
        
        try:
            # Second pass: Black formatting
            code = black.format_str(code, mode=black.FileMode())
        except:
            pass

        try:
            # Third pass: YAPF formatting
            code, _ = FormatCode(code)
        except:
            pass

        return code

    def _optimize_javascript(self, code: str) -> str:
        # Add JavaScript optimization logic here
        return code

    def analyze_complexity(self, code: str) -> Dict[str, Any]:
        try:
            tree = ast.parse(code)
            return {
                'cyclomatic_complexity': self._calculate_complexity(tree),
                'line_count': len(code.splitlines()),
                'function_count': len([node for node in ast.walk(tree) 
                                    if isinstance(node, ast.FunctionDef)])
            }
        except:
            return {}

    def _calculate_complexity(self, tree: ast.AST) -> int:
        complexity = 1
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
        return complexity
