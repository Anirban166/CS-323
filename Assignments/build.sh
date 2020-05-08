if [[ -z "$1" ]]; then
  PYTHON_BIN_PATH=python
else
  if [[ "$1" == --python_bin_path ]]; then
    shift
    PYTHON_BIN_PATH=$1
  else
    printf "Unrecognized argument $1"
    exit 1
  fi
fi

set -u -x

cp -f tensorflow_metadata/proto/v0/schema_pb2.py \
  ${BUILD_WORKSPACE_DIRECTORY}/tensorflow_metadata/proto/v0

cp -f tensorflow_metadata/proto/v0/path_pb2.py \
  ${BUILD_WORKSPACE_DIRECTORY}/tensorflow_metadata/proto/v0

cp -f tensorflow_metadata/proto/v0/anomalies_pb2.py \
  ${BUILD_WORKSPACE_DIRECTORY}/tensorflow_metadata/proto/v0

cp -f tensorflow_metadata/proto/v0/statistics_pb2.py \
  ${BUILD_WORKSPACE_DIRECTORY}/tensorflow_metadata/proto/v0

cd ${BUILD_WORKSPACE_DIRECTORY}

${PYTHON_BIN_PATH} setup.py bdist_wheel --universal

cd -
