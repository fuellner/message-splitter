"""__main__.py module"""

from cli import CLI
from application import Application

def main() -> None:
    """main method"""
    cli = CLI()
    app: Application = Application(cli)
    app.run()

if __name__ == '__main__':
    main()
