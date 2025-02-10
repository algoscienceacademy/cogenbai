from typing import Dict, Optional
import json
import os

class TemplateRegistry:
    def __init__(self):
        self.templates: Dict[str, Dict] = {}
        self.template_dir = os.path.join(os.path.dirname(__file__), 'data')
        self._load_templates()

    def _load_templates(self):
        if not os.path.exists(self.template_dir):
            os.makedirs(self.template_dir)
            return

        for filename in os.listdir(self.template_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.template_dir, filename), 'r') as f:
                    lang_templates = json.load(f)
                    self.templates.update(lang_templates)

    def get_template(self, language: str, template_name: str) -> Optional[str]:
        return self.templates.get(language, {}).get(template_name)

    def add_template(self, language: str, name: str, content: str):
        if language not in self.templates:
            self.templates[language] = {}
        self.templates[language][name] = content
        self._save_templates(language)

    def _save_templates(self, language: str):
        filepath = os.path.join(self.template_dir, f"{language}.json")
        with open(filepath, 'w') as f:
            json.dump({language: self.templates[language]}, f, indent=2)
