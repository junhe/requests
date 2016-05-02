# -*- coding: utf-8 -*-

"""
requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.

"""
HOOKS = ['response']

def default_hooks():
    return dict((event, []) for event in HOOKS)

# TODO: response is the only one

def dispatch_hook(key, hooks, hook_data, **kwargs):
    """Dispatches a hook dictionary on a given piece of data."""
    # This function calls the function(s) (callable objects) stored in
    # hooks for key, and return the valid return value of the last call

    # Hmm, never used this. It is equivelant to
    # hooks if hooks else dict(). return hooks it is not empty,
    # otherwise return dict()
    hooks = hooks or dict()
    value = hooks.get(key)

    # we found key in hooks and hook value is a single item (so callable)
    # we put the value to a list
    if value:
        # handle the case that value is a single item
        if hasattr(value, '__call__'):
            value = [value]

        for hook in value:
            # call the hook with hook data and arguments
            _hook_data = hook(hook_data, **kwargs)
            if _hook_data is not None:
                # we might return this 'hook_data'
                hook_data = _hook_data
    return hook_data

