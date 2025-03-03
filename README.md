# LLM App With LCEL

This repository provides a basic Language Model (LLM) application using Langchain Expression Language (LCEL). It covers the basics of building an API with FastAPI, handling requests with `requests`, running the server with `uvicorn`, and creating a client with Streamlit. You can also test the API on Postman. Screenshots are attached to help illustrate the workflow.

![View of Streamlit APp](https://github.com/user-attachments/assets/bb86a3a7-4287-4cf9-8ed2-857ace8c6744)

## Overview

The project demonstrates how to:

- Build a FastAPI server that leverages Langchain components for prompt engineering and language model inference.
- Create a simple client using the `requests` library and Streamlit to interact with the API.
- Integrate several important libraries, including **FastAPI**, **uvicorn**, **python-dotenv**, **langchain_groq**, **langchain_core**, and **streamlit**.
- Cover the basics of API development, deployment, and testing.

## Features

- **FastAPI Server:**  
  Provides a RESTful API endpoint that accepts a text input and a target language, translates the input using a configured language model, and returns the response.

- **Client Application:**  
  A simple Streamlit app that allows users to input text, select a target language, and see the translated output.

- **API Testing:**  
  You can test the API endpoint on Postman by sending a POST request to the `/chain/invoke` endpoint.

## Technologies and Libraries

- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python.
- **uvicorn:** An ASGI server used to run the FastAPI application.
- **requests:** For making HTTP requests in the client.
- **python-dotenv:** Loads environment variables from a `.env` file.
- **langchain_groq:** For interacting with the language model via the Groq API.
- **langchain_core:** Provides core prompt templating and output parsing functionalities.
- **Streamlit:** Used to build the simple client UI for interacting with the API.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/EniolaAdemola/LLM-App-With-LCEL.git
   ```

   ```bash
   cd LLM-App-With-LCEL

   ```

2. **Create and activate a virtual environment (optional but recommended) for me i used conda:**

   ```bash
   conda create -p venv python==3.10 -y
   ```

   ```bash
   conda activate venv

   ```

3. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Set up environment variables:**
   Create a .env file in the root directory with the following keys:
   ```bash
   GROQ_API_KEY=your_groq_api_key
   ```

---

## Running the Application

### 1. Start the Server

To run the FastAPI server, execute:

```bash
python server\server.py

```

The server will be accessible at http://127.0.0.1:8000. Make sure to add "/docs" to view the Langserve documentations (http://127.0.0.1:8000/docs/)

![View of the langserve server](https://github.com/user-attachments/assets/41f4b64e-4777-440b-a150-b5f3093f91b0)
![langserve_docs1](https://github.com/user-attachments/assets/a3cb6214-e028-496a-b0cf-be2078813153)
![langserve_docs2](https://github.com/user-attachments/assets/5fb003a9-beb9-4af6-862d-2de3de9fd59c)

### 2. Run the Streamlit Client

To start the client application, run:

```bash
streamlit run client\client.py

```

You can then interact with the LLM application using the provided web interface.
![View of Streamlit APp](https://github.com/user-attachments/assets/bb86a3a7-4287-4cf9-8ed2-857ace8c6744)

---

## API Endpoints

POST /chain/invoke
This endpoint accepts a JSON payload with the following structure:

```bash
{
    "input": {
        "language": "French",
        "text": "Your input text here"
    },
    "config": {},
    "kwargs": {}
}
```

It returns a JSON response with the translated or processed output.

#### Testing with Postman

You can test the API on Postman by sending a POST request to:

```bash
streamlit run client\client.py](http://127.0.0.1:8000/chain/invoke

```

Make sure to set the request body to JSON with the structure shown above.

![output](https://github.com/user-attachments/assets/9883b3ba-43cc-4d11-af91-9aa0bd00b464)

## 🤝 Contributing

Contributions are welcome! Feel free to submit a PR or open an issue.

## 📞 Contact

For inquiries, reach out to [Eniola Ademola](https://github.com/EniolaAdemola).

---
