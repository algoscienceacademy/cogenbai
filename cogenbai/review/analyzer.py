from typing import List, Dict, Any
import ast
import re

class CodeReviewAnalyzer:
    def __init__(self):
        self.metrics = {
            'complexity': self._analyze_complexity,
            'naming': self._analyze_naming,
            'documentation': self._analyze_documentation,
            'security': self._analyze_security
        }

    def review_code(self, code: str, language: str) -> Dict[str, Any]:
        results = {}
        for metric_name, analyzer in self.metrics.items():
            results[metric_name] = analyzer(code, language)
        return results

    def _analyze_complexity(self, code: str, language: str) -> Dict[str, Any]:
        if language == 'python':
            tree = ast.parse(code)
            return {
                'cyclomatic_complexity': self._count_branches(tree),
                'cognitive_complexity': self._analyze_cognitive_complexity(tree)
            }
        return {}

    def _analyze_naming(self, code: str, language: str) -> Dict[str, List[str]]:
        issues = []
        if language == 'python':
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Name):
                    if not self._is_valid_name(node.id):
                        issues.append(f"Invalid name: {node.id}")
        return {'issues': issues}

    def _analyze_documentation(self, code: str, language: str) -> Dict[str, Any]:
        doc_ratio = len(re.findall(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', code)) / max(1, len(code.splitlines()))
        return {
            'documentation_ratio': doc_ratio,
            'has_module_docstring': code.lstrip().startswith('"""') or code.lstrip().startswith("'''")
        }

    def _analyze_security(self, code: str, language: str) -> Dict[str, List[str]]:
        vulnerabilities = []
        dangerous_patterns = {
            'python': [
                (r'eval\(', 'Dangerous eval() usage'),
                (r'exec\(', 'Dangerous exec() usage'),
                (r'os\.system\(', 'Unsafe system command execution')
            ]
        }
        
        for pattern, message in dangerous_patterns.get(language, []):
            if re.search(pattern, code):
                vulnerabilities.append(message)
        return {'vulnerabilities': vulnerabilities}

    def _count_branches(self, tree: ast.AST) -> int:
        count = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.Try)):
                count += 1
        return count

    def _analyze_cognitive_complexity(self, tree: ast.AST) -> int:
        complexity = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For)):
                complexity += 1
                # Add nesting penalty
                complexity += self._get_nesting_level(node) * 0.5
        return int(complexity)

    def _get_nesting_level(self, node: ast.AST, level: int = 0) -> int:
        parent = getattr(node, 'parent', None)
        if parent is None:
            return level
        return self._get_nesting_level(parent, level + 1)

    def _is_valid_name(self, name: str) -> bool:
        if len(name) < 2:
            return False
        if not name.isidentifier():
            return False
        return True
