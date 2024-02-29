FROM alpine:3.16
WORKDIR /Restaurante_APP
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
COPY /requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
LABEL authors="matheuss.fernandes"
CMD ["uvicorn", "restaurant_API:app", "--host", "0.0.0.0", "--port", "8000"]