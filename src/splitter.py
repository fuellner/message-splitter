"""module Splitter"""


class Splitter:
    """class for splitting functionality"""

    def __init__(self, chunk_size: int, input_text: str) -> None:
        self.chunk_size: int = chunk_size - 4
        self.input_text: str = input_text
        self.output_text: str = ""

    def split_message(self) -> str:
        """method which does the actual splitting"""
        if self.chunk_size < 1 or not self.input_text:
            return ""

        chunks: list[str] = []
        offset: int = 0
        input_text_length: int = len(self.input_text)
        i: int = 0
        optional_space: str = ""

        while i <= input_text_length:
            if (i + self.chunk_size <= input_text_length) and self.input_text[i + self.chunk_size] != " ":
                while offset < self.chunk_size and self.input_text[i + (self.chunk_size - offset)] != " ":
                    offset += 1
                    optional_space = ""
            if offset == self.chunk_size:
                offset = 0
                optional_space = " "
            chunks.append(self.input_text[i: i + self.chunk_size - offset])
            i = i + self.chunk_size - offset
            offset = 0
        chunk_count = len(chunks)
        chunks[0] = "1" + "/" + str(object=chunk_count) + " " + chunks[0]

        for k in range(1, chunk_count, 1):
            chunks[k] = str(k + 1) + "/" + str(object=chunk_count) + \
                optional_space + chunks[k]

        for chunk in chunks:
            self.output_text = self.output_text + chunk + \
                "\n\n--------------------------------------\n\n"

        return self.output_text
