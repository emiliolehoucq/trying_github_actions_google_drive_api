Repo to try uploading files to Google Drive using the API within GitHub Actions. I learned from Google's documentation, particularly "[Python quickstart](https://developers.google.com/drive/api/quickstart/python)" and "[Upload file data](https://developers.google.com/drive/api/guides/manage-uploads)", as well as ChatGPT. Before attempting this, you need to:

1. Create a Google Cloud Project in [https://console.cloud.google.com/](https://console.cloud.google.com/).
2. Enable the Google Drive API within that project (in "APIs & Services", search for the Google Drive API and enable it
3. Create a Service Account (in "APIs & Services" > "Credentials", create credentials and choose service account)
4. Open the details of the service account and, under keys, download a JSON key
5. Share a Google Drive folder with the service account email (e.g., `your-service-account@your-project-id.iam.gserviceaccount.com`)
6. Store credentials in GitHub Secrets
