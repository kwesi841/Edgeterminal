FROM python:3.11-slim

WORKDIR /work
COPY requirements.txt /work/requirements.txt
RUN pip install --no-cache-dir -r /work/requirements.txt
COPY . /work

EXPOSE 8000
CMD ["uvicorn", "edge-terminal.backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
