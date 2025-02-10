import click
from ..core.model import CogenBAI
from ..languages.generator import LanguageGenerator
from ..config import CogenConfig

@click.group()
def cli():
    """COGENBAI Command Line Interface"""
    pass

@cli.command()
@click.argument('prompt')
@click.option('--language', '-l', required=True, help='Target programming language')
@click.option('--framework', '-f', help='Framework to use')
def generate(prompt: str, language: str, framework: str = None):
    """Generate code from a prompt"""
    model = CogenBAI()
    result = model.generate_code(prompt, language)
    click.echo(result)

@cli.command()
def list_languages():
    """List supported programming languages"""
    generator = LanguageGenerator()
    for lang, config in generator.language_configs.items():
        click.echo(f"\n{lang}:")
        click.echo(f"  Frameworks: {', '.join(config['frameworks'])}")
        click.echo(f"  Package Manager: {config['package_manager']}")

@cli.command()
@click.argument('project_name')
@click.option('--template', '-t', default='python_project', help='Project template to use')
@click.option('--description', '-d', default='A new project', help='Project description')
def scaffold(project_name: str, template: str, description: str):
    """Generate a new project scaffold"""
    from ..templates.registry import TemplateRegistry
    registry = TemplateRegistry()
    template_data = registry.get_template('scaffolds', template)
    if not template_data:
        click.echo(f"Template {template} not found")
        return
    
    # Create project structure
    import os
    import json
    structure = json.loads(template_data)['structure']
    base_path = os.path.join(os.getcwd(), project_name)
    
    for path, content in _walk_structure(structure):
        full_path = os.path.join(base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        if isinstance(content, str):
            with open(full_path, 'w') as f:
                f.write(content.replace('${project_name}', project_name)
                               .replace('${project_description}', description))

def _walk_structure(structure, parent=""):
    for name, content in structure.items():
        path = os.path.join(parent, name)
        if isinstance(content, dict):
            yield from _walk_structure(content, path)
        else:
            yield path, content

if __name__ == '__main__':
    cli()
