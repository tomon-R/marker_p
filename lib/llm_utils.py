import os
from pathlib import Path

import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def process_md_with_llm(md_path):
    """
    Processes a Markdown file with the new Assistants API and saves the result in llm_out/{directory name}.
    """
    md_path = Path(md_path)
    if not md_path.exists() or not md_path.suffix == ".md":
        raise ValueError(f"Invalid Markdown file: {md_path}")

    output_dir = Path("llm_out") / md_path.parent.parent.name / md_path.parent.name
    output_dir.mkdir(parents=True, exist_ok=True)

    with md_path.open("r") as f:
        md_content = f.read()

    # Combine the role description with the Markdown content
    role_description = """
    ## Background
    You are an assistant responsible for proofreading Markdown files. These Markdown files consist of natural language, figures, tables, and equations, and are generated using an OCR tool (marker-pdf). Your task is to understand the context, fill in incomplete content, and correct the information to make it accurate. 
    
    ## instructions
    - Correct the content to be natural.
    - Equations should be re-interpret in LaTeX format.
    - Tables are most likely mis-recognized and ordered unorganized way. Please re-interpret them in a persistent way.
    - Complex characters are sometimes mis-recognized as characters from another language. Assume the characters in the language that is natural in the context.
    - **THIS PROCESS SHOULD BE APPLIED THE FULL CONTENT.**
    - **YOU SHOULD OUTPUT FULL THE CONTENT.**
    - **DO NOT SAY ANY OTHER THINGS THAN THE CONTENT OF THE CONTENT.**
    """

    query = f"{role_description}\n\n## Markdown Content\n{md_content}"

    try:
        # Invoke OpenAI API for completion with the required parameters
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model="gpt-4o",
        )

        # Extract the assistant's response from the response object
        if response:
            print("got response:")
            print(response)
        response_content = response.choices[0].message.content

        # Save the response to the output directory
        response_file = output_dir / md_path.name
        with response_file.open("w") as f:
            f.write(response_content)

        print(f"Processed {md_path} with LLM and saved output at {response_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
