# Use an official Python runtime as an image
FROM python:3.6

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY wait-for-it.sh /app/
RUN chmod +x wait-for-it.sh
COPY *.py /app/

CMD ["./wait-for-it.sh", "mysql:3306", "-t", "120", "--", "python", "bot.py"]
