import asyncio
import logging

from aiohttp import web

from app.routes import setup_routes


def init(loop):
    # setup application and extensions
    app = web.Application(loop=loop)

    # setup views and routes
    setup_routes(app)

    return app


def create_app():
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()

    app = init(loop)
    web.run_app(app, host='127.0.0.1', port=8080)
