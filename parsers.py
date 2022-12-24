from dateutil import parser


def noop_parser(text):
    return text


def parse_int(text):
    return int(text.strip().replace('-', ''))


def parse_date(text):
    try:
        date = parser.parse(text)
    except:
        return None
    return date


def strip(text):
    return text.strip()
