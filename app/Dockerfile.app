# Use a Python base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app


# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python
COPY weather_app.py .

EXPOSE 8501

CMD ["streamlit", "run", "weather_app.py", "--server.port", "8501"]
