#!/usr/bin/env bash
# Batch-run classifier on files in uploaded_images/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PYTHON="${PYTHON:-python3}"
ARCH="${1:-vgg}"
DATA_DIR="${SCRIPT_DIR}"
UPLOADED_DIR="${DATA_DIR}/uploaded_images"
DOGFILE="${DATA_DIR}/dognames.txt"
OUT_CSV="${DATA_DIR}/uploaded_results.csv"

echo "Running batch classifier"
echo "Python: ${PYTHON}"
echo "Arch: ${ARCH}"
echo "Uploaded dir: ${UPLOADED_DIR}"
echo "Output CSV: ${OUT_CSV}"

${PYTHON} "${DATA_DIR}/batch_runner.py" --dir "${UPLOADED_DIR}" --arch "${ARCH}" --dogfile "${DOGFILE}" --out "${OUT_CSV}"

rc=$?
if [ $rc -ne 0 ]; then
  echo "batch runner failed with exit code $rc"
  exit $rc
fi

echo "Done. Results: ${OUT_CSV}"
