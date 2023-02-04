from PIL import Image
import os
import pathlib


def get_metadata(abs_file_path):
    # load img
    targetImage = Image.open(abs_file_path)
    # get the entry from the dictionatry
    file_name = os.path.basename(abs_file_path)
    print(f'filename: {file_name}')
    for key, value in targetImage.text.items():
        print(f'\t{key} --> \t{value}')
    print()


if __name__ == '__main__':
    # Absoluter Pfad vom Hauptverzeichnis
    pfad_input = (pathlib.Path(__file__).parent.absolute())
    print()
    print(f'path: {pfad_input}')

    for root, folders, file in os.walk(pfad_input):
        # print(f'root: {root}')
        for folder in folders:
            if folder == 'autosaved_img' or folder == 'saved_images_by_gui':
                print()
                print(f'folder --> {folder}:')
                print()
                for entry in os.listdir(folder):
                    # print(f'\tentry: {entry}')
                    abs_pfad = os.path.join(root, folder, entry)
                    # print(abs_pfad)
                    get_metadata(abs_pfad)
