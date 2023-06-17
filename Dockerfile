# The base image
FROM python:alpine
 
# Maintiner
LABEL maintainer="chlin@pdx.edu"

# Copy the content into contrainer dir 
COPY . /app

# Set the working dir of the contianer
WORKDIR /app

# Install packages
RUN pip install --no-cache -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
