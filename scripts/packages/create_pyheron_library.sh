#!/usr/bin/env bash

set -e

TMP_DIR=`mktemp -d`
PYHERON_TOPLEVEL_DIR="${TMP_DIR}/pyheron"
UNZIP_DEST="${TMP_DIR}/unzipped"
HERON_DIR=`git rev-parse --show-toplevel`
BUILT_PKG_PATH=${HERON_DIR}/bazel-bin/heron/streamparse/src/python/pyheron_pkg.pex


# directory structure
# pyheron
# |- heron/
# |  |- __init__.py
# |  |- common/src/python/
# |  \_ proto/
# |
# |- pyheron/
# |  |- bolt/
# |  |- component/
# |  |- spout/
# |  |- stream.py
# |  |- topology.py
# |  \_ __init__.py
# |
# |- setup.py
# \_ requirements.txt


# build pyheron_pkg pex file
cd ${HERON_DIR}
bazel build heron/streamparse/src/python:pyheron_pkg
unzip -d $UNZIP_DEST $BUILT_PKG_PATH

# creates a pyheron directory
mkdir -p $PYHERON_TOPLEVEL_DIR
# copis everything under heron to pyheron dir
cp -R ${UNZIP_DEST}/heron ${PYHERON_TOPLEVEL_DIR}
# move streamparse/src/python -> pyheron
mv ${PYHERON_TOPLEVEL_DIR}/heron/streamparse/src/python ${PYHERON_TOPLEVEL_DIR}/pyheron
rm -rf ${PYHERON_TOPLEVEL_DIR}/heron/streamparse


echo "PyHeron toplevel directory: ${PYHERON_TOPLEVEL_DIR}"
tree $PYHERON_TOPLEVEL_DIR