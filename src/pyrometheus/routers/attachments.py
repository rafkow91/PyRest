from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix='/attachments',
    tags=['attachements']
)


@router.post('/files/')
async def create_upload_file(file: UploadFile):
    with open(file.filename, mode='wb') as handler:
        handler.write(await file.read())

    return {'filename': file.filename, 'Content-Type': file.content_type}
