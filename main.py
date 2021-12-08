import asyncio


host = 'minechat.dvmn.org'
port = 5000


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        message = await reader.read(1000)
        decode_message = message.decode("utf-8")
        print(decode_message)


asyncio.run(tcp_echo_client(host, port))