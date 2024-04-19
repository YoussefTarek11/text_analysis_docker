# Use a slim Python 3.9 base image (adjust version as needed)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install NLTK dependencies
RUN pip install nltk

# Copy Python script and text file
COPY . .

# Command to run the script
CMD ["python", "text_analysis.py"]
