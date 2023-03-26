Sure, here's the README.md file:

```
# HTTP Monitor

[![Python Version](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/release/python-390/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/username/http-monitor/blob/main/LICENSE)

HTTP Monitor is a Python script that monitors and prints all HTTP requests through localhost in formatted and colored verbose output.

## Installation

1. Clone the repository:

```
$ git clone https://github.com/username/http-monitor.git
```

2. Install dependencies:

```
$ pip3 install -r requirements.txt
```

## Usage

To run the script, navigate to the project directory and run the following command:

```
$ python3 http_monitor.py
```

This will start the server on `localhost:8000` and print all HTTP requests to the console in formatted and colored verbose output.

## Docker

To run the application using Docker, first, build the Docker image:

```
$ docker build -t http-monitor .
```

Then, run the Docker container:

```
$ docker run -p 8000:8000 http-monitor
```

This will start the server on `localhost:8000` and print all HTTP requests to the console in formatted and colored verbose output.

## Files

- `http_monitor.py`: Python script that monitors and prints all HTTP requests through localhost in formatted and colored verbose output.
- `requirements.txt`: List of dependencies required by the application.
- `Dockerfile`: Instructions for building a Docker image of the application.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/username/http-monitor/blob/main/LICENSE) file for details.
```