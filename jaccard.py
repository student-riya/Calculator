import math

def jaccard_similarity(set1, set2):
    """
    Compute the Jaccard Similarity between two sets.
    Jaccard Similarity = (Size of Intersection) / (Size of Union)
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0.0

def cosine_similarity(set1, set2):
    """
    Compute the Cosine Similarity between two sets.
    Cosine Similarity = (Size of Intersection) / (sqrt(size(set1)) * sqrt(size(set2)))
    """
    intersection = len(set1.intersection(set2))
    norm1 = math.sqrt(len(set1))
    norm2 = math.sqrt(len(set2))
    return intersection / (norm1 * norm2) if norm1 != 0 and norm2 != 0 else 0.0

# Example Usage
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "fig"}

jaccard = jaccard_similarity(set_a, set_b)
cosine = cosine_similarity(set_a, set_b)

print(f"Jaccard Similarity: {jaccard:.4f}")
print(f"Cosine Similarity: {cosine:.4f}")
