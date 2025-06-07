from ninja import NinjaAPI
from timehack_app.api import router
from timehack_app.utils.errors import ErrorMessage, LoginError, ModelValidationError, InputValidationError, ModelNotFoundError
from ninja.errors import AuthenticationError, ValidationError
from django.http import Http404

api = NinjaAPI(csrf=True)
api.add_router("", router)

@api.exception_handler(AuthenticationError)
def authentication_errors(request, exc):
    error_message = ErrorMessage()
    error_message.add('auth-0002')
    return api.create_response(
        request,
        error_message.to_dict(),
        status=401
    )
    
@api.exception_handler(ValidationError)
def validation_errors(request, exc):
    error_message = ErrorMessage()
    error_message.add('payload-001')
    return api.create_response(
        request,
        error_message.to_dict(),
        status=422,
    )
    
@api.exception_handler(Http404)
def not_found_errors(request, exc):
    error_message = ErrorMessage()
    error_message.add('notfound-001')
    return api.create_response(
        request,
        error_message.to_dict(),
        status=404,
    )

@api.exception_handler(ModelNotFoundError)
def not_found_errors(request, exc):
    error_message = ErrorMessage()
    error_message.add('notfound-001')
    return api.create_response(
        request,
        error_message.to_dict(),
        status=404,
    )

@api.exception_handler(LoginError)
def login_error(request, exc):
    error_message = ErrorMessage()
    error_message.add('auth-0001')
    return api.create_response(
        request,
        error_message.to_dict(),
        status=403,
    )

@api.exception_handler(ModelValidationError)
def model_validation_error(request, exc):
   # error_message = ErrorMessage()
   # error_message.add('modelvalidation-001')
    return api.create_response(
        request,
        exc.to_dict(),
        status=422,
    )

@api.exception_handler(InputValidationError)
def input_validation_error(request, exc):
    #error_message = ErrorMessage()
   # error_message.add('inputvalidation-001')
    return api.create_response(
        request,
        exc.to_dict(),
        status=422,
    )

