# COGENBAI Build Guide

This guide explains how to build, deploy, and use COGENBAI from source, including Ollama integration.

## Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended)
- Git
- Docker (optional)
- Ollama

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/algoscienceacademy/cogenbai.git
cd cogenbai
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e ".[dev]"
```

## Building the Model

1. Download the base model:
```bash
python scripts/download_model.py --model codegen-16B-multi
```

2. Train or fine-tune (optional):
```bash
python scripts/train.py \
    --model-path models/codegen-16B-multi \
    --train-data data/code_samples \
    --epochs 3
```

## Ollama Integration

1. Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Create Modelfile:
```bash
# Create Modelfile
FROM codellama
PARAMETER temperature 0.7
PARAMETER top_p 0.95
SYSTEM """
You are COGENBAI, an advanced code generation AI created by Algo Science Academy.
Created by: Shahrear Hossain Shawon
Organization: Algo Science Academy
"""

# Build the model
ollama create cogenbai -f Modelfile
```

3. Deploy with Ollama:
```bash
ollama run cogenbai
```

## Docker Deployment

1. Build Docker image:
```bash
docker build -t cogenbai:latest .
```

2. Run container:
```bash
docker run -d -p 8000:8000 cogenbai:latest
```

## Project Structure

```
cogenbai/
├── cogenbai/
│   ├── core/           # Core model implementation
│   ├── languages/      # Language-specific generators
│   ├── templates/      # Code templates
│   ├── collaboration/  # Real-time collaboration
│   ├── review/        # Code review tools
│   ├── testing/       # Test generation
│   └── api/           # REST API
├── tests/             # Unit and integration tests
├── scripts/           # Build and utility scripts
└── docs/             # Documentation
```

## Configuration

1. Create configuration file:
```yaml
# config.yaml
model:
  name: codegen-16B-multi
  device: cuda
  max_length: 1024
  temperature: 0.7

language:
  default: python
  style:
    python: black
    javascript: prettier
```

2. Apply configuration:
```python
from cogenbai import CogenConfig
config = CogenConfig.load('config.yaml')
```

## API Deployment

1. Start the API server:
```bash
uvicorn cogenbai.api.server:app --host 0.0.0.0 --port 8000
```

2. Access API documentation:
```
http://localhost:8000/docs
```

## Testing

Run the test suite:
```bash
pytest tests/
```

## Development Workflow

1. Create new feature branch:
```bash
git checkout -b feature/new-feature
```

2. Make changes and run tests:
```bash
pytest tests/
black cogenbai/
```

3. Build documentation:
```bash
mkdocs build
```

## Performance Optimization

1. Enable CUDA acceleration:
```python
model = CogenBAI(device="cuda")
```

2. Batch processing:
```python
config = CogenConfig(batch_size=4, num_workers=2)
```

## Monitoring

1. Start Prometheus metrics:
```bash
docker-compose up -d prometheus grafana
```

2. Access dashboard:
```
http://localhost:3000
```

## Troubleshooting

Common issues and solutions:

1. CUDA Out of Memory:
```bash
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
```

2. Model Loading Issues:
```python
import torch
torch.cuda.empty_cache()
```

## Security Considerations

1. API Authentication:
```python
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

2. Rate Limiting:
```python
from fastapi_limiter import FastAPILimiter
await FastAPILimiter.init(redis)
```

## Production Deployment

1. Using Kubernetes:
```bash
kubectl apply -f k8s/
```

2. Load Balancing:
```bash
kubectl apply -f k8s/ingress.yaml
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

## Support

For support and questions:
- Email: contact@algoscienceacademy.com
- GitHub Issues: [Create Issue](https://github.com/algoscienceacademy/cogenbai/issues)

## License

Copyright (c) 2024 Algo Science Academy. All rights reserved.
