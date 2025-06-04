'''
Error Format:

{'success': False,
 'errors': 
          [
            {
               "error": "auth-0001",
               "message": "Invalid credentials",
               "detail": "",
               "associated_field": "",
            },
            {
               "error": "auth-0002",
               "message": "User not authenticated",
               "detail": "",
               "associated_field": "",
            }
          ]
}
'''
import json

error_codes = {
                'auth-0001': {
                                'message': 'Invalid Credentials',
                                'detail': '',
                                'associated_field': '',
                             },
                'auth-0002': {
                                'message': 'User not authenticated',
                                'detail': '',
                                'associated_field': '',
                             },
                'payload-001': {
                                'message': 'Unprocessable Entity',
                                'detail': '',
                                'associated_field': '',
                              },
                'notfound-001': {
                                'message': 'Page Not Found',
                                'detail': '',
                                'associated_field': '',
                              },
                'modelvalidation-001': {
                                'message': 'Model Validation Error',
                                'detail': '',
                                'associated_field': '',
                              },
                'inputvalidation-001': {
                                'message': 'Model Validation Error',
                                'detail': '',
                                'associated_field': '',
                              },                              
                              
                             
              }


class ErrorMessage:

      def __init__(self):
          self.error = {}
          self.errors = []          
          self.error['errors'] = self.errors

      def add(self, code):
          error_item = {}
          error_item["error"] = code
          error_item["message"] = error_codes[code]['message']
          error_item["detail"] = error_codes[code]['detail']
          self.error['success'] = False          
          self.errors.append(error_item)
                    
      def to_dict(self):
        return self.error


class LoginError(Exception):
    pass


# This should use inheritance from ErrorMessage
class ModelValidationError(Exception):

      def __init__(self, msg=""):
          self.msg=msg
          self.error = {}
          self.errors = []          
          self.error['errors'] = self.errors
          self.error_codes = {
                'model-0001': {
                                'message': 'Integrity Error', # Duplicated id????
                                'detail': ''
                             },
                'model-0002': {
                                'message': 'Blank or Null Field',
                                'detail': ''
                             },
                'model-0003': {
                                'message': 'Input exceds the maximum lenth for this field',
                                'detail': ''
                             },
                'model-0004': {
                                'message': 'There is another entry with the same value in the database',
                                'detail': ''
                             },
                'model-0005': {
                                'message': 'Invalid Field',
                                'detail': ''
                             },                           
              }
          self.django_codes = {
		'blank': {
		                'message': 'Blank or Null Field',
		                'code': 'model-0002'
		             },
		'max_length': {
		                'message': 'Input exceds the maximum lenth for this field',
		                'code': 'model-0003'
		             }, 
		'unique': {
		                'message': 'There is another entry with the same value in the database',
		                'code': 'model-0004'
		             }, 
		'invalid': {
		                'message': 'Invalid Field',
		                'code': 'model-0005'
		             },                                
	      }

      def add(self, code, field_name=""):
          error_item = {}
          error_item["error"] = code
          error_item["message"] = self.error_codes[code]['message']
          error_item["detail"] = self.error_codes[code]['detail']
          error_item['associated_field'] = field_name
          self.error['success'] = False
          self.errors.append(error_item)

      def get_django_code(self, code):
          return self.django_codes[code]['code']

      def add_from_django(self, django_error):
          # Validate ValidationError
          # if type(django_error) == ValidationError
          # if django_error has error_dict and error_dict is dict
          # Iterate
          for key, value in django_error.error_dict.items():
            field_name = key
            for code in value:
                model_validation_error_code = self.get_django_code(code.code)
                self.add(model_validation_error_code, field_name)

      def to_dict(self):
        return self.error

# This should use inheritance from ErrorMessage
class InputValidationError(Exception):

      def __init__(self, msg=""):
          self.msg=msg
          self.error = {}
          self.errors = []          
          self.error['errors'] = self.errors
          self.error_codes = {
                'form-0001': {
                                'message': 'Password and confirmation dont match',
                                'detail': ''
                             },
                'form-0002': {
                                'message': 'Invalid E-mail format',
                                'detail': ''
                             },                             
              }

      def add(self, code):
          error_item = {}
          error_item["error"] = code
          error_item["message"] = self.error_codes[code]['message']
          error_item["detail"] = self.error_codes[code]['detail']
          self.error['success'] = False          
          self.errors.append(error_item)
                    
      def to_dict(self):
        return self.error



    

