# Package Manager
- This project uses **Poetry** for dependency management
- ALWAYS use `poetry run` prefix for Python commands (e.g., `poetry run pytest`, `poetry run python script.py`)

# Common Commands
- `poetry run pytest tests/`: Run all tests
- `poetry run pytest tests/path/to/test.py`: Run specific test file
- `poetry run pytest tests/path/to/test.py::TestClass::test_method`: Run single test
- `poetry run pytest --cov=src tests/`: Run tests with coverage report
- `poetry run python examples/script.py`: Run example scripts
- `poetry run pylint src/`: Run linter on source code
- `poetry run black .`: Auto-format code
- `poetry run isort .`: Sort imports
- `poetry run mypy src/`: Type checking

# Communication Guidelines

## Explaining Bash Commands
- **ALWAYS explain your intent** when executing bash commands
- Before running any command, clearly state:
  - **What** you're trying to achieve
  - **Why** this command is needed
  - **What** the expected outcome is
- Example: "I'm going to check the git status to see what files have been modified" (not just running `git status` silently)
- This helps the user understand your reasoning and catch potential issues before execution

# Code Quality & Production Standards

## Documentation Requirements
- **Docstrings**: All public functions, classes, and modules MUST have docstrings
  - Use Google-style docstrings with Args, Returns, Raises sections
  - Include usage examples for complex functions
  - Document side effects (database writes, API calls, file I/O)
- **README.md**: Keep up-to-date with:
  - Project overview and purpose
  - Installation instructions
  - Quick start guide
  - Architecture overview
  - Example usage
  - Contributing guidelines
- **Inline Comments**: Use sparingly, only for non-obvious logic
- **Type Hints**: REQUIRED for all function signatures (args and return types)

## Testing Standards
- **Coverage Target**: Aim for 80%+ test coverage
- **Test Organization**:
  - Mirror src/ structure in tests/ directory
  - Use descriptive test names: `test_<function>_<scenario>_<expected_outcome>`
  - Group related tests in classes
- **Test Types Required**:
  - Unit tests for all core logic
  - Integration tests for multi-component interactions
  - End-to-end tests for complete workflows
- **Fixtures**: Use pytest fixtures for common setup (database connections, mock data)
- **Mocking**: Mock external services (APIs, LLMs) in unit tests
- **Test Data**: NEVER use production credentials in tests

## Code Quality Checks
- **Linting**: Code MUST pass `pylint src/` with score ≥ 8.0/10
- **Formatting**: Use `black .` for consistent formatting (120 char line length)
- **Import Sorting**: Use `isort .` to organize imports (standard → third-party → local)
- **Type Checking**: Run `mypy src/` before committing (all type hints must be valid)
- **No Dead Code**: Remove unused imports, variables, and functions
- **Complexity**: Keep cyclomatic complexity low (max 10 per function)

## Error Handling
- **Specific Exceptions**: Catch specific exceptions, not bare `except:`
- **Error Messages**: Provide actionable error messages with context
- **Logging**: Log errors with full stack traces using `logger.exception()`
- **Graceful Degradation**: Handle failures gracefully (retry logic, fallbacks)
- **Validation**: Validate inputs at system boundaries (API endpoints, user input)

## Logging Standards
- **Log Levels**:
  - DEBUG: Detailed diagnostic info (state transitions, variable values)
  - INFO: High-level workflow steps (node execution, database writes)
  - WARNING: Recoverable issues (API rate limits, missing optional data)
  - ERROR: Errors that prevent operation completion
- **Structured Logging**: Include context (session_id, node_name, user_query)
- **No Secrets**: NEVER log credentials, API keys, or PII
- **Performance**: Avoid excessive logging in hot paths

## Database Best Practices (if using database)
- **Connection Management**:
  - Agent workflows: Use SHARED connection (prevents "database is locked")
  - Web apps: Use NEW connection per request (thread-safe)
  - Always close connections (use context managers or try/finally)
- **Schema Changes**: Use migration files in `database/migrations/`
- **Type Safety**: Use None for AUTOINCREMENT fields, not manual IDs
- **Transactions**: Wrap multi-table inserts in transactions
- **Backups**: Document backup strategy in README

## Architecture Standards
- **Separation of Concerns**:
  - `src/`: Core business logic (reusable, framework-agnostic)
  - `app/`: UI layer (presentation only)
  - `examples/`: Runnable demos and workflows
- **Dependency Injection**: Pass connections/config as parameters, not globals
- **Single Responsibility**: Each module/class should have one clear purpose
- **DRY Principle**: Extract common logic into reusable functions

## Git Workflow
- **Branch Naming**:
  - `feature/<description>`: New features
  - `fix/<description>`: Bug fixes
  - `docs/<description>`: Documentation updates
  - `refactor/<description>`: Code refactoring
- **Commit Messages**:
  - Use conventional commits: `<type>: <description>`
  - Types: feat, fix, docs, test, refactor, chore
  - Example: `feat: add caching layer`, `fix: resolve race condition`
- **Pull Requests**:
  - Include description of changes and reasoning
  - Link related issues
  - Ensure all tests pass
  - Request reviews for significant changes

## Pre-Commit Checklist
Before committing code, verify:
- [ ] All tests pass: `poetry run pytest tests/`
- [ ] Coverage maintained: `poetry run pytest --cov=src tests/` (aim for ≥80%)
- [ ] Linting passes: `poetry run pylint src/` (score ≥8.0/10)
- [ ] Formatting applied: `poetry run black . && poetry run isort .`
- [ ] Type checking passes: `poetry run mypy src/`
- [ ] Docstrings added for new functions/classes
- [ ] No sensitive data (API keys, credentials) in code
- [ ] README updated if public API changed
- [ ] Example scripts tested: `poetry run python examples/<script>.py`

## Security & Privacy
- **Credentials**: Store in `.env` file (NEVER commit to git)
- **API Keys**: Use environment variables, never hardcode
- **Input Validation**: Sanitize user input to prevent injection attacks
- **Dependencies**: Regularly update dependencies (`poetry update`)
- **Secrets Scanning**: Use tools to prevent accidental credential commits

# Code Style
- Follow PEP 8 Python style guidelines
- Use type hints for ALL function signatures
- Import organization: standard library → third-party → local imports
- Line length: 120 characters max
- Use f-strings for string formatting (not % or .format())

# Workflow
- Prefer running single tests for performance and faster feedback
- Always test code changes before committing
- Write tests FIRST for new features (TDD approach preferred)
- Document architectural decisions in code comments or docs/

# Project-Specific Instructions

## TODO: Customize these for your project
- Add any project-specific API scopes or credentials
- Document any special workflow requirements
- List any external services or integrations
- Add deployment instructions
- Include any domain-specific guidelines
