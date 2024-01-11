FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
ENV PYTHONBUFFERED True
WORKDIR /app
COPY . .
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt