# Stage 1: Build
FROM golang:1.24-alpine AS builder

WORKDIR /app
COPY go.mod .          
COPY main.go .

RUN go build -o my-app

# Stage 2: Run
FROM scratch
COPY --from=builder /app/my-app /my-app
EXPOSE 8080
ENTRYPOINT ["/my-app"]
