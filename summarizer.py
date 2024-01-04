from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.prompts import PromptTemplate

from langchain.chains import LLMChain


def get_summary(content):
    llm = Ollama(
        model="mistral",
        #  callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]),
        temperature=0.9,
    )

    prompt = PromptTemplate(
        input_variables=["text"],
        template="Generate the summary of the following text. Include key points and TLDR: {text}",
    )

    chain = LLMChain(llm=llm, prompt=prompt, verbose=False)

    return chain.run(content)
