# Base image
FROM python:3.11

# Installing OpenCV dependencies
RUN apt-get update -y && \
    apt-get install ffmpeg libsm6 libxext6 tk -y

# # Copying source code to container
COPY . src

WORKDIR /src

# pip install dependencies
RUN pip install -r requirements.txt && \
    pip install jupyter pandas numpy seaborn opencv-python jupyter-black boto3 python-dotenv&& \
    pip freeze > requirements.txt

# Commands to run Tkinter application
CMD ["/src/desktop_app/main.py"]
ENTRYPOINT ["python3"]