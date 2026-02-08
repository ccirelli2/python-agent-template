# Contributing to [Project Name]

Thank you for your interest in contributing! This document provides guidelines and standards for contributing to this project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Quality Standards](#code-quality-standards)
- [Testing Requirements](#testing-requirements)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Architecture Guidelines](#architecture-guidelines)

## Code of Conduct

This project adheres to professional standards of collaboration:
- Be respectful and constructive in all interactions
- Focus on what is best for the community and the project
- Show empathy towards other contributors
- Accept constructive criticism gracefully

## Getting Started

### Prerequisites
- Python 3.12+
- Poetry (dependency management)
- Git

### First Time Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/project-name.git
   cd project-name
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Install pre-commit hooks**
   ```bash
   poetry run pre-commit install
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

5. **Run tests to verify setup**
   ```bash
   poetry run pytest tests/
   ```

## Development Setup

### Project Structure
```
project-name/
├── src/                    # Core business logic (reusable, framework-agnostic)
│   ├── agent/             # Agent module
│   ├── database/          # Database operations (if applicable)
│   └── utils.py           # Shared utilities
├── app/                   # Web application (optional)
│   ├── main.py           # Entry point
│   ├── pages/            # Multi-page components
│   └── utils/            # App-specific utilities
├── examples/              # Runnable demos and workflows
├── tests/                 # Test suite (mirrors src/ structure)
├── database/migrations/   # SQL migrations (if applicable)
└── data/                  # Data storage
```

### Development Tools

All commands use the `poetry run` prefix:

```bash
# Run tests
poetry run pytest tests/

# Run tests with coverage
poetry run pytest --cov=src tests/

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
```

## Code Quality Standards

### Documentation
- **All public functions/classes MUST have docstrings** using Google-style format:
  ```python
  def process_data(input_data: dict, validate: bool = True) -> dict:
      """
      Process input data and return structured output.

      Args:
          input_data: Raw data dictionary to process
          validate: Whether to validate data before processing

      Returns:
          Processed data as a dictionary

      Raises:
          ValueError: If input_data is invalid and validate=True

      Example:
          >>> result = process_data({"key": "value"})
          >>> print(result)
          {"processed": "value"}
      """
  ```

- **Type hints are REQUIRED** for all function signatures
- **Inline comments** only for non-obvious logic

### Code Style
- **Line length**: 120 characters max
- **Formatting**: Use `black` (enforced by pre-commit)
- **Import order**: standard library → third-party → local (enforced by `isort`)
- **Naming conventions**:
  - Classes: `PascalCase`
  - Functions/variables: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
  - Private methods: `_leading_underscore`

### Linting Standards
- Code MUST pass `pylint` with score ≥ 8.0/10
- Fix all errors before submitting PR
- Document any pylint disables with justification

### Type Safety
- Run `mypy src/` and fix all type errors
- Use `Optional[T]` for nullable types
- Use `Union[T1, T2]` or `T1 | T2` for multiple types

## Testing Requirements

### Test Coverage
- **Target**: 80%+ code coverage
- Run coverage report: `poetry run pytest --cov=src --cov-report=html tests/`
- View report: `open htmlcov/index.html`

### Test Organization
```
tests/
├── conftest.py                # Shared fixtures
├── src/
│   ├── test_utils.py         # Tests for src/utils.py
│   ├── agent/
│   │   ├── test_state.py     # Tests for src/agent/state.py
│   │   └── test_nodes.py     # Tests for src/agent/nodes.py
│   └── ...
└── integration/              # Integration tests
    └── test_workflow.py
```

### Writing Tests
1. **Test naming**: `test_<function>_<scenario>_<expected_outcome>`
   ```python
   def test_process_data_valid_input_returns_dict():
       """Test that process_data returns a dict with valid input."""
       # Arrange
       input_data = {"key": "value"}

       # Act
       result = process_data(input_data)

       # Assert
       assert isinstance(result, dict)
       assert "processed" in result
   ```

2. **Use fixtures** for common setup:
   ```python
   @pytest.fixture
   def sample_data():
       """Provide sample test data."""
       return {"key": "value"}

   def test_process_data_with_fixture(sample_data):
       """Test processing with fixture data."""
       result = process_data(sample_data)
       assert result is not None
   ```

3. **Mock external services** (APIs, LLMs):
   ```python
   from unittest.mock import patch

   @patch('src.agent.nodes.ChatOpenAI')
   def test_agent_node_mocked_llm(mock_llm):
       """Test agent node with mocked LLM."""
       mock_llm.return_value.invoke.return_value = "mocked response"
       # Test with mock
   ```

4. **Test categories**:
   - Unit tests: Test individual functions in isolation
   - Integration tests: Test interactions between components
   - E2E tests: Test complete workflows

## Commit Guidelines

### Commit Message Format
Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <description>

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring (no behavior change)
- `perf`: Performance improvements
- `chore`: Maintenance tasks (dependencies, build, etc.)

**Examples**:
```
feat: add caching layer for API responses

fix: resolve race condition in database writes

docs: update README with deployment instructions

test: add integration tests for agent workflow

refactor: extract prompt templates into separate module
```

### Branch Naming
- `feature/<description>`: New features (`feature/add-caching`)
- `fix/<description>`: Bug fixes (`fix/database-race-condition`)
- `docs/<description>`: Documentation (`docs/improve-readme`)
- `refactor/<description>`: Refactoring (`refactor/extract-prompts`)

## Pull Request Process

### Before Submitting a PR

1. **Run the pre-commit checklist**:
   ```bash
   # All must pass
   poetry run pytest tests/
   poetry run pytest --cov=src tests/  # Coverage ≥80%
   poetry run pylint src/              # Score ≥8.0
   poetry run black . && poetry run isort .
   poetry run mypy src/
   ```

2. **Update documentation**:
   - Add/update docstrings for new functions
   - Update README.md if public API changed
   - Add examples if introducing new features

3. **Add tests**:
   - Unit tests for new functions
   - Integration tests for new workflows
   - Update existing tests if behavior changed

### PR Description Template
```markdown
## Description
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] All tests passing
- [ ] Code coverage ≥80%

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No breaking changes (or documented if unavoidable)
- [ ] Pre-commit hooks passing
```

### Review Process
1. Submit PR with clear description
2. Address reviewer feedback promptly
3. Keep PR scope focused (one feature/fix per PR)
4. Rebase on main before merging (avoid merge commits)

## Architecture Guidelines

### Separation of Concerns
- **`src/`**: Framework-agnostic business logic
  - No UI framework imports
  - Reusable across different interfaces (CLI, API, UI)
- **`app/`**: UI-specific presentation layer
  - Only UI logic, no core business logic
- **`examples/`**: Runnable demonstrations
  - Self-contained scripts
  - Documented with clear docstrings

### Database Best Practices (if applicable)
- **Connection Management**:
  - Use context managers for connections
  - Always close connections (try/finally)
- **Schema Changes**: Create migration files in `database/migrations/`
- **Type Safety**: Use appropriate types for database fields
- **Transactions**: Wrap multi-table operations in transactions

### Error Handling
- Catch specific exceptions, not bare `except:`
- Provide actionable error messages with context
- Log errors with stack traces: `logger.exception()`
- Handle failures gracefully (retry logic, fallbacks)

### Logging
- Use appropriate log levels (DEBUG/INFO/WARNING/ERROR)
- Include context in log messages
- Never log credentials or PII
- Structured logging for production readability

### Security
- Store credentials in `.env` (never commit)
- Validate user input at system boundaries
- Sanitize inputs to prevent injection
- Regularly update dependencies

## Questions or Need Help?

- Open an issue for bugs or feature requests
- Use Discussions for questions and ideas
- Tag maintainers for urgent issues

Thank you for contributing! 🚀
