Pre-Requisites:
Python - https://www.python.org/downloads/
A New Relic account - https://one.newrelic.com
A New Relic license key - https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#license-key

Steps:
Install these three dependencies:
    pip install opentelemetry-api
    pip install opentelemetry-sdk
    pip install opentelemetry-exporter-otlp-proto-http

Add the following environment variables:
    export OTEL_SERVICE_NAME=MyPythonService
    export OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.nr-data.net
    export OTEL_EXPORTER_OTLP_HEADERS=api-key=<New Relic Ingest License Key>
    export OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT=4095
    export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
    export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf 
    export OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
    export OTEL_RESOURCE_ATTRIBUTES=service.instance.id=123

Using Terminal, create a python virtual environment
    python3 -m venv environment

Activate the virtual environment
    source environment/bin/Activate

Install the required packages
     pip install -r requirements.txt

Run the python script
    python3 app.py
