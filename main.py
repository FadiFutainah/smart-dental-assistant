from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"  # Directory to store uploaded images
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.post('/upload/')
async def upload_image(image: UploadFile = File(...)):
    try:
        image_data = await image.read()
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)

        with open(image_path, "wb") as f:
            f.write(image_data)

        return JSONResponse(content={"message": "Image uploaded successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=5000)
