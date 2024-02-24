from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import keyboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/write_on_doc/")
def write_on_doc(data: dict):
    msg = data['text']
    print(msg)
    # pyautogui.write(f'{msg}')
    keyboard.write(f'{msg}')
    
    return {"msg": "done"}

# pip install pyinstaller
# pyinstaller --onefile main.py