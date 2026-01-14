def response(hey_bob):
    """Determine Bob's response based on what is said to him.
    
    Bob's responses:
    - "Sure." - if you ask him a question (ends with ?)
    - "Whoa, chill out!" - if you YELL AT HIM (all caps)
    - "Calm down, I know what I'm doing!" - if you yell a question
    - "Fine. Be that way!" - if you say nothing (silence/whitespace)
    - "Whatever." - anything else
    
    :param hey_bob: str - what is said to Bob.
    :return: str - Bob's response.
    
    Examples:
    >>> response("How are you?")
    'Sure.'
    >>> response("WATCH OUT!")
    'Whoa, chill out!'
    >>> response("WHAT'S GOING ON?")
    'Calm down, I know what I'm doing!'
    >>> response("   ")
    'Fine. Be that way!'
    >>> response("Let's go to the park.")
    'Whatever.'
    """
    # Strip whitespace to check the actual content
    message = hey_bob.strip()
    
    # Check for silence (empty or only whitespace)
    if not message:
        return "Fine. Be that way!"
    
    # Check if it's a question (ends with ?)
    is_question = message.endswith('?')
    
    # Check if it's yelling (all uppercase with at least one letter)
    is_yelling = message.isupper() and any(c.isalpha() for c in message)
    
    # Determine response based on conditions
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."