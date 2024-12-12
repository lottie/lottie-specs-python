import json
from importlib.resources import files


def load_specs():
    with open(files("lottie_specs.data").joinpath("lottie.schema.json")) as fp:
        return json.load(fp)
