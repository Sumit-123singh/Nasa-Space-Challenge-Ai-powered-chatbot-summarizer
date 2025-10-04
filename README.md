# NASA Bioscience Chatbot with Gemini AI

A **one-to-one user query chatbot** built with **FastAPI** that lets users explore, summarize, and visualize **NASA bioscience research data** using **Google Gemini AI**. This backend handles dynamic user queries, maintains personalized chat sessions, and returns context-aware responses.

---

## 🚀 Features

- **Dynamic Queries:** Users can ask **any question** related to NASA bioscience research or general knowledge.
- **One-to-One Sessions:** Each user has a **personalized conversation history**.
- **Context-Aware Responses:** Gemini AI uses previous messages to generate relevant replies.
- **Async & Scalable:** Uses `httpx.AsyncClient` to handle multiple simultaneous requests.
- **Timeout & Error Handling:** Safely handles API timeouts, HTTP errors, and unexpected exceptions.
- **Easy Integration:** Clean JSON input/output for web or mobile frontends.
- **NASA-Style Interface Ready:** Backend designed for futuristic NASA bioscience web apps.

---

## 💻 Tech Stack

- **Backend:** FastAPI  
- **AI:** Google Gemini API (`gemini-2.5-pro` model recommended)  
- **HTTP Requests:** `httpx` (async)  
- **Environment Variables:** `python-dotenv`  
- **Python Version:** 3.10+  

---

## 📁 Project Structure

