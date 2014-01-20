import logging
import os


log = logging.getLogger(__name__)

def post_activate_source(args):
    return """
#patch to wrap gems inside the virtual env

if [ -n "${GEM_HOME+x}" ]; then
    export _OLD_GEM_HOME="$GEM_HOME"
fi
export GEM_HOME=$VIRTUAL_ENV

if [ -n "${GEM_PATH+1}" ]; then
    export _OLD_GEM_PATH="$GEM_PATH"
fi
export GEM_PATH=""

"""



def pre_deactivate_source(args):
    return  """
#restore the value before entering the venv

if [ -n "${_OLD_GEM_HOME+1}" ]; then
    GEM_HOME="$_OLD_GEM_HOME"
    export GEM_HOME
    unset _OLD_GEM_HOME
else
    unset GEM_HOME
fi

if [ -n "${_OLD_GEM_PATH+1}" ]; then
    GEM_PATH="$_OLD_GEM_PATH"
    export GEM_PATH
    unset _OLD_GEM_PATH
else
    unset GEM_PATH
fi

"""
