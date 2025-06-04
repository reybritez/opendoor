from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hola Mundo"}

if __name__ == "__main__":
    config = uvicorn.Config(
        "app:app",
        host="127.0.0.1",
        port=8000,
        ssl_keyfile="./certs/private.key",
        ssl_certfile="./certs/certificate.crt"
    )
server = uvicorn.Server(config)
server.run()