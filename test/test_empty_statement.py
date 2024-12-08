
from ..parser import Parser
import pytest


@pytest.fixture
def parser():
    return Parser()

def test_block(parser):

    program = ''';'''

    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "EmptyStatement",
        }]
    }
