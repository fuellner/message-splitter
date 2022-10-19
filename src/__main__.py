"""__main__.py module"""

from cli import CLI
from application import Application


def main() -> None:
    """main method"""
    app: Application = Application()
    app.run()


if __name__ == '__main__':
    main()
