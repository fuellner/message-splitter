"""module Splitter"""

import time


class Splitter:
    """class for splitting functionality"""
    def split_message(
            self,
            chunk_size: int,
            input_text: str,
            output_file_flag: bool = False,
            output_file_name: str = ""
    ) -> str:
        """method which does the actual splitting"""
        chunk_size = int(chunk_size) - 4
        chunks: list[str] = []
        output: str = ""
        offset: int = 0
        input_text_length: int = len(input_text)
        i: int = 0

        while i <= input_text_length:
            if (i + chunk_size <= input_text_length
                    and input_text[i + chunk_size] != " "):
                while input_text[i + (chunk_size - offset)] != " ":
                    offset += 1
            chunks.append(input_text[i: i + chunk_size - offset])
            i = i + chunk_size - offset
            offset = 0

        chunk_count = len(chunks)
        chunks[0] = "1" + "/" + str(chunk_count) + " " + chunks[0]

        for k in range(1, chunk_count, 1):
            chunks[k] = str(k + 1) + "/" + str(chunk_count) + chunks[k]

        for chunk in chunks:
            output = output + chunk + "\n\n--------------------------------------\n\n"

        if output_file_name == "":
            output_file_name = "splitted_"

        if output_file_flag:
            with open(
                f'{output_file_name}{int(time.time())}.txt', "a", encoding="utf-8"
            ) as output_file:
                output_file.write(output)

        return output

    def load_input_string(self, file_path: str) -> str:
        """method set_input_text"""
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                return file.read()
        except Exception as error:
            return f'WARNING: An error occured while reading the file with message: {error}'
