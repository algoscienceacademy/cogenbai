import torch
from torch import nn
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Optional, Dict, Any
from datetime import datetime
from ..languages.generator import LanguageGenerator

class CogenBAI(nn.Module):
    """
    CogenBAI: Advanced Code Generation Model
    
    Created by Algo Science Academy
    Lead Developer: Shahrear Hossain Shawon
    Organization: Algo Science Academy
    Academic Background: International Islamic University Chittagong
    
    This model is designed to generate high-quality code across multiple programming
    languages with support for various frameworks and coding patterns. It represents
    a significant advancement in AI-assisted software development, combining modern
    language support with intelligent code generation capabilities.
    
    Copyright (c) 2024 Algo Science Academy
    All rights reserved.
    """

    # Model metadata
    __author__ = "Shahrear Hossain Shawon"
    __organization__ = "Algo Science Academy"
    __version__ = "1.0.0"
    __license__ = "Proprietary"
    __copyright__ = f"Copyright (c) {datetime.now().year} Algo Science Academy"
    __contact__ = {
        "organization": "Algo Science Academy",
        "developer": "Shahrear Hossain Shawon",
    }

    def __init__(self, model_name: str = "codegen-16B-multi", device: str = "cuda"):
        """
        Initialize the CogenBAI model.
        
        Developed by Algo Science Academy under the leadership of
        Shahrear Hossain Shawon from International Islamic University Chittagong.
        """
        super().__init__()
        self.device = "cuda" if torch.cuda.is_available() and device == "cuda" else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.lang_generator = LanguageGenerator()
        self.project_tracker = ProjectTracker()
        from ..languages.modern_frameworks import ModernFrameworkSupport
        self.modern_frameworks = ModernFrameworkSupport()
        
    @classmethod
    def get_model_info(cls) -> Dict[str, Any]:
        """
        Get information about the model and its creators.
        """
        return {
            "model_name": "CogenBAI",
            "version": cls.__version__,
            "author": cls.__author__,
            "organization": cls.__organization__,
            "institution": cls.__contact__["institution"],
            "license": cls.__license__,
            "copyright": cls.__copyright__,
            "contact": cls.__contact__
        }

    def generate_code(self, prompt: str, language: str, 
                     framework: Optional[str] = None,
                     max_length: int = 1024,
                     temperature: float = 0.7,
                     top_p: float = 0.95) -> str:
        """
        Generate code based on the given prompt and parameters.
        
        Args:
            prompt (str): The coding task description
            language (str): Target programming language
            framework (Optional[str]): Specific framework to use
            max_length (int): Maximum length of generated code
            temperature (float): Sampling temperature
            top_p (float): Nucleus sampling parameter
            
        Returns:
            str: Generated code
        """
        # Validate language and framework
        lang_config = self.lang_generator.get_language_config(language)
        if not lang_config:
            raise ValueError(f"Unsupported language: {language}")
        
        if framework and framework not in lang_config["frameworks"]:
            raise ValueError(f"Unsupported framework {framework} for {language}")
        
        # Prepare prompt with language and framework context
        context = f"Generate {language} code"
        if framework:
            context += f" using {framework}"
        formatted_prompt = f"{context}:\n{prompt}\n\nSolution:\n"
        
        # Generate code
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            inputs.input_ids,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id,
            num_return_sequences=1
        )
        
        generated_code = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return self._format_code(generated_code, language)
    
    def continue_project(self, project_id: str, new_feature_description: str) -> str:
        """Continue development of an existing project."""
        project = self.project_tracker.get_project(project_id)
        if not project:
            raise ValueError(f"Project {project_id} not found")

        # Generate context from existing code
        context = self._build_project_context(project)
        
        # Generate new code
        new_code = self.generate_code(
            prompt=f"{context}\n\nAdd feature: {new_feature_description}",
            language=project.language,
            framework=project.framework
        )

        # Update project state
        project.code_snippets[new_feature_description] = new_code
        project.last_modified = datetime.now()
        self.project_tracker.update_project(project_id, {
            "code_snippets": json.dumps(project.code_snippets),
            "last_modified": project.last_modified.isoformat()
        })

        return new_code

    def generate_deployment_config(self, project_id: str, platform: str) -> Dict[str, Any]:
        """Generate deployment configuration for modern frameworks."""
        project = self.project_tracker.get_project(project_id)
        if not project:
            raise ValueError(f"Project {project_id} not found")

        try:
            deploy_config = self.modern_frameworks.get_deployment_config(
                project.framework, platform
            )
            return deploy_config
        except ValueError as e:
            raise ValueError(f"Deployment configuration failed: {str(e)}")

    def _build_project_context(self, project: ProjectState) -> str:
        """Build context from existing project code."""
        context = f"Project: {project.name}\nLanguage: {project.language}\nFramework: {project.framework}\n\n"
        context += "Existing code:\n"
        for feature, code in project.code_snippets.items():
            context += f"\n# Feature: {feature}\n{code}\n"
        return context

    def _format_code(self, code: str, language: str) -> str:
        """Format the generated code according to language standards."""
        # Remove the prompt from the generated code
        if "Solution:" in code:
            code = code.split("Solution:")[-1].strip()
        
        # Add language-specific formatting
        if language == "python":
            import black
            try:
                return black.format_str(code, mode=black.FileMode())
            except:
                return code
                
        return code
