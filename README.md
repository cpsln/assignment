## Setup:

1. Install Python [v3.9.6] (https://www.python.org/downloads/release/python-390/) or above.

2. Download and install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/).
    - Run the docker desktop and accept terms and conditions.
    
3. Run the following command from project's root directory:
    ```sh
      docker-compose -f docker-compose.yaml up -d --build
    ```
4. Setup virtual environment, activate and run following command root directory:
    ```sh
      pip install -r requirement.txt
    ```
5. Run the following command root directory:
    ```sh
      uvicorn main:app --reload
    ```