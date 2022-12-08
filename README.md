# talana_kombat
Talana challenge.

## Description

1. The **game.py** and **player.py** files are the classes used to simulate the game.
2. Inside the test directory, the **test.py** file, are the unit tests for the two example cases found in the document plus two test cases that you add. They simulate the game.
3. In the file **answer.txt** is located all challenge answers.


## Prepare local environment

1. Create environment: `python -m venv venv/talana_kombat` 
2. Activate the environment: `source venv/talana_kombat/bin/activate`
3. Instal requirements for grant unit tests: `pip install -r requirements.txt` 

## Run tests

1. With environment activated just run: `pytest -q tests/test.py`


# Run with docker

1. Build image: `docker build . -t talent_kombat:1.0.0`
2. Create a container for test executions: `docker run -itd --name talana_kombat talana_kombat:1.0.0`
3. Now you are able to enter container and run test yourself:
   
   ``` 
   > docker exec -it talana_kombat sh
   /app # pytest -q tests/test.py
   ```

