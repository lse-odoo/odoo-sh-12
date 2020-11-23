# -*- coding: utf-8 -*-
from odoo import http
import asyncio
import logging

_logger = logging.getLogger(__name__)

servers = []

def runServer(port):
    @asyncio.coroutine
    def handle_echo(reader, writer):
        data = yield from reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        _logger.info("(Server) Received %r from %r" % (message, addr))

        _logger.info("(Server) Send: %r" % message)
        writer.write(data)
        yield from writer.drain()

        _logger.info("(Server) Close the client socket")
        writer.close()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    coro = asyncio.start_server(handle_echo, '0.0.0.0', port, loop=loop)
    server = loop.run_until_complete(coro)
    servers.append(server)

    # Serve requests until Ctrl+C is pressed
    _logger.info('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

class TestPort(http.Controller):
    @http.route('/test_port/test_port/start/<int:port>', auth='public')
    def index(self, port,  **kw):
        _logger.warning("Server start")
        runServer(port)
        _logger.warning("Server end")
        return "Hello, world"

    @http.route('/test_port/test_port/pingme/<int:port>', auth='public')
    def index2(self, port, **kw):
        @asyncio.coroutine
        def tcp_echo_client(message, loop):
            reader, writer = yield from asyncio.open_connection('127.0.0.1', port,
                                                                loop=loop)
            _logger.info('(Client) Send: %r' % message)
            writer.write(message.encode())
            data = yield from reader.read(100)
            _logger.info('(Client) Received: %r' % data.decode())
            _logger.info('(Client) Close the socket')
            writer.close()

        message = 'Hello World! Send'
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(tcp_echo_client(message, loop))
        loop.close()
        return "Ping ended"

    @http.route('/test_port/test_port/close_all', auth='public')
    def index3(self, port, **kw):
        for server in servers:
            server.close()
