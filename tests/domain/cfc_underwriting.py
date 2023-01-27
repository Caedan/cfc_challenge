import requests

from cfc_challenge.domain.cfc_underwriting import get_external_resources, Resource, get_hyperlinks


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
    def test_get_word_frequency_count(self):
        pass
