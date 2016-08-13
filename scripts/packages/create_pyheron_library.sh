#!/usr/bin/env bash

set -e

TMP_DIR=`mktemp -d`
PYHERON_TOPLEVEL_DIR="${TMP_DIR}/pyheron"
echo "PyHeron toplevel directory: ${PYHERON_TOPLEVEL_DIR}"
HERON_DIR=`git rev-parse --show-toplevel`

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


# creates a directory
mkdir -p $PYHERON_TOPLEVEL_DIR

# heron/common and corresponding __init__.py
mkdir -p ${PYHERON_TOPLEVEL_DIR}/heron/common/src/python


# copy directory heron/streamparse/src/python to pyheron/pyheron
cp -R ${HERON_DIR}/heron/streamparse/src/python ${PYHERON_TOPLEVEL_DIR}/pyheron