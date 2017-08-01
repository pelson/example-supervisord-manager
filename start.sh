#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


export SUPERVISOR_CONFIG_REPO_LOCN=${DIR}

cd ${SUPERVISOR_CONFIG_REPO_LOCN}
supervisord -c ${SUPERVISOR_CONFIG_REPO_LOCN}/supervisord.conf
