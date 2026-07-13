
FROM alpine:3.19

RUN apk update && apk add --no-cache python3

WORKDIR /app

COPY app.py /app/app.py

EXPOSE 8080

CMD ["python3", "/app/app.py"]
