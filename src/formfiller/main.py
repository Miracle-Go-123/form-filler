#!/usr/bin/env python
import sys
import warnings

from formfiller.crew import Formfiller
import json

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
# read the user response json


def run():
    """
    Run the crew.
    """
    # with open("assets/jsons/pdf_form_schema.json", "r") as file:
    #     pdf_form_schema = json.load(file)
    # with open("../assets/jsons/result.json", "r") as file:
    #     user_response = json.load(file)
    inputs = {
        "user_response": '/Volumes/Drive D/vizafi/python/formfiller/assets/jsons/result.json',
        "pdf_form_schema": '/Volumes/Drive D/vizafi/python/formfiller/assets/raw_pdfs/i-90.pdf',
    }
    Formfiller().crew().kickoff(inputs=inputs)


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         Formfiller().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         Formfiller().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         Formfiller().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
