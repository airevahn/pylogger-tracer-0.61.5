# pylogger-tracer-0.61.5

this repo aims to prove that using python ddtrace v0.61.5, the trace_id is injected to the logs without having to configure the logging library's output format.
it contains a sample python web app using flask, that generates error log when there's a request at port 8081.
the kubernetes yaml file is also available in this repo.
