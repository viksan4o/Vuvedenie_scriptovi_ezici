def analyze_text_file(filename):
    with open(filename, "r") as f:
        text = f.read()
    punct = ".,!?;:„“\"'-…"
    p_count = sum(1 for c in text if c in punct)
    for p in punct:
        text = text.replace(p, " ")
    words = text.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    most_common = max(counts, key=counts.get) if counts else "No words"
    print("Words:", len(words))
    print("Punctuation marksи:", p_count)
    print(f"Most common word: {most_common} ({counts.get(most_common, 0)} times)")
