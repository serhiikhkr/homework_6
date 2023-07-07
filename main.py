from pathlib import Path
import shutil
import sys
import folders_parser as parser
from normalize import normalize
# import os


def main(folder: Path):
    parser.folder_scan(folder)
    for file in parser.IMAGES:
        create_new_folder_m_d(file, folder / 'images')
    for file in parser.VIDEO:
        create_new_folder_m_d(file, folder / 'video')
    for file in parser.MUSIC:
        create_new_folder_m_d(file, folder / 'audio')
    for file in parser.DOCUMENT:
        create_new_folder_m_d(file, folder / 'documents')
    for file in parser.ARCHIVES:
        create_new_folder_m_d(file, folder / 'archives')


def create_new_folder_m_d(fl: Path,new_path: Path):
    new_path.mkdir(exist_ok=True, parents=True)
    fl.replace(new_path / normalize(fl.name))

def create_new_folder_archives(fl: Path, new_path: Path):
    new_path.mkdir(exist_ok=True,parents=True)
    foler_upack_file = normalize(fl.name.replace(fl.suffix,''))
    unpack_archives = new_path / foler_upack_file
    unpack_archives.mkdir(exist_ok=True,parents=True)
    shutil.unpack_archive(fl,unpack_archives)

# def del_empty_folders(path: Path):
#     for fl in path.iterdir():
#         if fl.is_file():
#             continue
#         elif fl.is_dir():
#             if len(os.listdir(fl)) == 0:
#                 fl.rmdir()

if __name__ == "__main__":
    if sys.argv[1]:
        scan_folder = Path(sys.argv[1])
        main(scan_folder)



