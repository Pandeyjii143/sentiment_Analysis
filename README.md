# 😊 Sentiment Analysis using LangChain & ChatOpenAI

A simple and efficient **Sentiment Analysis** application built using **LangChain** and **OpenAI's ChatOpenAI**. This project demonstrates how to leverage Large Language Models (LLMs) to classify text into **Positive**, **Negative**, or **Neutral** sentiments using structured outputs.

---

## 🚀 Features

* 🤖 Powered by **LangChain**
* 🧠 Uses **ChatOpenAI** for sentiment classification
* 📋 Structured output with **TypedDict**
* ⚡ Fast and lightweight implementation
* 🔧 Easy to customize for different use cases
* 📦 Beginner-friendly project structure

---

## 🛠️ Tech Stack

* Python 3.10+
* LangChain
* LangChain OpenAI
* OpenAI GPT Models
* python-dotenv

---

## 📂 Project Structure

```text
Sentiment-Analysis/
│── with_structured_output_typedDict.py
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Sentiment-Analysis.git
cd Sentiment-Analysis
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💡 Example

**Input**

```text
I absolutely love this product! It works perfectly and exceeded my expectations.
```

**Output**

```text
Sentiment: Positive
```

---

## 📌 Example Structured Output

```python
from typing import TypedDict

class Sentiment(TypedDict):
    sentiment: str
```

Example response:

```python
{
    "sentiment": "Positive"
}
```

---

## 📦 Requirements

```text
langchain
langchain-openai
python-dotenv
openai
```

---

## 🎯 Learning Outcomes

* Integrating LangChain with OpenAI models
* Using `ChatOpenAI`
* Working with structured outputs (`TypedDict`)
* Prompt engineering fundamentals
* Building simple LLM-powered applications

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, improve the project, and submit a pull request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates future improvements.

---

## 📜 License

This project is licensed under the MIT License.
