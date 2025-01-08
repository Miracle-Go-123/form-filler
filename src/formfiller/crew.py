from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from PyPDFForm import PdfWrapper
import json
import re
from pydantic import BaseModel
from typing import List, Union
# Uncomment the following line to use an example of a custom tool
# from formfiller.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

class Pydantic(BaseModel):
   field_key : str
   answer : Union[str, int, bool]

class outputPydantic(BaseModel):
	response: List[Pydantic]
@CrewBase
class Formfiller():
	"""Formfiller crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff # Optional hook to be executed before the crew starts
	def parse_pdf(self, inputs):
		"""
		Logic for pdf parsing using custom pypdfform
		"""
		self.pdf_obj = inputs['pdf_form_schema']
		pdf_form_schema = PdfWrapper(self.pdf_obj).schema
		pdf_form_schema_json = json.dumps(pdf_form_schema, indent=4, sort_keys=True)
		modified_inputs = {
        "user_response": inputs['user_response'],
        "pdf_form_schema": pdf_form_schema_json,
    	}
		return modified_inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def fill_pdf(self, output):
		"""
		Logic to validate and process the output JSON
		"""
		try:
			# Convert CrewOutput to JSON string
			output_str = output.to_dict()
			if output_str is None:
				return None
			filled_res = {}
			for dic in output_str['response']:
				if dic['answer'] != "":
					filled_res[dic['field_key']] = dic['answer']
			filled = PdfWrapper(self.pdf_obj).fill(
				filled_res
			)
			# return filled
			with open("/Volumes/Drive D/vizafi/python/formfiller/assets/gen_pdfs/output.pdf", "wb+") as output:
				output.write(filled.read())
			# Optional Save the json to a file 
			with open("/Volumes/Drive D/vizafi/python/formfiller/assets/jsons/response.json", "w") as file:
				json.dump(output_str, file, indent=4, sort_keys=True)
			return 'Form filled successfully'
		
		except AttributeError as e:
			print(f"Error converting CrewOutput to JSON: {e}")
			return None
	@agent
	def form_filler(self) -> Agent:
		return Agent(
			config=self.agents_config['form_filler'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	@task
	def form_filling_task(self) -> Task:
		config=self.tasks_config['form_filling_task']
		config['output_json'] = outputPydantic
		return Task(
			config=config,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Formfiller crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=False,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
