"""
Unit Tests for Codepipeline class
"""
import json
import pytest
from lambda_sample_events import SampleEvent
from lambda_sample_events.unknown_service_error import UnknownServiceError

JSON_SAMPLES = 'lambda_sample_events/json_samples/'
SERVICES = [
    'codepipeline',
    'sns',
    'cloudformation',
    'ses',
    'scheduled',
    'dynamodb_update',
    'cognito_sync_trigger',
    'kinesis_stream',
    's3_put',
    's3_delete',
    'cloudwatch_logs'
]

def test_invalid_service_name():
    """ Tests invoking with an invalid Service Name """
    with pytest.raises(UnknownServiceError):
        SampleEvent('invalid')

@pytest.mark.parametrize("service_name", SERVICES)
def test_supported_service(service_name):
    """ Tests each supported service for a proper event """
    service = SampleEvent(service_name)
    json_event = json.load(open(JSON_SAMPLES + service_name +'.json'))
    assert service.event == json_event