**Flask CSV Chatbot API**

This project provides a Flask-based API that allows users to upload CSV files and ask questions about the data using OpenAI's language model.

\## Features

\- Accepts CSV files or ZIP archives containing CSV files.

\- Processes queries on the uploaded dataset using OpenAI.

\- Returns a natural language response based on the data.

\## Installation

\### Prerequisites

\- Python 3.8+

\- Flask

\- OpenAI API key

\- Required dependencies listed in \`requirements.txt\`

\### Setup

1\. Clone the repository:

\`\`\`sh

git clone <https://github.com/your-repo/flask-csv-chatbot.git>

cd flask-csv-chatbot

1. Install dependencies:

sh

CopyEdit

pip install -r requirements.txt

1. Create a .env file and add your OpenAI API key:

ini

CopyEdit

OPENAI_API_KEY=your_api_key_here

1. Run the application:

sh

CopyEdit

python app.py

**API Usage**

**Endpoint**

**URL:** <https://iitmproject2.onrender.com/api/>

**Method:** POST

**Request Format**

Use the following cURL command to test the API:

sh

CopyEdit

curl -X POST "<https://iitmproject2.onrender.com/api/>" \\

\-F "question=Question to be asked" \\

\-F "file=@/path/to/your/file.csv"

**Response Format**

The API will return a JSON response:

json

CopyEdit

{

"answer": "Your response based on the CSV data."

}

**Deployment**

You can deploy this API on platforms like **Render, Vercel, or AWS Lambda** using **Mangum** for serverless deployment.

**License**

This project is licensed under the MIT License.

**Author**

Developed by Rohit Sharma (<23f2002473@ds.study.iitm.ac.in>).

vbnet

CopyEdit

Let me know if you need any changes! 🚀
