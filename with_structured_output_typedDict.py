from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model=ChatOpenAI()
reviews = [
    "This laptop exceeded my expectations with its fast performance and excellent battery life.",
    "The product quality is outstanding, and the packaging was secure and premium.",
    "Customer support responded quickly and resolved my issue within a few hours.",
    "The interface is clean, intuitive, and very easy to use even for beginners.",
    "Overall, I am highly satisfied with the purchase and would definitely recommend it to others."
]
class Review(TypedDict):

  summary:str
  sentiment:str

structured_Model= model.with_structured_output(Review)

result=structured_Model.invoke(reviews)

print(result)
print(result['summary'])
print(result['sentiment'])