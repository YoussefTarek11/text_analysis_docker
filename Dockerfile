FROM python:3.9-slim
WORKDIR /app

RUN pip install nltk

COPY . .

CMD ["python", "text_analysis.py"]
