#!/bin/bash

pip install -U pip setuptools wheel
pip install -U spacy

while getopts ":s:" opt; do
  case $opt in
    s)
      size=$OPTARG
      model="es_core_news_${size}"
      python -m spacy download "$model"
      ;;
    \?)
      echo "INVALID OPTION: -$OPTARG" >&2
      ;;
  esac
done