"""module Splitter"""

import time


class Splitter:
    """class for splitting functionality"""

    def __init__(
        self,
        chunk_size: int = 280,
        input_string: str = "",
        file_path: str = "",
        output_file_path: str = ""
    ) -> None:
        self.chunk_size: int = int(chunk_size) - 4
        self.input_string: str = input_string
        self.file_path: str = file_path
        self.output_file_name: str = output_file_path

    def split_message(self) -> str:
        """method which does the actual splitting"""
        chunks: list[str] = []
        output: str = ""
        offset: int = 0
        i: int = 0

        input_text: str = self.get_input_string()
        input_text_length: int = len(input_text)

        while i <= input_text_length:
            if (i + self.chunk_size <= input_text_length
                    and input_text[i + self.chunk_size] != " "):
                while input_text[i + (self.chunk_size - offset)] != " ":
                    offset += 1
            chunks.append(input_text[i: i + self.chunk_size - offset])
            i = i + self.chunk_size - offset
            offset = 0

        chunk_count = len(chunks)
        chunks[0] = "1" + "/" + str(chunk_count) + " " + chunks[0]

        for k in range(1, chunk_count, 1):
            chunks[k] = str(k + 1) + "/" + str(chunk_count) + chunks[k]

        if self.output_file_name is None:
            self.output_file_name = "splitted_"

        with open(
                f'{self.output_file_name}{int(time.time())}.txt', "a", encoding="utf-8"
        ) as output_file:
            for chunk in chunks:
                output = output + chunk + "\n\n--------------------------------------\n\n"
                output_file.write(
                    chunk + "\n\n--------------------------------------\n\n")
        return output

    def set_input_string(self, input_string: str = "") -> None:
        """method set_input_text"""
        self.input_string: str = input_string

    def get_input_string(self) -> str:
        """method set_input_text"""
        if self.input_string != "":
            return self.input_string

        if self.file_path != "":
            try:
                with open(self.file_path, 'r', encoding="utf-8") as file:
                    return file.read()
            except Exception as error:
                return f'WARNING: An error occured while reading the file with message: {error}'
        return ""
