FROM python:3.9-alpine3.18

WORKDIR /

COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install pandas
RUN pip install zenml

COPY . .
CMD ["python", "run_pipeline.py"]