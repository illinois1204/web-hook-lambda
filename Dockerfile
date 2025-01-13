FROM python:3.12.8-alpine3.20

WORKDIR /src/app
COPY . .
RUN pip install -r requirements.txt && \
    pip install "uvicorn[standard]"

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "warning"]