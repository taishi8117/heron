#!/usr/bin/env bash

set -e

TMP_DIR=`mktemp -d`
PYHERON_TOPLEVEL_DIR="${TMP_DIR}/pyheron"
echo "PyHeron toplevel directory: ${PYHERON_TOPLEVEL_DIR}"
HERON_DIR=`git rev-parse --show-toplevel`

cd ${HERON_DIR}

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

################################### heron/common ###################################################
mkdir -p ${PYHERON_TOPLEVEL_DIR}/heron/common/src

# recursively create __init__.py
for DIR in heron heron/common heron/common/src
do
  touch ${PYHERON_TOPLEVEL_DIR}/${DIR}/__init__.py
done

# copy dir from heron/common/src/python
cp -R ${HERON_DIR}/heron/common/src/python ${PYHERON_TOPLEVEL_DIR}/heron/common/src/python

#################################### heron/proto ###################################################

############################## heron/streamparse -> pyheron ########################################

# copy directory heron/streamparse/src/python to pyheron/pyheron
cp -R ${HERON_DIR}/heron/streamparse/src/python ${PYHERON_TOPLEVEL_DIR}/pyheron

tree $PYHERON_TOPLEVEL_DIR