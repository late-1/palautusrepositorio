# Agent Instructions

## Project

This is a small Flask application for user registration and login. Keep changes
focused on the existing architecture and preserve the browser-facing routes and
template element IDs used by the Robot Framework suites.

## Setup and verification

- Use Python 3.14 or newer and `uv`.
- Install dependencies with `uv sync`.
- Initialize the Browser library once with `uv run rfbrowser init`.
- Start the application from the repository root with `uv run python src/index.py`.
- Run browser tests in a second terminal with `uv run robot src/tests`.
- The application and tests use `http://localhost:5001`; start the server before
  running the browser tests.

## Architecture

- [src/index.py](src/index.py) is the supported application entry point.
- [src/app.py](src/app.py) owns Flask routes, redirects, flash messages, and the
  test reset endpoint.
- [src/entities/user.py](src/entities/user.py) contains the user entity.
- [src/repositories/user_repository.py](src/repositories/user_repository.py)
  provides in-memory persistence.
- [src/services/user_service.py](src/services/user_service.py) owns registration
  validation and credential checks.
- [src/templates/](src/templates/) contains Jinja templates; preserve the
  existing template inheritance and selectors.
- [src/AppLibrary.py](src/AppLibrary.py) contains custom Robot Framework
  keywords.

Keep repository and service instances consistent with the existing module-level
singletons. Route handlers translate service exceptions into flash messages and
redirects; keep business validation in the service layer.

## Test conventions and pitfalls

- Browser suites are in [src/tests/](src/tests/), with shared setup and selectors
  in [src/tests/resource.robot](src/tests/resource.robot).
- User data is process-local and is cleared by `POST /tests/reset`; restarting
  the server also clears it.
- Browser tests require Chromium and the Browser library initialization.
- Imports assume the documented `uv run python src/index.py` invocation from the
  repository root.
- `/tests/reset` is test support, not an application authentication mechanism.
- Treat the hard-coded Flask secret key as development-only configuration.

When changing routes, form fields, titles, or element IDs, update the affected
Robot suites and run the complete browser test command.

## Change discipline

Prefer small changes that match the existing naming and layering conventions.
Do not edit generated test artifacts such as `output.xml`, `log.html`, or
`report.html` unless explicitly asked.