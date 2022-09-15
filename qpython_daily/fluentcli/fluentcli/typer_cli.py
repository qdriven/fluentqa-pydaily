
import typer
from fluentcli.typer_demo.typer_command import app as greet_app

app = typer.Typer(name="demo typer cli ....")
app.add_typer(greet_app)

def main():
    app()


if __name__=="__main__":
    main()