#!/bin/bash
export PYTHONPATH=.

pytest --color=yes --junitxml=results.xml | tee test-results.txt