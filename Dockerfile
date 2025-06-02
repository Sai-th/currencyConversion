# get a lightweight python image from official python 3.11
FROM python:3.11-slim 

# sets working directory inside /app inside the ocntainer 
WORKDIR /app 

#copies requirements.txt to /app for ease of execution
COPY requirements.txt requirements.txt 

#removes packages cache after installation to save space
RUN pip install --no-cache-dir -r requirements.txt 

#copies all the files and folders from currencyConversion to container so the wprk is done smoothly
COPY . .

#runs python app.py when the container is generated using this image.
CMD ["python", "app.py"]