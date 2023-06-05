# ginkgo-webhook

## What is it

A project to contain the POC webhooks used for the Gingko Sapio Demo

### What is included

`server.py` is the entry point for the python server that will host the webhook. It will configure the server and then
start it

`webhook/hello_world.py` is a bare-bones webhook that you can use to verify that your Sapio System is successfully
communicating with your webhook

## Requirements

This project depends on [sapiopylib](https://pypi.org/project/sapiopylib/)

For the `ROOT` `/` path to load it depends on the [markdown](https://pypi.org/project/Markdown/) package being installed
to generate the HTML


## Building

Included with this project is a requirements.txt file that allows for you to quickly install the dependencies
through `pip`
> `pip install -r requirements.txt`

## Running

> `python -u server.py`

The `-u` unbuffered parameter is used so that the stdout/stderr console output isn't buffered, so it doesn't need to be
flushed before being shown

## Further Reading

In addition to this project we have interactive python tutorials that you can use to learn more about the Sapio REST API
and webhooks on GitHub at [Sapio Python Tutorials](https://github.com/sapiosciences/sapio-py-tutorials/)


## About Us

Sapio is at the forefront of the Digital Lab with its science-aware platform for managing all your life science data
with its integrated Electronic Lab Notebook, LIMS Software and Scientific Data Management System.

Visit us at https://www.sapiosciences.com/