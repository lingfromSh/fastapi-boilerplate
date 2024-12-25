# fastapi-boilerplate

This is a boilerplate for building scalable and maintainable web APIs based on FastAPI.

See more details: [Documentation](docs/index.md)

## Tech Stack

- FastAPI

### API

- GraphQL
  - strawberry
- RESTful API
  - authlib
  - fastapi-pagination
  - piccolo-api
- Socketio
  - python-socketio
- Validation
  - pydantic

### Database

- tortoise-orm
- aerich

### Configuration

- dynaconf
- pydantic-settings

### Task Queue

- taskiq

### Authentication

- authlib

### Monitoring

- grafana

### Logging

- loguru

### Metrics

- prometheus

### Testing

#### Unit Testing

- pytest
- pytest-asyncio
- pytest-cov
- pytest-mock

#### Throughput Testing

- locust

## Code Quality

- black
- isort
- ruff
- pre-commit

## Virtual Environment Management

UV is a tool for managing multiple python versions.

### Installation

#### macOS/Linux

##### Install Latest Version

```bash
# curl
curl -LsSf https://astral.sh/uv/install.sh | sh
# or wget
wget -qO- https://astral.sh/uv/install.sh | sh
```

##### Install Specific Version

```bash
curl -LsSf https://astral.sh/uv/{version}/install.sh | sh
```
