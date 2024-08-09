from functools import wraps

from flask import request, abort


def validate_request_with_factory(request_class: object, arg: str, method: str = 'POST'):
    """validate request by a dto validator"""

    def decorator(f):
        """kind of decorator function

        :param f: next function
        """

        @wraps(f)
        def decorated_function(*args, **kwargs):
            """main function itself"""

            data = {}

            data.update(request.view_args)
            data.update(request.args)

            if method == 'GET':
                data.update(request.args)

            if method == 'POST' or method == 'PUT' or method == 'DELETE':
                data.update(request.get_json())

            try:
                kwargs[arg] = request_class.generate(**data)
            except Exception as e_info:
                reason = str(e_info)[str(e_info).find('__init__()') + 10:]
                abort(406, reason)
            return f(*args, **kwargs)

        return decorated_function

    return decorator
