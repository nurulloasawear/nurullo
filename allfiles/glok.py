import asyncio
import websockets
import pyautogui
import io
from PIL import Image

async def send_screen(websocket, path):
    while True:
        screenshot = pyautogui.screenshot()
        screenshot_bytes = io.BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_bytes.seek(0)
        await websocket.send(screenshot_bytes.read())

async def receive_screen(websocket, path):
    while True:
        data = await websocket.recv()
        img = Image.open(io.BytesIO(data))
        img.show()

async def main():
    # Set up WebSocket server
    server = await websockets.serve(receive_screen, "0.0.0.0", 8765)
    print("WebSocket server started at ws://0.0.0.0:8765")

    # Connect to WebSocket server
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")
        await send_screen(websocket, None)

if __name__ == "__main__":
    asyncio.run(main())
