from dotenv import load_dotenv
from langchain import LLMChain, HuggingFaceHub

load_dotenv()

hub_llm = HuggingFaceHub(repo_id="mrm8488/t5-base-finetuned-wikiSQL")
# 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
