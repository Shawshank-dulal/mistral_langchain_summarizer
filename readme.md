# Text Summarizer and Keypoints Generator

## Uses Langchain and Mistral AI to summarize text and geenrate keypoints

## Features

- Text summarization
- key ideas generation
- TLDR generation

## How to Run?

### Install Dependencies

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Install ollama and run mistral

```sh
curl https://ollama.ai/install.sh | sh
ollama serve
ollama run mistral
```

### Run Fastapi

```sh
uvicorn app:app --reload
```

Now your summarizer API is ready just do a post request on localhost:8000/summary and body should be like this:

```sh
{url:"url of the transcript"}
```
