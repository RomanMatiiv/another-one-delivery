FROM golang:1.21.3-alpine3.18
LABEL authors="matiiv"

ENV OUTPUT_FILE="catalog"

WORKDIR app

COPY . .

RUN go build -o $OUTPUT_FILE main.go