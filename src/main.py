from uvicorn import Config, Server
from web_app import app


if __name__ == '__main__':
    print('hi')
    config = Config(
        app=app,
        host='localhost',
        port=8080
    )
    server = Server(config)
    server.run()