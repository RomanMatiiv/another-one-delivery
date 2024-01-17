import uvicorn
from typer import Typer

manager = Typer()


@manager.command()
def run_api():
    uvicorn.run(
        app="app.api.main:create_app",
        host="0.0.0.0",
        port=8000,
        loop="uvloop",
        http="httptools",
    )


if __name__ == "__main__":
    manager()
