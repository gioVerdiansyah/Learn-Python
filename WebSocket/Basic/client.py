import asyncio
import websockets

async def main():
    async with websockets.connect("ws://127.0.0.1:4545") as websocket:
        name = input("Enter your name: ")

        await websocket.send(name)

        msg = await websocket.recv()
        print(f"Received from server: {msg}")


if __name__ == "__main__":
    asyncio.run(main())