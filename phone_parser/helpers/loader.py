import os


class FileLoader:
    def __init__(self, files_path, files_ext):
        self.files_path = files_path
        self.files_ext = files_ext

    def generate_file_list(self):
        all_files = self.load_files(self.files_path, self.files_ext)
        return all_files

    def load_files(self, path, extension):

        all_files = list()

        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            if os.path.isdir(full_path):
                all_files = all_files + self.load_files(full_path, extension)
            else:
                if file.endswith(extension):
                    all_files.append(full_path)

        return all_files
