#Task 1
# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# List of keywords to highlight
keywords = ["good", "excellent", "bad", "poor", "average"]

# Function to highlight keywords
def highlight_keywords(reviews, keywords):
    for review in reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print(highlighted_review)

# Call the function
highlight_keywords(reviews, keywords)

#Task 2


# Positive and negative word lists
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function to tally positive and negative words
def sentiment_tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0
    
    for review in reviews:
        # Convert review to lowercase for case-insensitive matching
        review_lower = review.lower()
        
        # Count positive words
        for word in positive_words:
            total_positive += review_lower.count(word)
        
        # Count negative words
        for word in negative_words:
            total_negative += review_lower.count(word)
    
    return total_positive, total_negative

# Call the function and get the result
positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)

# Display the result
print(f"Total Positive Words: {positive_count}")
print(f"Total Negative Words: {negative_count}")

#Task 3

def review_summary(review, max_length=30):
    # Trim review to the max_length and ensure we don't cut off words
    if len(review) > max_length:
        # Find the last space within the allowed range
        end_index = review.rfind(' ', 0, max_length)
        if end_index == -1:
            end_index = max_length  # If no space found, just cut at max_length
        summary = review[:end_index] + "..."
    else:
        summary = review
    
    return summary

# Generate and print summaries for each review
for review in reviews:
    print(review_summary(review))