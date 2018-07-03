from django.template.defaultfilters import slugify


class Subtopic(object):
    """
    Create a subtopic
    """

    def __init__(self, uri, title, topic, description=None):
        """
        Constructor
        """

        self.uri = uri
        self.title = title
        self.slug = slugify(title)
        self.description = description
        self.topic = slugify(topic)
