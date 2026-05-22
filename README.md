# GitHub User Activity CLI

A dependency-free command-line interface (CLI) application built in Python that fetches and displays recent activity for any GitHub user. This project showcases structured application bootstrapping, native URL data fetching, and object-oriented configuration management.

## Project Architecture

The application is structured into modular components following an explicit separation of concerns:

* `app.py`: The entry point that orchestrates bootstrapping, argument parsing, and service execution.
* `github_activity/configs/bootstrap.py`: Traverses filesystem directories upward to locate the project root and load environment variables.
* `github_activity/configs/config.py`: Implements a type-safe object model wrapper (`AppConfig`) using the standard `tomllib` module.
* `github_activity/configs/http_request.py`: Low-level network wrapper around `urllib.request` tracking network connectivity and HTTP statuses.
* `github_activity/user_interface/cli': Built-in argument parsing strategy using `argparse`.
* `github_activity/services/activity.py`: Business logic layer executing API orchestrations.

## Installation

### Prerequisites
* Python 3.11 or higher (required for native `tomllib` support).

### Configuration Setup
Before installing, ensure you have a `github_activity.toml` configuration file in your project root directory containing the API configurations:

```toml
[api]
github_base_url = "https://api.github.com/users/"
github_activity_path = "/events"

Installation
pip install -e .

Note: Default github_activity.toml is provided.

Project URL: https://roadmap.sh/projects/github-user-activity