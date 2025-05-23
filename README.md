# Git Repository Analysis Tool

A powerful tool for analyzing Git repositories using LLM-powered insights. This tool provides detailed analysis of repository patterns, milestones, technical challenges, team dynamics, and more.

## Installation

```bash
pip install git-analyzer
```

## Usage

### Basic Analysis

```bash
git-analyzer https://github.com/username/repo.git --format markdown
```

### Analysis with Date Range

```bash
git-analyzer https://github.com/username/repo.git \
    --start-date 2023-01-01 \
    --end-date 2024-03-20 \
    --format markdown
```

### OpenAI API Key Configuration

You can provide your OpenAI API key in three ways:

1. Command line argument:
```bash
git-analyzer https://github.com/username/repo.git --openai-key your-api-key
```

2. Environment variable:
```bash
export OPENAI_API_KEY=your-api-key
git-analyzer https://github.com/username/repo.git
```

3. .env file:
Create a `.env` file in your working directory:
```
OPENAI_API_KEY=your-api-key
```

### Custom Prompts

You can customize the analysis prompts by providing a JSON file:

```bash
git-analyzer https://github.com/username/repo.git \
    --custom-prompts path/to/prompts.json
```

Example prompts.json:
```json
{
    "system_prompt": "Your custom system prompt",
    "analysis_prompts": {
        "overview": "Your custom overview prompt",
        "milestones": "Your custom milestones prompt",
        "technical_achievements": "Your custom technical achievements prompt",
        "challenges": "Your custom challenges prompt",
        "team_dynamics": "Your custom team dynamics prompt",
        "code_quality": "Your custom code quality prompt",
        "recommendations": "Your custom recommendations prompt"
    }
}
```

### Advanced Options

```bash
git-analyzer https://github.com/username/repo.git \
    --start-date 2023-01-01 \
    --end-date 2024-03-20 \
    --format markdown \
    --output-dir custom_reports \
    --openai-key your-api-key \
    --model gpt-4 \
    --custom-prompts path/to/prompts.json
```

## Output

The tool generates a comprehensive report in either JSON or Markdown format, including:

- Repository overview
- Development patterns
- Key milestones
- Technical achievements
- Challenges and solutions
- Team dynamics
- Code quality assessment
- Recommendations

Reports are saved in the specified output directory (default: `reports/`).

## Requirements

- Python 3.7+
- Git
- OpenAI API key (for LLM analysis)

## Dependencies

- gitpython
- openai
- python-dotenv
- argparse