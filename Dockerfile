FROM python:alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8777
CMD ["python", "app.py"]


