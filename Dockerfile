FROM python:3.10-slim
WORKDIR /app

COPY .env .env
# .env 파일 검증
RUN if [ -n "$(grep 'ENV_CHECK' .env)" ]; then \
echo ".env is missing ENV_CHECK" && exit 1; \
    fi

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main_sensor.py"]
