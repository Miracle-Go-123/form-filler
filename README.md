# Formfiller Crew

Welcome to the Formfiller Crew project
## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system.



```bash
$ pip install crewai[tools] uvicorn 
```

## Running
This command initializes the formfiller Crew, assembling the agents and assigning them tasks as defined in your configuration.

1. Navigate to src/formfiller in terminal
2. Start the server
```bash
$ uvicorn main:app --reload
```
3. Send Request to server
```bash
$ python test_server.py
```
## Understanding Your Crew

The formfiller Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

