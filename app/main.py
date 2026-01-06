from app.services.dialogue import listen, handle, speak
import asyncio


async def run():
    await speak("Welcome to the restaurant. How can I help you?")
    while True:
        text = listen()
        reply = handle(text)
        await speak(reply)

if __name__ == "__main__":
    asyncio.run(run())
