# Use Python 3.12.3 slim image as the base
FROM python:3.12.3-slim AS base

# Set the working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock .env ap-southeast-2-bundle.pem ./
COPY src ./src

# Set environment variables
ENV PYTHONPATH=/app/src
ENV PATH=/app/.venv/bin:$PATH

# Install Poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev && \
    pip install pytest && \
    yes | poetry cache clear --all . && \
    pip cache purge

# Set the entrypoint to run tests
ENTRYPOINT ["poetry", "run", "pytest"]