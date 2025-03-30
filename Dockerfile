# Start with a slim Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory
COPY . .

# Expose the port FastAPI will run on
EXPOSE 80

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
