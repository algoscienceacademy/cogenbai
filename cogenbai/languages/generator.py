from typing import Dict, Optional

class LanguageGenerator:
    def __init__(self):
        self.language_configs: Dict[str, dict] = {
            "python": {
                "frameworks": ["django", "flask", "fastapi", "pyramid", "aiohttp", "tornado"],
                "package_manager": "pip/poetry/conda",
                "file_extension": ".py",
                "testing_frameworks": ["pytest", "unittest", "nose"],
                "doc_format": "docstring",
            },
            "javascript": {
                "frameworks": [
                    "react", "vue", "angular", "next.js", "nuxt.js", "express",
                    "astro", "sveltekit", "remix", "solid", "qwik"
                ],
                "package_manager": "npm/yarn/pnpm",
                "file_extension": ".js",
                "testing_frameworks": ["jest", "vitest", "cypress", "playwright"],
                "doc_format": "jsdoc",
                "bundlers": ["vite", "webpack", "rollup", "esbuild", "turbopack"]
            },
            "typescript": {
                "frameworks": [
                    "react", "vue", "angular", "next.js", "nest.js",
                    "astro", "sveltekit", "remix", "solid", "qwik"
                ],
                "package_manager": "npm/yarn/pnpm",
                "file_extension": ".ts",
                "testing_frameworks": ["jest", "vitest", "cypress", "playwright"],
                "doc_format": "tsdoc",
                "bundlers": ["vite", "webpack", "rollup", "esbuild", "turbopack"]
            },
            "rust": {
                "frameworks": ["actix", "rocket", "warp", "yew"],
                "package_manager": "cargo",
                "file_extension": ".rs",
                "testing_frameworks": ["cargo test"],
                "doc_format": "rustdoc",
            },
            "go": {
                "frameworks": ["gin", "echo", "fiber", "buffalo"],
                "package_manager": "go mod",
                "file_extension": ".go",
                "testing_frameworks": ["testing"],
                "doc_format": "godoc",
            },
            "java": {
                "frameworks": ["spring", "quarkus", "micronaut", "jakarta ee"],
                "package_manager": "maven/gradle",
                "file_extension": ".java",
                "testing_frameworks": ["junit", "testng"],
                "doc_format": "javadoc",
            },
            "kotlin": {
                "frameworks": ["spring", "ktor", "compose"],
                "package_manager": "maven/gradle",
                "file_extension": ".kt",
                "testing_frameworks": ["junit", "kotlintest"],
                "doc_format": "kdoc",
            },
            "cpp": {
                "frameworks": ["qt", "boost", "opencv", "llvm"],
                "package_manager": "vcpkg/conan/cmake",
                "file_extension": ".cpp",
                "testing_frameworks": ["gtest", "catch2", "doctest"],
                "doc_format": "doxygen",
                "ide_support": ["visual-studio", "clion", "qt-creator"]
            },
            "dart": {
                "frameworks": ["flutter", "shelf", "aqueduct"],
                "package_manager": "pub",
                "file_extension": ".dart",
                "testing_frameworks": ["test", "flutter_test"],
                "doc_format": "dartdoc",
                "ide_support": ["android-studio", "vscode"]
            },
            "swift": {
                "frameworks": ["swiftui", "vapor", "perfect"],
                "package_manager": "swift-package-manager/cocoapods",
                "file_extension": ".swift",
                "testing_frameworks": ["xctest"],
                "doc_format": "markdown",
                "ide_support": ["xcode"]
            },
            "matlab": {
                "frameworks": ["simulink", "app-designer"],
                "package_manager": "matlab-package-installer",
                "file_extension": ".m",
                "testing_frameworks": ["matlab.unittest"],
                "doc_format": "matlab-doc",
                "ide_support": ["matlab-ide"]
            },
            "bash": {
                "frameworks": ["bash-it", "oh-my-bash"],
                "package_manager": "apt/yum/brew",
                "file_extension": ".sh",
                "testing_frameworks": ["bats", "shunit2"],
                "doc_format": "man-pages",
                "ide_support": ["vscode", "bash-ide"]
            }
        }
        
    def get_language_config(self, language: str) -> Optional[dict]:
        return self.language_configs.get(language.lower())
    
    def generate_boilerplate(self, language: str, framework: str) -> str:
        config = self.get_language_config(language)
        if not config or framework not in config["frameworks"]:
            raise ValueError(f"Unsupported language or framework: {language}/{framework}")
            
        # Add framework-specific boilerplate generation here
        return f"// Generated {framework} boilerplate for {language}"
    
    def generate_hello_world(self, language: str) -> str:
        templates = {
            "python": 'print("Hello, World!")',
            "javascript": 'console.log("Hello, World!");',
            "typescript": 'console.log("Hello, World!");',
            "rust": 'fn main() {\n    println!("Hello, World!");\n}',
            "go": 'package main\n\nfunc main() {\n    println("Hello, World!")\n}',
            "java": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
            "kotlin": 'fun main() {\n    println("Hello, World!")\n}'
        }
        return templates.get(language.lower(), "// Language not supported")
