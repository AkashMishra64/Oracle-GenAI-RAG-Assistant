import oracle_ads
from langchain.llms import OracleGenAI

def query_enterprise_data(prompt):
    # Using Oracle GenAI to generate SQL from natural language for Data Analysts
    llm = OracleGenAI(model_id="cohere.command")
    return llm.generate([prompt])