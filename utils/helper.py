import re




# ==================================
# Clean News Text
# ==================================

def clean_text(text):

    """
    Preprocess news text before ML prediction.
    """

    if not text:

        return ""


    # Convert to string

    text = str(text)



    # Lowercase

    text = text.lower()



    # Remove URLs

    text = re.sub(
        r"http\S+|www\S+",
        "",
        text
    )



    # Remove HTML tags

    text = re.sub(
        r"<.*?>",
        "",
        text
    )



    # Remove email addresses

    text = re.sub(
        r"\S+@\S+",
        "",
        text
    )



    # Remove punctuation

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )



    # Remove numbers

    text = re.sub(
        r"\d+",
        "",
        text
    )



    # Remove extra spaces

    text = " ".join(
        text.split()
    )



    return text






# ==================================
# Format Prediction Result
# ==================================

def format_result(prediction):

    """
    Convert ML prediction into readable result.

    Dataset:
    0 = Fake News
    1 = Real News
    """



    try:

        prediction = int(prediction)


    except Exception:


        return "Unknown"





    if prediction == 1:


        return "Real News"




    elif prediction == 0:


        return "Fake News"




    else:


        return "Unknown"








# ==================================
# Calculate Confidence
# ==================================

def calculate_confidence(probabilities):

    """
    Convert model probability into percentage.
    """



    if probabilities is None:


        return 0





    confidence = max(
        probabilities
    ) * 100




    return round(
        float(confidence),
        2
    )