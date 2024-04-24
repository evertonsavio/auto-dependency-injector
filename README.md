# Python Winter Boot

This project demonstrates how to perform auto dependency injection in Python.

## Getting Started
## How it works

The `@Service`, `@Component` and `@Primary` decorators are used to do dependency injection automatically given an interface and at least one implementation of that interface.
Your service implementation should be decorated with `@Service` and the class that will be injected should be decorated with `@Component`.
If you have more than one implementation of the interface, you should use the `@Primary` decorator to specify which implementation should be used.

## Installation

```bash
pip install -r ./requirements.txt
```

## Acknowledgements

This example was inspired by how Java Spring Boot framework do automatically dependency injection using annotations.