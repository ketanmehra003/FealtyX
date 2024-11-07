from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Initialize the LLM model once to avoid redundant instantiation
model = OllamaLLM(model="llama3.2")

def get_student_summary(student_data):
    # Validate that all required keys are in student_data
    required_keys = {"name", "age", "email"}
    if not required_keys.issubset(student_data):
        missing_keys = required_keys - student_data.keys()
        raise ValueError(f"Missing required student data fields: {', '.join(missing_keys)}")

    # Construct the prompt template using validated student details
    template = """
    Question: Given the following student data, provide a direct profile summary that includes only the provided information, without mentioning missing information or any introductory phrases.

    Student Data:
    - Name: {name}
    - Age: {age}
    - Email: {email}

    Answer: Summarize in one sentence using only the details provided, without mentioning missing information or extra context.
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Chain prompt with the model and invoke the response
    chain = prompt | model
    try:
        response = chain.invoke(student_data)
    except Exception as e:
        raise RuntimeError(f"Failed to generate student summary: {e}")

    # Optional: Clean up response if needed
    return response.strip() if isinstance(response, str) else response
