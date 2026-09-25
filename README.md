# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.
## Features

- View marketplace items
- Add new items
- Search marketplace items
- Mark items as sold
- View marketplace statistics
- JSON API
- Health check endpoint
## CI/CD Pipeline

```text
Git Push
   ↓
GitHub
   ↓
Lint
   ↓
Tests
   ↓
Docker Build
   ↓
Render Deploy
   ↓
Live Application