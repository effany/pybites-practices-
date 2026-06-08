import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


@pytest.fixture
def service_ranges():
    return [
        ServiceIPRange(
            service='AMAZON',
            region='ap-northeast-2',
            cidr=IPv4Network('3.5.140.0/22'),
        ),
        ServiceIPRange(
            service='S3',
            region='us-east-1',
            cidr=IPv4Network('54.231.0.0/17'),
        ),
    ]


def test_parse_ipv4_service_ranges(json_file):
    ranges = parse_ipv4_service_ranges(json_file)
    assert ranges
    assert all(isinstance(r, ServiceIPRange) for r in ranges)
# def test_parse_ipv4_service_ranges(ranges):
#     assert parse_ipv4_service_ranges(Path("ip-ranges.json")) == ranges

def test_invalid_ip():
    with pytest.raises(ValueError):
        get_aws_service_range('1000.200.300.400.700', [])

def test_get_aws_service_range(service_ranges):
    expected = [
        ServiceIPRange(service='AMAZON', region='ap-northeast-2',
                       cidr=IPv4Network('3.5.140.0/22')),
    ]
    assert get_aws_service_range('3.5.140.1', service_ranges) == expected

def test_get_aws_service_range_no_match(service_ranges):
    assert get_aws_service_range('10.0.0.1', service_ranges) == []