from transformers import pipeline


class Hubert:
    def autocomplete(self, input_str: str) -> str:
        generator = pipeline("text-generation")
        return generator(input_str)
