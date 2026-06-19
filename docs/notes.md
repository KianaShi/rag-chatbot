# Day 1 Notes
- What is RAG?
Retrieve information first, then let LLM generate answers.
- Chunking concern
Chunking may be inaccurate if important context is split across chunks.
Possible solutions include paragraph-based splitting, overlap, and tuning chunk size. 
- What does embedding do?
Embedding converts text into vectors. Similar meanings are represented by vectors that are close to each other.
This allows the system to find relevant information even when different words are used.
- Why use vector databases?
Vector databases store embeddings and make similarity search efficient.
When a user asks a question, the question is also converted into a vector. The system then finds the most similar chunks and sends them to the LLM.
- What does the LLM do?
The LLM mainly organizes retrieved information into natural language.
In a RAG system, retrieval provides knowledge, while the LLM provides expression and reasoning.
Incorrect retrieval may lead the LLM to generate incorrect answers, even if the model itself is powerful.
- Personal Thoughts
My intuition is that a vector database and retriever are somewhat similar to a HashMap, but with fuzzy matching instead of exact matching.
A HashMap returns a value when the key matches exactly. In contrast, a retriever returns the top-k chunks whose vectors are closest to the query vector.
This analogy is not perfectly accurate, but it helps me understand how retrieval works.

# Day 2 Design
Input: file_path
Output: list[str]
Behavior: Ignore empty lines.
Different file formats should return the same output structure.
