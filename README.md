# Python Agent Template

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Poetry](https://img.shields.io/badge/poetry-dependency%20management-blue)
![LangChain](https://img.shields.io/badge/LangChain-AI%20Agents-green)
![Test Coverage](https://img.shields.io/badge/coverage-0%25-red)
![License](https://img.shields.io/badge/license-MIT-green)

A **production-ready** template for building AI agents with LangChain, LangGraph, and comprehensive tooling.

> **⚠️ This is a template repository.** Replace this README with your project-specific documentation.

## 🎯 Features

This template provides:

- ✅ **LangChain & LangGraph** - Ready-to-use agent framework
- ✅ **Poetry** - Modern Python dependency management
- ✅ **Pre-commit Hooks** - Automated code quality checks
- ✅ **Testing Setup** - pytest with coverage reporting
- ✅ **Code Quality Tools** - black, isort, pylint, mypy
- ✅ **Project Structure** - Production-ready folder organization
- ✅ **Documentation** - Template docs and contributing guidelines
- ✅ **CI/CD Ready** - GitHub Actions workflows included

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)
- Git

### Installation

```bash
# Clone this template (or use "Use this template" on GitHub)
git clone <your-repo-url> my-agent-project
cd my-agent-project

# Install dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install

# Copy environment template
cp .env.example .env
# Edit .env with your API keys

# Run tests to verify setup
poetry run pytest tests/
```

---

## 📁 Project Structure

```
python-agent-template/
├── src/                               # Core business logic
│   ├── agent/                        # Agent module
│   │   ├── __init__.py              # Public API exports
│   │   ├── state.py                 # Pydantic state models
│   │   ├── prompts.py               # LLM prompt templates
│   │   ├── nodes.py                 # Workflow node functions
│   │   └── workflow.py              # Graph builder
│   │
│   ├── database/                     # Database layer (optional)
│   │   ├── __init__.py
│   │   ├── operations.py            # Database operations
│   │   └── tracing.py               # Execution tracing
│   │
│   └── utils.py                      # Shared utilities
│
├── app/                              # Web application (optional)
│   ├── main.py                       # Streamlit entry point
│   ├── pages/                        # Multi-page components
│   └── utils/                        # App-specific utilities
│
├── examples/                         # Runnable demos
│   └── basic_agent.py               # Example agent script
│
├── tests/                            # Test suite
│   ├── conftest.py                  # Shared fixtures
│   ├── src/                         # Tests mirror src/
│   └── data/                        # Test data
│
├── database/                         # Database files
│   └── migrations/                  # SQL migrations
│
├── data/                            # Data storage
│   └── databases/                   # SQLite files
│
├── docs/                            # Documentation
├── notebooks/                       # Jupyter notebooks
├── scratch/                         # Temporary work
│
├── .github/workflows/               # CI/CD workflows
│   └── ci.yml                       # GitHub Actions
│
├── pyproject.toml                   # Poetry config
├── .pre-commit-config.yaml         # Pre-commit hooks
├── .gitignore                       # Git ignore rules
├── .env.example                     # Environment template
├── CLAUDE.md                        # Claude Code instructions
├── CONTRIBUTING.md                  # Contribution guidelines
└── README.md                        # This file
```

---

## 🛠️ Development

### Common Commands

```bash
# Run tests
poetry run pytest tests/

# Run tests with coverage
poetry run pytest --cov=src tests/

# Run specific test file
poetry run pytest tests/src/test_example.py

# Run linter
poetry run pylint src/

# Format code
poetry run black .

# Sort imports
poetry run isort .

# Type checking
poetry run mypy src/

# Run example scripts
poetry run python examples/basic_agent.py

# Start Streamlit app (if applicable)
poetry run streamlit run app/main.py
```

### Pre-commit Hooks

This template uses pre-commit hooks to maintain code quality:

```bash
# Install hooks
poetry run pre-commit install

# Run manually on all files
poetry run pre-commit run --all-files
```

Hooks include:
- **black** - Code formatting
- **isort** - Import sorting
- **mypy** - Type checking
- **trailing-whitespace** - Remove trailing spaces
- **end-of-file-fixer** - Ensure files end with newline
- **check-yaml** - Validate YAML files
- **check-added-large-files** - Prevent large file commits

---

## 🏗️ Architecture

### Design Principles

1. **Separation of Concerns**
   - `src/` - Framework-agnostic business logic
   - `app/` - UI layer (Streamlit, FastAPI, etc.)
   - `examples/` - Runnable demonstrations

2. **Testability**
   - Dependency injection
   - Mocked external services
   - Test fixtures for common setup

3. **Type Safety**
   - Type hints on all functions
   - Pydantic models for data validation
   - mypy for static type checking

4. **Code Quality**
   - Pre-commit hooks for consistency
   - Linting with pylint (≥8.0/10)
   - Test coverage tracking

---

## 🧪 Testing

### Running Tests

```bash
# All tests
poetry run pytest tests/

# With coverage report
poetry run pytest --cov=src --cov-report=html tests/
open htmlcov/index.html

# Specific test file
poetry run pytest tests/src/test_example.py -v

# Single test
poetry run pytest tests/src/test_example.py::test_function_name
```

### Writing Tests

Follow the testing conventions:

```python
def test_function_name_scenario_expected_result():
    """Test that function_name does X when Y."""
    # Arrange
    input_data = ...

    # Act
    result = function_name(input_data)

    # Assert
    assert result == expected_output
```

---

## 📝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

### Quick Checklist

Before submitting a PR:
- [ ] All tests pass: `poetry run pytest tests/`
- [ ] Coverage maintained: `poetry run pytest --cov=src tests/`
- [ ] Linting passes: `poetry run pylint src/` (score ≥8.0)
- [ ] Formatting applied: `poetry run black . && poetry run isort .`
- [ ] Type checking passes: `poetry run mypy src/`
- [ ] Docstrings added for new functions
- [ ] README updated if needed

---

## 📄 License

This template is released under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🔗 Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)

---

## ✨ Getting Started with Your Project

1. **Update project metadata** in `pyproject.toml`
2. **Replace this README** with your project description
3. **Update CLAUDE.md** with project-specific instructions
4. **Remove optional dependencies** you don't need (Streamlit, pandas, etc.)
5. **Start building** your agent in `src/agent/`
6. **Add tests** as you develop features
7. **Document** your code with docstrings

Happy building! 🚀
