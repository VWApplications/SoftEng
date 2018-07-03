def create_uri(self, title):
    """
    Clean title to URI format.
    """

    # Capitalize
    title = title.title()

    # Replace space to underline
    uri = title.replace(" ", "_")

    return uri
