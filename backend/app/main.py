from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import os
import yt_dlp

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return '''
    <form action="/download" method="post">
        <label for="url">YouTube Video URL:</label><br>
        <input type="text" id="url" name="url" required><br>
        <input type="submit" value="Download">
    </form>
    '''

@app.post("/download")
async def download(url: str = Form(...)):
    try:
        filename = 'backend/app/video.mp4'
        ydl_opts = {
            'format': 'best',
            'outtmpl': filename,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completed!")

        return JSONResponse(content={'message': 'Video downloaded successfully!', 'file_name': os.path.basename(filename)})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
