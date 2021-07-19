from python_calculator.input import FileInputReader, InteractiveInputReader


class InputReaderFactory:
    def create_reader(self, file_name: str):
        if file_name:
            return FileInputReader(file_name)
        return InteractiveInputReader()
