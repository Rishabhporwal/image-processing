# Local Running

    - python -m venv AIQ(Environment Name)
    - source AIQ/Scripts/activate
    - pip install -r requirement.txt
    - python main.py

    -  Run In Browser : http://127.0.0.1:8080/

# Executing in Docker

    - docker build -t image-resize-api .
    - docker run -p 8080:8080 image-resize-api
    - Run In Browser : http://127.0.0.1:8080/
