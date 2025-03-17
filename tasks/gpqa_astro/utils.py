import datasets
import random

# Prompt template from simple-evals: https://github.com/openai/simple-evals/blob/83ed7640a7d9cd26849bcb3340125002ef14abbe/common.py#L14
GPQA_QUERY_TEMPLATE = """
Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering.

{Question}

A) {A}
B) {B}
C) {C}
D) {D}
""".strip()

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        # Format the question
        question = doc["Question"]
        
        # Get the correct answer and incorrect answers
        correct_answer = doc["Correct Answer"]
        incorrect_answers = [
            doc["Incorrect Answer 1"],
            doc["Incorrect Answer 2"],
            doc["Incorrect Answer 3"]
        ]
        
        # Randomly insert the correct answer among the incorrect ones
        gold_index = random.randint(0, 3)
        options = incorrect_answers.copy()
        options.insert(gold_index, correct_answer)
        
        # Format the query using the template
        query = GPQA_QUERY_TEMPLATE.format(
            Question=question,
            A=options[0],
            B=options[1],
            C=options[2],
            D=options[3]
        )
        
        # Create the output document
        out_doc = {
            "query": query,
            "answer": chr(65 + gold_index)
        }
        return out_doc

    # Add remove_columns parameter to keep only the new columns
    return dataset.map(_process_doc, remove_columns=dataset.column_names)
