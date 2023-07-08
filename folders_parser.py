from pathlib import Path
import sys

folder_path = Path(sys.argv[1])

IMAGES = []
VIDEO = []
DOCUMENT = []
MUSIC = []
ARCHIVES = []
OTHER = []


new_folders_with_ex = {
    'IMAGES': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'VIDEO': ['AVI', 'MP4', 'MOV', 'MKV'],
    'MUSIC': ['MP3', 'OGG', 'WAV', 'AMR'],
    'ARCHIVES': ['ZIP', 'GZ', 'TAR'],
    'DOCUMENTS': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'OTHER': ['*']

}



def folder_scan(path: Path) -> None:    #Сканирование указанной папки
    for el in path.iterdir():
        if el.is_dir():
            if el.name not in ["archives", "video", "audio", "documents", "images"]:
                folder_scan(el)
        else:
            file_ex = scan_ex(el.name)
            list_folder_ex = list(new_folders_with_ex.items())
            dir = None

            for ex in range(len(list_folder_ex)):
                if file_ex in list_folder_ex[ex][1]:
                    list_name = list_folder_ex[ex][0]
                    if list_name == 'IMAGES':
                        IMAGES.append(path / el.name)
                        dir = '+'
                        break
                    elif list_name == 'VIDEO':
                        VIDEO.append(path / el.name)
                        dir = '+'
                        break
                    elif list_name == 'MUSIC':
                        MUSIC.append(path / el.name)
                        dir = '+'
                        break
                    elif list_name == 'DOCUMENTS':
                        DOCUMENT.append(path / el.name)
                        dir = '+'
                        break
                    elif list_name == 'ARCHIVES':
                        ARCHIVES.append(path / el.name)
                        dir = '+'
                        break
            if not dir:
                OTHER.append(path / el.name)




def scan_ex(file_name: str) -> str:
    return Path(file_name).suffix[1:].upper()

