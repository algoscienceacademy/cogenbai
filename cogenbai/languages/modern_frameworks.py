from typing import Dict, Optional

class ModernFrameworkSupport:
    def __init__(self):
        self.framework_configs = {
            "astro": {
                "package_manager": "npm/pnpm",
                "setup_command": "npm create astro@latest",
                "build_command": "npm run build",
                "dev_command": "npm run dev",
                "testing": ["vitest", "playwright"],
                "deployment": ["vercel", "netlify", "cloudflare"]
            },
            "sveltekit": {
                "package_manager": "npm/pnpm",
                "setup_command": "npm create svelte@latest",
                "build_command": "npm run build",
                "dev_command": "npm run dev",
                "testing": ["vitest", "playwright"],
                "deployment": ["vercel", "netlify"]
            },
            "remix": {
                "package_manager": "npm/pnpm",
                "setup_command": "npx create-remix@latest",
                "build_command": "npm run build",
                "dev_command": "npm run dev",
                "testing": ["vitest", "cypress"],
                "deployment": ["vercel", "fly.io"]
            },
            "nextjs": {
                "package_manager": "npm/pnpm",
                "setup_command": "npx create-next-app@latest",
                "build_command": "npm run build",
                "dev_command": "npm run dev",
                "testing": ["jest", "cypress"],
                "deployment": ["vercel", "netlify"]
            }
        }
        
    def get_deployment_config(self, framework: str, platform: str) -> Dict:
        if framework not in self.framework_configs:
            raise ValueError(f"Unsupported framework: {framework}")
            
        if platform not in self.framework_configs[framework]["deployment"]:
            raise ValueError(f"Unsupported deployment platform: {platform}")
            
        return {
            "platform": platform,
            "framework": framework,
            "config": self._get_platform_config(framework, platform)
        }
    
    def _get_platform_config(self, framework: str, platform: str) -> Dict:
        configs = {
            "vercel": {
                "file": "vercel.json",
                "content": {
                    "buildCommand": self.framework_configs[framework]["build_command"],
                    "devCommand": self.framework_configs[framework]["dev_command"],
                    "framework": framework
                }
            },
            "netlify": {
                "file": "netlify.toml",
                "content": f"""
[build]
command = "{self.framework_configs[framework]['build_command']}"
publish = "dist"
"""
            }
        }
        return configs.get(platform, {})
