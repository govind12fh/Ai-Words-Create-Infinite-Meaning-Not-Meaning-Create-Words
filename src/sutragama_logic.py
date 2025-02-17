import json

knowledge_base = {
    "Atman": "Eternal and beyond sensory perception.",
    "Karma": "Cause and effect governing actions.",
    "Moksha": "Liberation achieved through knowledge."
}

def infer_from_sutragama(query):
    return knowledge_base.get(query, "Unknown concept in current knowledge base.")

if __name__ == "__main__":
    test_query = "Karma"
    print(f"Answer: {infer_from_sutragama(test_query)}")
    src/sutragama_logic.py
