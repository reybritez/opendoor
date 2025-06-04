from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hola Mundo"}

@app.get("/opendoor")
async def open_door(door: str):
    if door == "gimnasio":
        url = "http://192.168.1.163:8090/device/openDoorControl"
        params = {
            "data": "Open the door successfully",
            "result": 1,
            "pass": "12345678",
            "sucess": "true"
        }
        response = requests.get(url, params=params)
        return {"action": f"Abriendo la puerta del gimnasio", "status": response.status_code}
    
    return {"action": f"Abriendo la puerta: {door}"}

if __name__ == "__main__":
    config = uvicorn.Config(
        "app:app",
        host="127.0.0.1",
        port=8000,
    )
    server = uvicorn.Server(config)
    server.run()