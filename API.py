from ListCompany import ListCompany
import qrcode
from docxtpl import DocxTemplate, InlineImage
from fastapi import FastAPI
from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
import uvicorn
import cv2
from docx.shared import Mm
import cv2
import pdf2image
from typing import List
from fastapi import FastAPI, File, UploadFile
import json


app = FastAPI()
listCompany = ListCompany()
@app.post("/")
async def list_company(request: Request):
    body = await request.body()
    body = json.loads(body)
    data = listCompany.get_list_company(body["data"])
    return data

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)