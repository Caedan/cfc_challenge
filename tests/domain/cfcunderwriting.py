import requests

from cfc_challenge.domain.cfc_underwriting import get_external_resources, Resource


class TestGetExternalResources:
    response = requests.get("https://www.cfcunderwriting.com/")

    def test_get_external_resources(self):
        external_resources = get_external_resources(self.response)
        assert external_resources == [
            Resource(
                source="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700",
                tag='<link '
                    'href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700" rel="stylesheet"/>',
            ),
            Resource(
                source="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css",
                tag='<link '
                    'href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" '
                    'rel="stylesheet"/>',
            ),
            Resource(
                source="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
                tag='<script '
                    'crossorigin="anonymous" '
                    'integrity='
                    '"sha512-+NqPlbbtM1QqiK8ZAo4Yrj2c4lNQoGv8P79DPtKzj++l5jnN39rHA/xsqn8zE9l0uSoxaCdrOgFs6yjyfbBxSg=="'
                    ' src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>',
            ),
            Resource(
                source="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.min.js",
                tag='<script '
                    'defer="" '
                    'src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.min.js">'
                    '</script>',
            ),
            Resource(
                source="https://www.google.com/recaptcha/api.js?render=6LemiyEaAAAAAGwb4nR8oX38fxyM36xjIGbwz6d4",
                tag='<script '
                    'src="https://www.google.com/recaptcha/api.js?render=6LemiyEaAAAAAGwb4nR8oX38fxyM36xjIGbwz6d4">'
                    '</script>',
            ),
        ]
