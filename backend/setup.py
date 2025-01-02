from setuptools import setup, find_packages

setup(
    name="todo_backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["psycopg2"],
    entry_points={
        "console_scripts": [
            "todo-backend=app:run",
        ]
    },
)
