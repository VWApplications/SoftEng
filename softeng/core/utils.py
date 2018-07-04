def create_uri(text):
    """
    Clean text to URI format.
    """

    # Capitalize
    text = text.title()

    # Replace space to underline
    uri = text.replace(" ", "_")

    return uri
