import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir , "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w')as archive :
        for filepath in filepaths:
            archive.write(filepath , arcname=pathlib.Path(filepath).name)

if __name__ == "__main__":
    make_archive(filepaths=["test.txt", "test2.txt"], dest_dir="dest")