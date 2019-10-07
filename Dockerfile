
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /genderApp

# Set the working directory to /genderApp
WORKDIR /genderApp

# Copy the current directory contents into the container at /genderApp
ADD . /genderApp/

# Install any needed packages specified in requirements.txt
RUN python3 -m pip install -r requirements.txt

CMD ["python", "genderApp.py"]