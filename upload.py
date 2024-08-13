from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
from datetime import datetime

# Authenticate using the service account
credentials = service_account.Credentials.from_service_account_file(
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
)
service = build('drive', 'v3', credentials=credentials)

folder_id = '13LooTAmZJCjtcxiOjJtWqo68NUQS4BD9' # https://drive.google.com/drive/u/0/folders/13LooTAmZJCjtcxiOjJtWqo68NUQS4BD9
file_name = 'photo' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpeg'
file_metadata = {
    'name': file_name,
    'parents': [folder_id]
}
media = MediaFileUpload('photo.jpeg', mimetype='image/jpeg')

# Upload the file to the shared folder
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
