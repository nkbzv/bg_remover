# pip install rembg[gpu] onnxruntime-gpu
from rembg import remove
from PIL import Image
from pathlib import Path


def find_files(directory: str, extensions: list) -> list:
    """Поиск файлов в директории с заданными расширениями"""
    all_files = []
    for ext in extensions:
        all_files.extend(Path(directory).glob(ext))
    return all_files

def process_file(input_path: Path, output_dir: str) -> None:
    """Удаление фона для заданного файла"""
    file_name = input_path.stem
    output_path = f'{output_dir}/{file_name}_output.png'
    input_img = Image.open(input_path)
    output_img = remove(input_img)
    output_img.save(output_path)

def remove_bg(input_dir: str, output_dir: str, extensions: list) -> None:
    """Удаление фона для всех файлов в директории"""
    all_files = find_files(input_dir, extensions)
    for index, item in enumerate(all_files, 1):
        process_file(item, output_dir)
        print(f'Completed: {index}/{len(all_files)}')

if __name__ == '__main__':
    input_dir = 'input_imgs'
    output_dir = 'output_imgs'
    extensions = ['*.png', '*.jpg']
    remove_bg(input_dir, output_dir, extensions)