# Fine-Tuning Language Models

This directory contains implementations and examples of fine-tuning different Large Language Models (LLMs). Each subfolder focuses on a specific model and fine-tuning approach.

## Directory Structure

```
fine_tuning/
├── finetune_gpt/
│   ├── README.md
│   └── openai_ft.ipynb
└── finetune_llama/
    ├── README.md
    ├── requirements.txt
    └── finetune_Llama.ipynb
```

## Available Fine-Tuning Examples

### 1. GPT Fine-Tuning (`finetune_gpt/`)
- Demonstrates fine-tuning using OpenAI's API
- Focuses on prompt engineering and optimization
- Uses JSONL format for training data
- Suitable for those working with OpenAI's models

### 2. Llama 2 Fine-Tuning (`finetune_llama/`)
- Implements PEFT (Parameter-Efficient Fine-Tuning) with LoRA
- Shows how to fine-tune on consumer hardware
- Includes complete environment setup
- Demonstrates model publishing to Hugging Face Hub

## Getting Started

Each subfolder contains:
- Detailed README with specific instructions
- Jupyter notebooks with step-by-step implementations
- Required dependencies and setup guides

Choose the appropriate folder based on your model and use case:
- For OpenAI GPT models: Use `finetune_gpt/`
- For Llama 2 models: Use `finetune_llama/`

## Prerequisites

- Basic understanding of machine learning and NLP
- Python programming experience
- Access to appropriate model APIs or weights
- GPU access (especially for Llama 2 fine-tuning) 