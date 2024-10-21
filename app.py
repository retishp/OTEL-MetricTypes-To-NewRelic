from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.metrics import CallbackOptions, Observation
from typing import Iterable
import time
import random

def createCounter(meter):    
 my_counter = meter.create_counter("mycounter.increments")

 my_counter.add(3)
 time.sleep(10)

 my_counter.add(5)
 time.sleep(10)

 my_counter.add(10)
 time.sleep(10)

def createUpDownCounter(meter):    
 my_updown_counter = meter.create_up_down_counter("myupdowncounter")

 my_updown_counter.add(3)
 time.sleep(10)

 my_updown_counter.add(-1)
 time.sleep(10)

 my_updown_counter.add(10)
 time.sleep(10)
 
def createHistogram(meter):
 # Create the histogram instrument
 my_histogram = meter.create_histogram("myhistogram")

 # Record histogram values. This will create a histogram with 3 values/count.
 for i in range(1, 10):
    latency  = random.randint(1, 1000)
    my_histogram.record(latency, attributes={"attr1": "value1"})

 time.sleep(10)

# Register a call back function
def pf_callback(options: CallbackOptions) -> Iterable[Observation]:
    # Once registered the call back function is automatically invoked
    # for every harvest cycle
    return [Observation(random.randint(1,100), {"pid": 1}),
            Observation(random.randint(1,100), {"pid": 2}),
            Observation(random.randint(1,100), {"pid": 3})]

# Create an Observable counter (asynchronous)
def createObservableCounter(meter):
 #Once created the callback function will be automatically invoked every harvest cycle (in this case, 5 seconds)
 meter.create_observable_counter(name="myobservablecounter", description="process page faults", callbacks = [pf_callback])
 time.sleep(20)
 
# Main function starts here
metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter(),export_interval_millis=5000)
provider = MeterProvider(metric_readers=[metric_reader])

# Sets the global default meter provider
metrics.set_meter_provider(provider)

# Creates a meter from the global meter provider
meter = metrics.get_meter("my.meter.name")

createCounter(meter)
createUpDownCounter(meter)
createHistogram(meter)
createObservableCounter(meter)







