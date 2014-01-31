import logging
import os


log = logging.getLogger(__name__)


def post_activate_source(args):
    return """
if [ -e "${VIRTUAL_ENV}/.gem" ]; then

    if [ -n "${GEM_HOME+x}" ]; then
        export _OLD_GEM_HOME="$GEM_HOME"
    fi
    export GEM_HOME=$VIRTUAL_ENV

    if [ -n "${GEM_PATH+x}" ]; then
        export _OLD_GEM_PATH="$GEM_PATH"
    fi
    export GEM_PATH=""

    if [ -n "${BUNDLE_HOME+x}" ]; then
        export _OLD_BUNDLE_HOME="$BUNDLE_HOME"
    fi
    export BUNDLE_HOME="$GEM_HOME"

    if [ -n "${BUNDLE_BIN+x}" ]; then
        export _OLD_BUNDLE_BIN="$BUNDLE_BIN"
    fi
    export BUNDLE_BIN="${GEM_HOME}/bin"

fi

"""


def pre_deactivate_source(args):
    return  """
if [ -e "${VIRTUAL_ENV}/.gem" ]; then

    if [ -n "${_OLD_GEM_HOME+x}" ]; then
        GEM_HOME="$_OLD_GEM_HOME"
        export GEM_HOME
        unset _OLD_GEM_HOME
    else
        unset GEM_HOME
    fi

    if [ -n "${_OLD_GEM_PATH+x}" ]; then
        GEM_PATH="$_OLD_GEM_PATH"
        export GEM_PATH
        unset _OLD_GEM_PATH
    else
        unset GEM_PATH
    fi

    if [ -n "${_OLD_BUNDLE_HOME+x}" ]; then
        BUNDLE_HOME="$_OLD_BUNDLE_HOME"
        export BUNDLE_HOME
        unset _OLD_BUNDLE_HOME
    else
        unset BUNDLE_HOME
    fi

    if [ -n "${_OLD_BUNDLE_BIN+x}" ]; then
        BUNDLE_BIN="$_OLD_BUNDLE_BIN"
        export BUNDLE_BIN
        unset _OLD_BUNDLE_BIN
    else
        unset BUNDLE_BIN
    fi

fi

"""
