from dataclasses import dataclass, field
from typing import Dict, Any, List
import json
import os

@dataclass
class CogenConfig:
    # Model settings
    model_name: str = "codegen-16B-multi"
    max_length: int = 2048
    temperature: float = 0.8
    top_p: float = 0.95
    
    # Language settings
    default_language: str = "python"
    supported_languages: List[str] = field(default_factory=lambda: [
        "python",
        "javascript",
        "typescript",
        "java",
        "rust",
        "go",
        "cpp",
        "csharp",
        "php",
        "ruby",
        "kotlin",
        "swift",
        "dart"  # Added dart
    ])
    
    code_style: Dict[str, str] = field(default_factory=lambda: {
        "python": "black",
        "javascript": "prettier",
        "typescript": "prettier",
        "java": "google",
        "rust": "rustfmt",
        "go": "gofmt",
        "cpp": "clang-format",
        "csharp": "dotnet-format",
        "php": "php-cs-fixer",
        "ruby": "rubocop",
        "kotlin": "ktlint",
        "swift": "swiftformat",
        "dart": "dart format"  # Added dart formatter
    })
    
    language_extensions: Dict[str, List[str]] = field(default_factory=lambda: {
        "python": [".py", ".pyi", ".pyx"],
        "javascript": [".js", ".jsx", ".mjs"],
        "typescript": [".ts", ".tsx"],
        "java": [".java"],
        "rust": [".rs"],
        "go": [".go"],
        "cpp": [".cpp", ".hpp", ".cc", ".h"],
        "csharp": [".cs"],
        "php": [".php"],
        "ruby": [".rb"],
        "kotlin": [".kt"],
        "swift": [".swift"],
        "dart": [".dart"]  # Added dart extension
    })
    
    # Generation settings
    add_comments: bool = True
    add_type_hints: bool = True
    add_docstrings: bool = True
    
    # Performance settings
    use_gpu: bool = True
    batch_size: int = 1
    num_workers: int = 4
    
    @classmethod
    def load(cls, config_path: str) -> 'CogenConfig':
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config_dict = json.load(f)
            return cls(**config_dict)
        return cls()
    
    def save(self, config_path: str):
        with open(config_path, 'w') as f:
            json.dump(self.__dict__, f, indent=2)
