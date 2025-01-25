#!/bin/bash
echo "$@"
SCRIPTDIR=$(readlink -f "$(dirname "$0")")
echo "Script directory: $SCRIPTDIR"
pushd "${SCRIPTDIR}" || exit
echo "now in scriptdir"
if [ ! -e ".venv" ]
then
	python3 -m venv .venv
fi

source .venv/bin/activate
pip3 install -r requirements.txt &> /dev/null
python3 "$SCRIPTDIR"/server.py &
# echo "Server PID: $!"
echo $! > pid
popd || exit 0