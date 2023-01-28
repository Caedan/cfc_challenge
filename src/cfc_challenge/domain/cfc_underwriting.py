import re
from dataclasses import dataclass, asdict

from bs4 import BeautifulSoup, Comment, ResultSet
from requests import Response


@dataclass
class Resource:
    source: str
    tag: str

    def dict(self) -> dict[str, str]:
        return {k: str(v) for k, v in asdict(self).items()}


def get_external_resources(response: Response) -> list[Resource]:
    """
    Extracts all external resources
    """
    external_resources = []
    soup = BeautifulSoup(response.content, "lxml")
    resource_tags = soup.find_all(["link", "script", "noscript"])

    for tag in resource_tags:
        if tag.name == "link":
            if tag["href"].startswith("https") and "cfcunderwriting" not in tag["href"]:
                resource = Resource(source=tag["href"], tag=str(tag))
                external_resources.append(resource)
        else:
            script_source = tag.get("src")
            if script_source:
                if script_source.startswith("https") and "cfcunderwriting" not in script_source:
                    resource = Resource(source=script_source, tag=str(tag))
                    external_resources.append(resource)

    return external_resources


def get_hyperlinks(response: Response) -> tuple[dict[str, str], str]:
    """
    Extracts all hyperlinks and returns a tuple
    containing an enumerated dict of all links and the link to Privacy Policy
    """
    soup = BeautifulSoup(response.content, "lxml")
    anchor_tags = soup.find_all("a", href=True)
    links = set()
    privacy_policy = ""

    for tag in anchor_tags:
        if tag.name == "a" and (tag["href"].startswith("/") or tag["href"].startswith("https")):
            link = tag["href"]
            # The links set is primarily helping to deduplicate links
            links.add(link)
            if "privacy-policy" in link:
                privacy_policy = link

    return {str(k): v for k, v in zip(range(len(links)), links)}, privacy_policy


def get_word_frequency_count(response: Response) -> dict[str, int]:
    """
    Gets a case insensitive count of the word frequency inside the response
    """
    words: dict[str, int] = {}
    soup = BeautifulSoup(response.content, "lxml")

    # Remove text that is hidden from view
    soup.find("div", {"class": "popup-holder"}).decompose()
    soup.find("div", {"class": "newsletter"}).decompose()

    text = soup.body.findAll(text=True)
    visible_texts = list(filter(_tag_visible, text))

    for text in visible_texts:
        for word in text.split():
            regex = re.compile("[^a-zA-Z]")
            clean_word = regex.sub("", word)

            if clean_word == "":
                continue

            if clean_word != "US":
                clean_word = clean_word.lower()

            if not words.get(clean_word):
                words[clean_word] = 1
            else:
                words[clean_word] += 1

    return words


def _tag_visible(element: ResultSet) -> bool:
    if element.parent.name in ["style", "script", "head", "title", "meta", "[document]"]:
        return False
    if isinstance(element, Comment):
        return False
    if element in ["\n", "↑", " ", "\xa0"] or any(re.findall("[0-9]+", str(element))):
        return False

    return True
