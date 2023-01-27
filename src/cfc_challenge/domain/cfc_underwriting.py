from dataclasses import dataclass, asdict

from bs4 import BeautifulSoup
from requests import Response


@dataclass
class Resource:
    source: str
    tag: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}


def get_external_resources(response: Response) -> list[Resource]:
    """Extracts all external resources"""
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


def get_hyperlinks(response: Response) -> dict[str, str]:
    """Extracts all hyperlinks and returns link to Privacy Policy"""
    pass


def get_word_frequency_count(response: Response) -> dict[str, int]:
    """Gets a case insensitive count of the word frequency inside the response"""
    pass
