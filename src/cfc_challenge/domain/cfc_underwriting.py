from requests import Response


def get_external_resources(response: Response) -> None:
    """ Extracts all external resources """
    pass


def get_hyperlinks(response: Response) -> str:
    """ Extracts all hyperlinks and returns link to Privacy Policy """
    pass


def get_word_frequency_count(response: Response) -> dict[str, int]:
    """ Gets a case insensitive count of the word frequency inside the reponse """
    pass
