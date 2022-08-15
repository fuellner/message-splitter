"""__main__.py module"""

from cli import CLI
from application import Application

def main() -> None:
    """main method"""
    cli = CLI()
    if not cli.process_arguments():
        print("try again!")
        return
    app: Application = Application(cli)
    app.run()

if __name__ == '__main__':
    main()
