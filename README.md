# Flashcards Application

This application is a web-based flashcard system designed to help users learn and review information interactively. It features a collection of flashcards that cover various topics, allowing users to flip between questions and answers. The app is built using FastAPI for the backend and serves HTML content to the frontend, providing a seamless and engaging learning experience.

## HTTP Call Sequence

```mermaid
sequenceDiagram
    participant User
    participant Endpoint
    participant HTML

    User->>Endpoint: GET /
    Endpoint->>HTML: Read flashcards.html
    HTML->>Endpoint: GET /flashcards
    Endpoint->>HTML: Read flashcards.json
    HTML->>User: Serve html
```

## Running the Application with Docker Compose

To run the application using Docker Compose, follow these steps:

1. **Rename the Environment File**

   First, rename the `.env.sample` file to `.env`:

   ```bash
   mv .env.sample .env
   ```

   Ensure that you replace `<ngrok_token>` in the `.env` file with your actual ngrok token.

2. **Run Docker Compose**

   Use the following command to start the services defined in the `docker-compose.yml` file:

   ```bash
   docker-compose up
   ```

   This will start both the API and ngrok services. The application will be accessible at `http://localhost:8000`, and the ngrok web interface will be available at `http://localhost:4040`.

## Building and Running the Docker Container

To build and run the Docker container for this application, follow these steps:

1. **Build the Docker Image**

   Open a terminal in the root directory of the project and run the following command to build the Docker image:

   ```bash
   docker build -t flashcards-app .
   ```

2. **Run the Docker Container**

   Once the image is built, run the container using the following command:

   ```bash
   docker run -p 8000:8000 flashcards-app
   ```

   This will start the application, and it will be accessible at `http://localhost:8000`.

## Development Tools Used

This project was developed in less than an hour using the following tools:

- **Visual Studio Code (VSCode)**: A versatile and powerful source code editor that supports a wide range of programming languages and extensions. It was used for writing, debugging, and managing the codebase. [Link to VSCode](https://code.visualstudio.com/)

- **Grok**: An AI-powered coding assistant that provides real-time code suggestions and explanations, helping to improve coding efficiency and learning. [Link to Grok](https://x.ai/)

- **Aider**: A tool that assists in generating and refining code, documentation, and other development tasks through AI-driven suggestions and automation. [Link to Aider](https://aider.chat/)

These tools significantly enhanced the development process, making it more efficient and collaborative.
