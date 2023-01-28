import requests

from cfc_challenge.domain.cfc_underwriting import (
    get_external_resources,
    Resource,
    get_hyperlinks,
    get_word_frequency_count,
)


class TestGetResourcesAndLinks:
    response = requests.get("https://www.cfcunderwriting.com/")

    def test_get_external_resources(self):
        external_resources = get_external_resources(self.response)
        assert external_resources == [
            Resource(
                source="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700",
                tag="<link "
                'href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700" rel="stylesheet"/>',
            ),
            Resource(
                source="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css",
                tag="<link "
                'href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" '
                'rel="stylesheet"/>',
            ),
            Resource(
                source="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
                tag="<script "
                'crossorigin="anonymous" '
                "integrity="
                '"sha512-+NqPlbbtM1QqiK8ZAo4Yrj2c4lNQoGv8P79DPtKzj++l5jnN39rHA/xsqn8zE9l0uSoxaCdrOgFs6yjyfbBxSg=="'
                ' src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>',
            ),
            Resource(
                source="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.min.js",
                tag="<script "
                'defer="" '
                'src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.min.js">'
                "</script>",
            ),
            Resource(
                source="https://www.google.com/recaptcha/api.js?render=6LemiyEaAAAAAGwb4nR8oX38fxyM36xjIGbwz6d4",
                tag="<script "
                'src="https://www.google.com/recaptcha/api.js?render=6LemiyEaAAAAAGwb4nR8oX38fxyM36xjIGbwz6d4">'
                "</script>",
            ),
        ]

    def test_get_hyperlinks(self):
        hyperlinks = get_hyperlinks(self.response)
        assert hyperlinks == {
            0: "/en-gb/products/class/cyber-insurance/",
            1: "https://www.instagram.com/cfc_underwriting/",
            2: "/en-gb/company/#recognition",
            3: "/en-gb/resources/events/",
            4: "/en-gb/products/industry/media-entertainment/",
            5: "/en-gb/products/industry/professional-services/",
            6: "/en-gb/digital-healthcare-report-2022/",
            7: "/en-gb/products/class/cyber-insurance/cyber-insurance-for-retailers/",
            8: "/en-gb/claims/",
            9: "/en-gb/products/industry/life-science/",
            10: "/en-gb/products/class/excess-umbrella/",
            11: "/en-gb/products/industry/manufacturing/",
            12: "/en-gb/cyber/",
            13: "/en-gb/",
            14: "/en-gb/ransomware-calculator/",
            15: "/en-gb/resources/",
            16: "/en-gb/resources/articles/",
            17: "/en-gb/cyber/response/cyber-reponse-app/",
            18: "/en-gb/resources/news/2020/12/cfc-named-top-insurance-workplace-in-uk/",
            19: "/en-gb/support/europe/",
            20: "/en-gb/resources/guides/the-future-of-healthcare/",
            21: "/en-gb/products/class/kidnap-ransom/",
            22: "/en-gb/product-governance/",
            23: "/en-gb/resources/webinars/",
            24: "/en-gb/emerging-risk/",
            25: "/en-gb/products/class/medical-malpractice/",
            26: "/en-gb/products/industry/ehealth/",
            27: "/en-gb/esg/",
            28: "/locations/switch/?isocode=GB",
            29: "/en-gb/products/industry/fintech/",
            30: "/locations/switch/?isocode=US",
            31: "/en-gb/products/class/cyber-insurance/new-to-cyber-insurance/",
            32: "/en-gb/products/class/intellectual-property/",
            33: "/en-gb/resources/guides/",
            34: "/en-gb/products/class/professional-liability/",
            35: "/en-gb/support/regulatory-information/",
            36: "/en-gb/products/class/property-casualty/",
            37: "/en-gb/products/class/environmental-liability/",
            38: "/en-gb/products/class/cyber-insurance/cyber-insurance-for-manufacturers/",
            39: "/en-gb/resources/case-studies/",
            40: "/en-gb/resources/news/2020/12/cfcs-professional-liability-product-wins-5-star-excellence-award/",
            41: "/en-gb/support/terms-of-use/",
            42: "/en-gb/support/modern-slavery-statement/",
            43: "/en-gb/gender-pay-gap-report/",
            44: "/en-us/resources/news/2021/12/cfc-comes-up-golden-at-insurance-times-awards/",
            45: "/en-gb/support/privacy-policy/",
            46: "/en-gb/products/industry/healthcare/",
            47: "/en-gb/resources/news/2022/05/cfc-s-cyber-threat-analysis-team-wins-customer-care-award/",
            48: "https://www.facebook.com/cfcspecialistinsurance",
            49: "/locations/switch/?isocode=AU",
            50: "/en-gb/products/industry/technology/",
            51: "/en-gb/careers/",
            52: "/en-gb/company/find-an-underwriter/?r=uk&d=executive-committee&q=",
            53: "/en-gb/support/complaints-procedure/",
            54: "/en-gb/products/class/cyber-insurance/cyber-insurance-for-construction/",
            55: "/en-gb/contact/",
            56: "/en-gb/company/",
            57: "https://www.youtube.com/user/CFCUnderwriting",
            58: "/en-gb/why-cfc/",
            59: "/locations/switch/?isocode=CA",
            60: "https://www.linkedin.com/company/cfc-underwriting-ltd",
            61: "/en-gb/sitemap/",
            62: "/en-gb/support/strategic-report/",
            63: "/en-gb/products/industry/financial-institutions/",
            64: "/en-gb/products/class/product-recall/",
            65: "/en-gb/products/class/management-liability/",
            66: "/en-gb/products/class/transaction-liability/",
            67: "/en-gb/products/class/terrorism/",
            68: "/en-gb/products/class/cyber-insurance/cyber-insurance-for-healthcare-providers/",
            69: "/en-gb/resources/news/",
            70: "https://twitter.com/cfcunderwriting",
            71: "/en-gb/products/class/cyber-insurance/cyber-insurance-for-professional-services/",
            72: "/en-gb/platform/",
            73: "/en-gb/cyber/response/",
        }, "/en-gb/support/privacy-policy/"


class GetWordFrequencyCount:
    privacy_policy = requests.get("https://www.cfcunderwriting.com")

    def test_get_word_frequency_count(self):
        word_frequency_count = get_word_frequency_count(self.privacy_policy)

        assert word_frequency_count == {
            "notify": 2,
            "a": 27,
            "claim": 6,
            "contact": 10,
            "careers": 4,
            "uk": 4,
            "US": 2,
            "canada": 2,
            "australia": 2,
            "platform": 1,
            "products": 13,
            "class": 2,
            "cyber": 17,
            "private": 1,
            "enterprise": 1,
            "large": 1,
            "corporate": 1,
            "excess": 3,
            "environmental": 2,
            "liability": 14,
            "pollution": 1,
            "professional": 10,
            "general": 2,
            "and": 45,
            "intellectual": 1,
            "property": 4,
            "infringement": 1,
            "defense": 1,
            "": 14,
            "pursuit": 1,
            "kidnap": 3,
            "ransom": 3,
            "marine": 1,
            "piracy": 1,
            "management": 2,
            "directors": 1,
            "officers": 1,
            "securities": 1,
            "offerings": 1,
            "nonprofits": 1,
            "medical": 3,
            "malpractice": 2,
            "healthcare": 8,
            "professionals": 3,
            "surgeons": 1,
            "dentists": 1,
            "doctors": 1,
            "product": 5,
            "recall": 2,
            "food": 1,
            "beverage": 1,
            "consumer": 1,
            "goods": 1,
            "automotive": 1,
            "engineers": 1,
            "services": 17,
            "recruitment": 2,
            "casualty": 2,
            "terrorism": 3,
            "sabotage": 1,
            "active": 1,
            "assailant": 1,
            "transaction": 2,
            "representation": 1,
            "warranty": 1,
            "insurance": 25,
            "industry": 3,
            "financial": 2,
            "institutions": 2,
            "investment": 1,
            "managers": 1,
            "indemnity": 1,
            "fintech": 3,
            "for": 37,
            "businesses": 1,
            "digital": 1,
            "ehealth": 3,
            "life": 2,
            "science": 2,
            "rd": 1,
            "devices": 1,
            "supplements": 1,
            "manufacturing": 3,
            "policies": 1,
            "manufacturers": 2,
            "media": 4,
            "entertainment": 2,
            "licensing": 1,
            "agreements": 1,
            "technology": 3,
            "companies": 1,
            "social": 1,
            "platforms": 1,
            "all": 2,
            "new": 2,
            "to": 99,
            "made": 3,
            "simple": 1,
            "our": 48,
            "awardwinning": 1,
            "solutions": 1,
            "cfc": 9,
            "response": 2,
            "tools": 1,
            "ransomware": 1,
            "calculator": 1,
            "calculate": 1,
            "the": 57,
            "cost": 1,
            "of": 48,
            "an": 5,
            "attack": 1,
            "app": 2,
            "mobile": 2,
            "industries": 1,
            "providers": 4,
            "retail": 1,
            "retailers": 1,
            "construction": 2,
            "claims": 2,
            "resources": 2,
            "featured": 2,
            "guides": 3,
            "future": 1,
            "knowledge": 1,
            "articles": 2,
            "insights": 1,
            "tips": 1,
            "best": 1,
            "practices": 1,
            "case": 3,
            "studies": 2,
            "real": 1,
            "customer": 3,
            "events": 2,
            "meet": 2,
            "up": 1,
            "inperson": 1,
            "or": 45,
            "online": 4,
            "news": 4,
            "latest": 2,
            "announcements": 2,
            "how": 2,
            "sell": 1,
            "popular": 1,
            "webinars": 2,
            "learn": 2,
            "from": 5,
            "wherever": 1,
            "you": 53,
            "are": 13,
            "company": 5,
            "award": 1,
            "business": 5,
            "names": 2,
            "top": 1,
            "workplace": 1,
            "about": 7,
            "more": 5,
            "team": 3,
            "senior": 1,
            "leadership": 1,
            "awards": 1,
            "recognition": 1,
            "ready": 1,
            "join": 1,
            "responsibility": 1,
            "commitment": 1,
            "esg": 1,
            "get": 2,
            "in": 28,
            "touch": 1,
            "governance": 3,
            "fair": 1,
            "value": 1,
            "assessments": 1,
            "fvas": 1,
            "home": 1,
            "privacy": 7,
            "policy": 6,
            "this": 6,
            "underwriting": 3,
            "we": 36,
            "process": 6,
            "personal": 27,
            "data": 38,
            "customers": 3,
            "brokers": 1,
            "website": 14,
            "visitors": 1,
            "european": 1,
            "union": 1,
            "users": 3,
            "by": 14,
            "clicking": 1,
            "here": 2,
            "will": 10,
            "collect": 7,
            "when": 3,
            "obtain": 1,
            "quote": 1,
            "one": 7,
            "course": 1,
            "providing": 1,
            "with": 14,
            "also": 5,
            "register": 1,
            "us": 21,
            "provide": 7,
            "your": 52,
            "information": 25,
            "through": 4,
            "types": 2,
            "may": 27,
            "include": 3,
            "application": 2,
            "including": 3,
            "addresses": 3,
            "date": 1,
            "birth": 1,
            "other": 5,
            "provided": 3,
            "help": 2,
            "carry": 4,
            "out": 5,
            "obligations": 4,
            "under": 3,
            "any": 15,
            "contract": 7,
            "place": 5,
            "between": 4,
            "relating": 3,
            "make": 9,
            "apps": 1,
            "portals": 1,
            "use": 8,
            "share": 1,
            "third": 5,
            "parties": 2,
            "acting": 1,
            "on": 8,
            "behalf": 1,
            "following": 2,
            "purposes": 10,
            "analyse": 1,
            "needs": 1,
            "administer": 2,
            "assess": 4,
            "adjust": 2,
            "respond": 3,
            "complaint": 4,
            "might": 2,
            "ensure": 2,
            "security": 2,
            "account": 2,
            "preventing": 1,
            "detecting": 1,
            "fraud": 2,
            "abuses": 2,
            "example": 5,
            "requesting": 1,
            "verification": 2,
            "order": 4,
            "reset": 1,
            "password": 1,
            "certain": 4,
            "circumstances": 5,
            "need": 5,
            "sensitive": 2,
            "which": 9,
            "physical": 3,
            "mental": 3,
            "health": 3,
            "condition": 3,
            "members": 2,
            "family": 2,
            "employees": 2,
            "criminal": 2,
            "offence": 2,
            "alleged": 1,
            "committed": 1,
            "only": 3,
            "such": 4,
            "where": 10,
            "have": 11,
            "consented": 3,
            "using": 5,
            "marketing": 3,
            "as": 11,
            "follows": 1,
            "that": 14,
            "request": 7,
            "feel": 1,
            "interest": 2,
            "market": 1,
            "research": 1,
            "ask": 1,
            "feedback": 1,
            "if": 7,
            "at": 3,
            "time": 7,
            "after": 1,
            "wish": 2,
            "stop": 2,
            "these": 6,
            "please": 5,
            "email": 1,
            "optoutcfcunderwritingcom": 1,
            "lawfully": 1,
            "rely": 2,
            "valid": 2,
            "legal": 7,
            "grounds": 2,
            "primary": 1,
            "ground": 1,
            "is": 8,
            "fulfil": 1,
            "take": 2,
            "steps": 1,
            "prior": 1,
            "entering": 1,
            "however": 2,
            "there": 2,
            "be": 7,
            "consent": 6,
            "particular": 2,
            "processing": 9,
            "activities": 1,
            "legitimate": 3,
            "interests": 3,
            "except": 1,
            "fundamental": 1,
            "rights": 4,
            "override": 1,
            "it": 1,
            "within": 2,
            "prevent": 1,
            "detect": 1,
            "compliance": 1,
            "obligation": 1,
            "subject": 3,
            "regulatory": 2,
            "duty": 1,
            "investigate": 1,
            "complaints": 2,
            "against": 2,
            "part": 1,
            "investigation": 1,
            "disclose": 2,
            "compelled": 1,
            "accordance": 3,
            "applicable": 6,
            "law": 9,
            "listed": 1,
            "above": 2,
            "scenarios": 1,
            "disclosure": 2,
            "subsidiaries": 1,
            "branches": 1,
            "associated": 1,
            "offices": 1,
            "outsourced": 2,
            "service": 5,
            "suppliers": 1,
            "facilitate": 1,
            "provision": 1,
            "centre": 1,
            "provider": 2,
            "safe": 1,
            "keeping": 1,
            "webhosting": 1,
            "collected": 1,
            "identity": 3,
            "partners": 1,
            "verify": 1,
            "public": 2,
            "databases": 2,
            "party": 3,
            "consultants": 1,
            "protect": 2,
            "integrity": 1,
            "systems": 1,
            "continuity": 1,
            "reasons": 1,
            "another": 1,
            "entity": 1,
            "temporary": 1,
            "permanent": 1,
            "basis": 1,
            "joint": 1,
            "venture": 1,
            "collaboration": 1,
            "financing": 1,
            "sale": 2,
            "merger": 2,
            "reorganisation": 1,
            "change": 1,
            "form": 2,
            "dissolution": 1,
            "similar": 1,
            "event": 1,
            "permanently": 1,
            "transferred": 2,
            "successor": 1,
            "advisors": 1,
            "who": 1,
            "manage": 1,
            "litigate": 1,
            "authorities": 1,
            "required": 4,
            "do": 5,
            "so": 6,
            "transfer": 1,
            "countries": 1,
            "outside": 1,
            "further": 1,
            "set": 1,
            "throughout": 1,
            "group": 1,
            "located": 1,
            "abroad": 1,
            "adequately": 1,
            "protected": 1,
            "appropriate": 1,
            "technical": 1,
            "organisation": 1,
            "contractual": 1,
            "lawful": 2,
            "means": 1,
            "protection": 5,
            "officer": 2,
            "copy": 1,
            "safeguards": 1,
            "put": 1,
            "previously": 1,
            "been": 1,
            "ours": 1,
            "then": 1,
            "continue": 2,
            "hold": 3,
            "purpose": 1,
            "continuing": 1,
            "connection": 1,
            "duration": 1,
            "reasonable": 1,
            "period": 1,
            "afterwards": 1,
            "keep": 2,
            "anonymised": 1,
            "no": 1,
            "longer": 1,
            "refer": 1,
            "statistical": 1,
            "without": 1,
            "limits": 1,
            "extent": 1,
            "doing": 1,
            "provides": 1,
            "individuals": 2,
            "numerous": 1,
            "right": 7,
            "access": 2,
            "rectify": 2,
            "erase": 1,
            "restrict": 1,
            "transport": 1,
            "object": 2,
            "their": 3,
            "lodge": 1,
            "relevant": 2,
            "authority": 2,
            "they": 3,
            "believe": 1,
            "not": 5,
            "being": 2,
            "processed": 1,
            "sar": 3,
            "controller": 1,
            "permitted": 3,
            "copies": 2,
            "would": 1,
            "like": 1,
            "ie": 1,
            "writing": 1,
            "whose": 1,
            "details": 1,
            "should": 1,
            "clear": 1,
            "submit": 1,
            "proof": 1,
            "fee": 1,
            "rectification": 1,
            "inaccurate": 1,
            "andor": 1,
            "complete": 1,
            "incomplete": 1,
            "withdraw": 3,
            "withdrawal": 1,
            "affect": 1,
            "lawfulness": 1,
            "based": 1,
            "previous": 1,
            "note": 2,
            "able": 1,
            "benefit": 1,
            "features": 1,
            "essential": 1,
            "suggest": 1,
            "questions": 1,
            "relation": 1,
            "supervisory": 1,
            "directly": 1,
            "commissioners": 1,
            "office": 1,
            "united": 1,
            "kingdom": 1,
            "visit": 3,
            "ico": 1,
            "instructions": 1,
            "nonpersonal": 1,
            "site": 4,
            "log": 1,
            "ip": 3,
            "address": 2,
            "unique": 1,
            "identifies": 1,
            "computer": 2,
            "internet": 1,
            "broad": 1,
            "geographic": 1,
            "visitor": 2,
            "optimise": 1,
            "link": 1,
            "personally": 1,
            "identifiable": 1,
            "cookies": 3,
            "small": 1,
            "text": 1,
            "files": 1,
            "placed": 1,
            "websites": 4,
            "widely": 1,
            "used": 2,
            "works": 1,
            "work": 2,
            "efficiently": 1,
            "well": 1,
            "owners": 1,
            "delete": 1,
            "block": 1,
            "but": 1,
            "choose": 1,
            "parts": 2,
            "sections": 1,
            "session": 2,
            "improve": 2,
            "assist": 1,
            "navigation": 1,
            "deliver": 1,
            "better": 1,
            "personalised": 1,
            "cookie": 1,
            "specifically": 1,
            "enable": 1,
            "track": 1,
            "movement": 1,
            "page": 4,
            "dont": 1,
            "asked": 1,
            "same": 1,
            "each": 1,
            "navigate": 1,
            "allow": 1,
            "recognise": 1,
            "changes": 1,
            "review": 1,
            "before": 1,
            "invite": 1,
            "participate": 1,
            "survey": 1,
            "related": 1,
            "participation": 1,
            "optional": 1,
            "offer": 1,
            "surveys": 1,
            "typeform": 1,
            "linked": 1,
            "own": 1,
            "cover": 1,
            "umbrella": 1,
            "why": 1,
            "europe": 1,
            "strategic": 1,
            "report": 2,
            "gender": 1,
            "pay": 1,
            "gap": 1,
            "procedure": 1,
            "modern": 1,
            "slavery": 1,
            "statement": 1,
            "terms": 1,
            "sitemap": 1,
        }
