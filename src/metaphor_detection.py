from transformers import pipeline

def detect_metaphors(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["literal meaning", "metaphorical meaning"]
    result = classifier(text, candidate_labels=labels)
    return result

if __name__ == "__main__":
    test_text = "Time is a thief that steals our moments."
    print(detect_metaphors(test_text))
    src/metaphor_detection.py
