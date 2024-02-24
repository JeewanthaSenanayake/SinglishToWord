import webbrowser
import uvicorn
from api import app  

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    
def open_html_file(html_file_path):
    # Open the HTML file in the default web browser
    webbrowser.open(html_file_path, new=2)

if __name__ == "__main__":
    html_file_path = "index.html"
    open_html_file(html_file_path)
    run_server()
