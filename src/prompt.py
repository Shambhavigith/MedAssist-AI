def build_context(retrieved_docs):

    context = ""

    for i, doc in enumerate(retrieved_docs, start=1):

        context += f"""
Document {i}:

{doc.page_content}

====================================
"""

    return context


def build_prompt(context, query):

    prompt = f"""
You are MedAssistAI, an AI-powered medical information assistant.

Answer the user's question using the provided context as the primary source of information.

Guidelines:
- Focus only on information relevant to the user's query.
- Summarize the retrieved information clearly and concisely.
- Do not include unrelated or repetitive details.
- If the answer is not available in the provided context, say:
  "I could not find sufficient information in the available medical sources."
- Do not make up information.
- Do not provide a diagnosis, treatment plan, or professional medical advice.
- Include a brief disclaimer that the response is for informational purposes only and is not a substitute for professional medical consultation.

Context:
{context}

User Question:
{query}

Answer:
"""

    return prompt
