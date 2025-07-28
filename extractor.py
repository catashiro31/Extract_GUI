import zipfile

def archive_extract(archive_path, dest_path):
    with zipfile.ZipFile(archive_path,"r") as archive:
        archive.extractall(dest_path)

if __name__ == "__main__":
    pass