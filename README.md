# COGENBAI

An advanced AI model for coding experts, created by Algo Science Academy.

## About

COGENBAI is developed by Algo Science Academy under the leadership of Shahrear Hossain Shawon,
a student at International Islamic University Chittagong. This cutting-edge AI model represents
a significant advancement in automated code generation and development assistance.

## Organization

- **Organization**: Algo Science Academy
- **Lead Developer**: Shahrear Hossain Shawon
- **Institution**: International Islamic University Chittagong
- **Version**: 1.0.0

## Features

- Multi-language code generation
- Framework and library integration
- Complete software solutions
- Custom framework creation
- Real-time voiceover assistance
- Cross-platform development support
- Advanced debugging tools
- Collaborative development features

## Installation

```bash
pip install cogenbai
```

## Usage

```python
from cogenbai import CogenBAI, VoiceSynthesizer

# Initialize the model
model = CogenBAI()

# Generate code
code = model.generate_code(
    prompt="Create a REST API endpoint in Python",
    language="python"
)

# Use voice assistance
voice = VoiceSynthesizer()
voice.explain_code(code, "This code creates a REST API endpoint using FastAPI")
```

## API Usage

Start the API server:
```bash
uvicorn cogenbai.api.server:app --reload
```

Generate code via API:
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Create a REST API endpoint", "language": "python"}'
```

Get supported languages:
```bash
curl "http://localhost:8000/supported-languages"
```

## CLI Usage

Generate code from command line:
```bash
cogenbai generate "Create a REST API endpoint" -l python -f fastapi
```

List supported languages:
```bash
cogenbai list-languages
```

## Project Scaffolding

Generate a new project structure:
```bash
cogenbai scaffold my-project -t python_project -d "My awesome project"
```

## Code Optimization

```python
from cogenbai.optimization import CodeOptimizer

optimizer = CodeOptimizer()
optimized_code = optimizer.optimize(code, "python")
complexity = optimizer.analyze_complexity(code)
```

## Collaborative Development

Start a collaborative session:
```python
import asyncio
from cogenbai import CogenBAI
from cogenbai.collaboration import SessionManager

async def main():
    session_manager = SessionManager()
    session = await session_manager.create_session("session1", "user1")
    
    # Join session
    await session_manager.join_session("session1", "user2")
    
    # Update code
    await session_manager.update_code("session1", "print('Hello, World!')")

asyncio.run(main())
```

Connect to WebSocket for real-time updates:
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/session1/user1');
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.type === 'code_update') {
        console.log('Code updated:', data.code);
    }
};
```

## Code Review and Testing

Review code quality:
```python
from cogenbai.review import CodeReviewAnalyzer

reviewer = CodeReviewAnalyzer()
results = reviewer.review_code(code, "python")
print(f"Code quality score: {results['complexity']['cyclomatic_complexity']}")
```

Generate tests:
```python
from cogenbai.testing import TestGenerator

generator = TestGenerator()
test_code = generator.generate_tests(code, "python", "unit")
print("Generated test code:", test_code)
```

## Hardware Requirements

### Model Size Information
- Model Parameters: 16 billion
- Model Size (FP16): ~32GB
- Model Size (FP32): ~64GB

### Minimum Hardware Requirements
- GPU Memory: 40GB (for FP16)
- System RAM: 64GB recommended
- Storage: 100GB free space

### Recommended Hardware
- GPU: NVIDIA A5000 (24GB) or better
- GPU Memory: 48GB or more
- System RAM: 128GB
- Storage: 500GB NVMe SSD

### Supported GPU Configurations
1. Single GPU (High-end):
   - NVIDIA A6000 (48GB)
   - NVIDIA A100 (80GB)

2. Multi-GPU Setup:
   - 2x NVIDIA RTX 4090 (24GB each)
   - 2x NVIDIA A5000 (24GB each)

### Memory Optimization Options
1. FP16 Precision (Default)
   - Model Size: ~32GB
   - Working Memory: ~8GB
   - Total Required: ~40GB

2. 8-bit Quantization
   - Model Size: ~16GB
   - Working Memory: ~4GB
   - Total Required: ~20GB

3. 4-bit Quantization
   - Model Size: ~8GB
   - Working Memory: ~2GB
   - Total Required: ~10GB

## Pushing to Ollama Registry

### 1. Find Your Ollama Public Key

Locate your public key based on your operating system:

- **Windows**: `C:\Users\<username>\.ollama\id_ed25519.pub`
- **macOS**: `~/.ollama/id_ed25519.pub`
- **Linux**: `/usr/share/ollama/.ollama/id_ed25519.pub`

### 2. Configure Registry Access

1. Copy your public key
2. Add it to [Ollama Registry Settings](https://ollama.com/settings)

### 3. Push the Model

#### Option 1: Create and Push New Model
```bash
# Pull base model
ollama pull llama3.2

# Create Modelfile
cat << EOF > Modelfile
FROM llama3.2
PARAMETER temperature 0.7
PARAMETER top_p 0.95
SYSTEM """
You are COGENBAI, an advanced code generation AI.
Focus: Code generation and software development assistance
Created by: Shahrear Hossain Shawon
Organization: Algo Science Academy
"""
EOF

# Create and push model
ollama create -f Modelfile algoscienceacademy/cogenbai
ollama push algoscienceacademy/cogenbai
```

#### Option 2: Push Existing Model
```bash
ollama cp llama3.2 algoscienceacademy/cogenbai
ollama push algoscienceacademy/cogenbai
```

## Usage

```bash
ollama run algoscienceacademy/cogenbai
```

For detailed build and deployment instructions, see [BUILD.md](BUILD.md).

## License

Copyright (c) 2024 Algo Science Academy. All rights reserved.

## Contact

For inquiries and collaboration opportunities:
- Organization: Algo Science Academy
- Lead Developer: Shahrear Hossain Shawon
- Email: contact@algoscienceacademy.com
- Website: https://algoscienceacademy.com
