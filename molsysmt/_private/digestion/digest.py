import functools
import inspect
from . import *

# The following dictionary maps the name of an argument
# to a digestion function. To add a new argument, create a digestion
# function and then put it in this dictionary.

args_dict = {
    "box": digest_box,
    "comparison": digest_comparison,
    "coordinates": digest_coordinates,
    "element": digest_element,
    "engine": digest_engine,
    "form": digest_form,
    "indices": digest_indices,
    "item": digest_item,
    "molecular_system": digest_single_molecular_system,
    "molecular_systems": digest_multiple_molecular_systems,
    "output": digest_output,
    "syntaxis": digest_syntaxis,
    "selection": digest_selection,
    "selections": digest_multiple_selections,
    "step": digest_step,
    "time": digest_time,
    "structure_indices": digest_indices,
    "to_form": digest_form,
}


def digest(check_args=True, check_kwargs=False):
    """ Decorator to digest the input arguments of a function, with
        the option to disable argument checking.

        When a function decorated with this decorator is called, its
        arguments will be checked and modified if necessary. If one
        of the arguments doesn't fill the requirements a corresponding
        error will be raised.

        The decorator uses the dictionary defined above which maps the
        name of an argument to a digestion function.


        Parameters
        ----------
        check_args: bool, default=True
            If true will digest all non keyword arguments passed to the
            decorated function.

        check_kwargs: bool, default=False
            If true will check all keyword arguments passed to the
            decorated function. If the function doesn't accept kwargs
            this won't have affect.
    """

    def decorator(func):
        # Use functools to preserve the metadata of the decorated function.
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_digested = []
            element_arg = ""
            if check_args:
                # When we call a function and specify the name of
                # the parameters, args get mapped to kwargs.
                # For example if we have a function with the following
                # signature foo(arg) and we call it in this way:
                # foo(arg=10), arg will appear as a keyword argument here.
                args_name = inspect.getfullargspec(func)[0]
                for ii, argument_name in enumerate(args_name):
                    try:
                        digested_value = args_dict[argument_name](args[ii])
                    except IndexError:
                        # Remove the argument from the dictionary, so it doesn't get
                        # repeated
                        digested_value = args_dict[argument_name](kwargs.pop(argument_name))
                    except KeyError:
                        digested_value = args[ii]

                    args_digested.append(digested_value)

                    if argument_name == "element":
                        element_arg = digested_value

            if check_kwargs and kwargs and element_arg:
                # TODO: We should change digest_argument function name cause it's confusing
                # The function get is the only one that uses kwargs (I think). So we will call that
                # function here.
                for argument_name, argument_value in kwargs.items():
                    kwargs[argument_name] = digest_argument(argument_name, element_arg)

            if check_args:
                return func(*args_digested, **kwargs)

            return func(*args, **kwargs)

        return wrapper

    return decorator