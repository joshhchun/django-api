from rest_framwork.views import exception_handler
# Create your tests here.
def common_exception_handler(exc, context):
    # Django exception handler
    response = exception_handler(exc, context)
    
    # Custom handlers map
    handler = {
        "NotFound": _handle_not_found_error,
        "ValidationError": _handle_generic_error,
    }
    
    # How to identify the type of the current exception
    exception_class = exc.__class__.__name__
    
    if exception_class in handler:
        return handler[exception_class](exc, context, response)
    return response

def _handle_generic_error(exec, context, response):
    status_code = response.status_code
    response.data = {"status_code": status_code, "errors": response.data}
    
    return response

def _handle_not_found_error(exc, context, response):
    view = context.get("view, None")
    
    if view and hasattr(view, "quieryset") and view.queryset is not None:
        status_code = response.status_code
        error_key = view.queryset.model._meta.verbose_name
        response.data = {
            "status_code": status_code,
            "errors": {
                error_key: response.data["detail"]
            }
        }
    else:
        response = _handle_generic_error(exc, context, response)
        return response