import asyncio
import websockets


async def send(websocket):
    msg = await websocket.recv()
    print(f"Server received: {msg}")

    delivered = f"Hello {msg}"
    await websocket.send(delivered)
    print(f"Server sent {delivered}")


async def main():
    async with websockets.serve(send, '127.0.0.1', 4545):
        await asyncio.Future() # run forever


if __name__ == "__main__":
    asyncio.run(main())