
import typer

app = typer.Typer(name="typer greet")

@app.command(name="greeting")
def greet(name: str):
    print(f"Hello {name}")


