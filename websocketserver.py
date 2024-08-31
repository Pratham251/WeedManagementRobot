import asyncio
import websockets
import json

# Define a function to handle incoming connections and messages
async def handler(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            print("Received data:", data)
            # Send a response back to the client
            response = {"status": "Data received", "received_data": data}
            await websocket.send(json.dumps(response))
    except websockets.exceptions.ConnectionClosed as e:
        print("Client disconnected")

# Start the WebSocket server
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8070):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

