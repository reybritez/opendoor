from fastapi import FastAPI
import uvicorn
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

# Agregar middleware para redirección HTTPS
app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/")
async def read_root():
    return {"message": "Hola Mundo"}

if __name__ == "__main__":
    # Configurar el servidor HTTPS
    config = uvicorn.Config(
        "app:app",
        host="kuarahy.deportivosajonia.lan",
        port=443,
        ssl_keyfile="./certs/private.key",
        ssl_certfile="./certs/certificate.crt"
    )
    server = uvicorn.Server(config)
    server.run()