import datasets
import random

SUPER_GPQA_QUERY_TEMPLATE = """
Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is the correct option letter. Think step by step before answering.

{Question}

{Options}
""".strip()

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        answer_letter = doc["answer_letter"]

        options = []
        letters = [chr(ord('A') + i) for i in range(len(doc["options"]))]
        for letter, option in zip(letters, doc["options"]):
            options.append(f"{letter}) {option}")
        options_str = "\n".join(options)

        query = SUPER_GPQA_QUERY_TEMPLATE.format(
            Question=doc["question"],
            Options=options_str
        )

        out_doc = {
            "query": query,
            "answer": answer_letter
        }
        return out_doc

    return dataset.map(_process_doc, remove_columns=dataset.column_names)
