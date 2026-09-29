import re



# ==================================
# Validate Email
# ==================================

def validate_email(email):

    """
    Validate email format.
    """

    if not email:
        return False


    pattern = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )


    return bool(
        re.match(
            pattern,
            email
        )
    )





# ==================================
# Validate Password
# ==================================

def validate_password(password):

    """
    Password Rules:

    - Minimum 8 characters
    - One uppercase letter
    - One lowercase letter
    - One number
    """

    if not password:

        return False



    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'.{8,}$'
    )


    return bool(
        re.match(
            pattern,
            password
        )
    )





# ==================================
# Validate News Text
# ==================================

def validate_news(news_text):


    if not news_text:

        return False



    news_text = news_text.strip()



    # Minimum news length

    if len(news_text) < 20:

        return False



    return True





# ==================================
# Validate Required Fields
# ==================================

def validate_required(*fields):


    for field in fields:


        if field is None:

            return False



        if not str(field).strip():

            return False



    return True





# ==================================
# Validate Full Name
# ==================================

def validate_name(name):


    if not name:

        return False



    pattern = (
        r'^[A-Za-z ]{3,50}$'
    )


    return bool(
        re.match(
            pattern,
            name
        )
    )





# ==================================
# Validate Password Match
# ==================================

def validate_password_match(
        password,
        confirm_password
):


    if password != confirm_password:

        return False


    return True