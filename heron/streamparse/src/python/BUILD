package(default_visibility = ["//visibility:public"])

load("/tools/rules/pex_rules", "pex_library", "pex_binary")

pex_library(
  name = "pyheron_lib",
  srcs = glob(["**/*.py"]),
  deps = [
    "//heron/common/src/python:common",
    "//heron/proto:proto-py",
  ],
  reqs = ['colorlog==2.6.1', 'pyyaml==3.10'],
)

pex_binary(
  name = "pyheron_pkg",
  srcs = glob(["**/*.py"]),
  deps = [
    "//heron/common/src/python:pyheron_common_pkg",
    "//heron/proto:proto-py",
  ]
)