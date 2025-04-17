FROM python:3.11-slim

# Sets the working directory
WORKDIR /app

# Copies only requirements first to take advantage of the cache
COPY requirements.txt .

# Installs dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copies the rest of the code
COPY . .

# Exposes the port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
