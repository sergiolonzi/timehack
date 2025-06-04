'''
'''
from typing import Dict, List

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from ninja import Router
from ninja.security import django_auth

from .models import ListOfTasks, SubTask, Task
from .schemas import (ListOfTasksIn, ListOfTasksOut, LoginSchemaIn, SubTaskIn,
                      SubTaskOut, TaskIn, TaskOut, UserSchemaIn, UserSchemaOut,
                      UserUpdateSchemaIn)
from .utils.validators import validate_email
from .utils.errors import ErrorMessage, LoginError, InputValidationError, ModelValidationError

router = Router()

#######################################
# Auth
#######################################
@router.post("/csrf")
@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request):
    return HttpResponse()


@router.post("/login", response=UserSchemaOut)
def login_endpoint(request, payload: LoginSchemaIn):
    username = payload.username
    password = payload.password
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return 200, user
    raise LoginError()


@router.get("/user-info", response=UserSchemaOut, auth=django_auth)
def get_user_info_endpoint(request):
    user = request.auth
    return 200, user


@router.post("/logout", response=None, auth=django_auth)
def logout_endpoint(request):
    logout(request)
    return 200


@router.post("/is-login", response=Dict, auth=django_auth)
def is_login_endpoint(request):
    return 200, {'is_login': True}


@router.post("/register", response=UserSchemaOut)
def create_user_endpoint(request, payload: UserSchemaIn):
    # Schema:
    input_validation_error = InputValidationError()
    username = payload.username
    email = payload.email
    password = payload.password
    password_confirm = payload.password_confirm

    if password != password_confirm:
        input_validation_error.add(code='form-0001')

    if not validate_email(email):
        input_validation_error.add(code='form-0002')

    if input_validation_error.errors:
        raise input_validation_error

    # Model:
    try:
        user = User()
        user.username=username
        user.email=email
        user.set_password(password)
        user.full_clean()
        user.save()
        return 200, user
    except IntegrityError:
        model_validation_error = ModelValidationError()
        model_validation_error.add(code='model-0001')
        raise model_validation_error
    except ValidationError as error:
        model_validation_error = ModelValidationError()
        model_validation_error.add_from_django(error)               
        raise model_validation_error

@router.put("/user/", response=UserSchemaOut, auth=django_auth)
def update_user_endpoint(request, payload: UserUpdateSchemaIn):
    input_validation_error = InputValidationError()
    user = request.auth
    email = payload.email
    password = payload.password
    password_confirm = payload.password_confirm

    if password != password_confirm:
        input_validation_error.add(code='form-0001')

    if validate_email(email):
        input_validation_error.add(code='form-0002')

    if input_validation_error.errors:
        raise input_validation_error

    # Validate Model:
    try:
        if email:
            user.email = email
        if password:
            user.set_password(password)
        user.save()
        login(request, user)
        return 201, user
    except IntegrityError:
        model_validation_error = ModelValidationError()
        model_validation_error.add(code='model-0001')
        raise model_validation_error
    except ValidationError as error:
        model_validation_error = ModelValidationError()
        model_validation_error.add_from_django(django_error=error)               
        raise model_validation_error


@router.get("/user/", response=UserSchemaOut, auth=django_auth)
def get_user_endpoint(request):
    user = request.auth
    return user


@router.delete("/user/", response=Dict, auth=django_auth)
def delete_user_endpoint(request):
    user = request.auth
    user.delete()
    return 201, {"success": True, 'Message': 'User deleted'}

#######################################
# Tasks
#######################################
# **************************************
# ** ListOfTasks
# **************************************


@router.post("/list-of-tasks", response=List[ListOfTasksOut], auth=django_auth)
def create_list_of_tasks_endpoint(request, payload: ListOfTasksIn):
    user = request.auth
    list_of_tasks = ListOfTasks()
    list_of_tasks.user = user
    list_of_tasks.name = payload.name
    list_of_tasks.description = payload.description

    try:
        list_of_tasks.save()
        lists_of_tags = ListOfTasks.objects.filter(user=user)
        return 200, lists_of_tags
    except IntegrityError:
        model_validation_error = ModelValidationError()
        model_validation_error.add(code='model-0001')
        raise model_validation_error
    except ValidationError as error:
        model_validation_error = ModelValidationError()
        model_validation_error.add_from_django(django_error=error)               
        raise model_validation_error


@router.get("/list-of-tasks/{list_of_tasks_id}", response=ListOfTasksOut, auth=django_auth)
def get_list_of_tasks_endpoint(request, list_of_tasks_id: int):
    user = request.auth
    # Get related
    try:
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except:
        model_not_found_error = ModelNotFoundError(Exception)
        raise model_not_found_error


@router.get("/list-of-tasks", response=List[ListOfTasksOut], auth=django_auth)
def list_list_of_tasks_endpoint(request):
    user = request.auth
    qs = ListOfTasks.objects.filter(user=user)
    return qs


@router.put("/list-of-tasks/{list_of_tasks_id}", response=List[ListOfTasksOut], auth=django_auth)
def update_list_of_tasks_endpoint(request, list_of_tasks_id: int, payload: ListOfTasksIn):
    user = request.auth
    try:
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        list_of_tasks.name = payload.name
        list_of_tasks.description = payload.description
    except:
        model_not_found_error = ModelNotFoundError(Exception)
        raise model_not_found_error

    try:
        list_of_tasks.save()
        lists_of_tags = ListOfTasks.objects.filter(user=user)
        return 200, lists_of_tags
    except IntegrityError:
        model_validation_error = ModelValidationError()
        model_validation_error.add(code='model-0001')
        raise model_validation_error
    except ValidationError as error:
        model_validation_error = ModelValidationError()
        model_validation_error.add_from_django(django_error=error)               
        raise model_validation_error


@router.delete("/list-of-tasks/{list_of_tasks_id}", response=List[ListOfTasksOut], auth=django_auth)
def delete_list_of_tasks_endpoint(request, list_of_tasks_id: int):
    user = request.auth
    try:
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
    except:
        model_not_found_error = ModelNotFoundError(Exception)
        raise model_not_found_error


    list_of_tasks.delete()
    lists_of_tags = ListOfTasks.objects.filter(user=user)
    return 200, lists_of_tags

####################################################
# Tasks
####################################################


@router.post("/task", response={200: ListOfTasksOut, 403: Dict}, auth=django_auth)
def create_task_endpoint(request, payload: TaskIn):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}

    list_of_tasks_id = payload.list_of_tasks_id

    try:
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}

    task = Task()
    task.name = payload.name
    task.description = payload.description
    task.list_of_tasks = list_of_tasks
    try:
        task.save()
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except IntegrityError:
        errors.append({
            "error": "auth-0001",
            "message": "Duplicated Username",
            "detail": "",
        })
        return 403, {"success": False, 'errors': errors}
    except ValidationError as err:
        for key, value in err.error_dict.items():
            print('key ' + key)
            print('value ' + value)
            for code in value:
                print('code ' + code)


@router.get("/task/{task_id}", response=TaskOut, auth=django_auth)
def get_task_endpoint(request, task_id: int):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}
    try:
        task = Task.objects.get(
            id=task_id, list_of_tasks__user=user)  # Test this
        return tasks
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}


@router.put("/task/{task_id}", response={200: ListOfTasksOut, 403: Dict}, auth=django_auth)
def edit_task_endpoint(request, task_id: int,  payload: TaskIn):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}
    # Validate Schema:
    try:
        task = Task.objects.get(
            id=task_id, list_of_tasks__user=user)  # Test this
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}

    if payload.name:
        task.name = payload.name
    if payload.description:
        task.description = payload.description

    if payload.done is None:
        task.done = False
    else:
        task.done = payload.done

    list_of_tasks_id = task.list_of_tasks.id
    try:
        task.save()
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except IntegrityError as err:
        print(err)
        errors.append({
            "error": "auth-0001",
            "message": "Duplicated Username",
            "detail": "",
        })
        return 403, {"success": False, 'errors': errors}
    except ValidationError as err:
        for key, value in err.error_dict.items():
            print('key ' + key)
            print('value ' + value)
            for code in value:
                print('code ' + code)


@router.delete("/task/{task_id}", response={200: ListOfTasksOut, 403: Dict}, auth=django_auth)
def delete_task_endpoint(request, task_id: int):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}
    try:
        task = Task.objects.get(
            id=task_id, list_of_tasks__user=user)  # Test this
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}

    list_of_tasks_id = task.list_of_tasks.id
    try:
        task.delete()
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except IntegrityError:
        errors.append({
            "error": "auth-0001",
            "message": "Duplicated Username",
            "detail": "",
        })
        return 403, {"success": False, 'errors': errors}
    except ValidationError as err:
        for key, value in err.error_dict.items():
            print('key ' + key)
            print('value ' + value)
            for code in value:
                print('code ' + code)

####################################################
# Subtasks
####################################################


@router.post("/subtask", response={200: ListOfTasksOut, 403: Dict, 404: Dict}, auth=django_auth)
def create_subtask_endpoint(request, payload: SubTaskIn):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}
    task_id = payload.tasks_id
    try:
        task = Task.objects.get(
            id=task_id, list_of_tasks__user=user)  # Test this
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}

    subtask = SubTask()
    subtask.name = payload.name
    subtask.description = payload.description
    subtask.task = task
    list_of_tasks_id = task.list_of_tasks.id

    try:
        subtask.save()
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except IntegrityError as err:
        print(err)
        errors.append({
            "error": "auth-0001",
            "message": "Duplicated Username",
            "detail": "",
        })
        return 403, {"success": False, 'errors': errors}
    except ValidationError as err:
        for key, value in err.error_dict.items():
            print('key ' + key)
            print('value ' + value)
            for code in value:
                print('code ' + code)


@router.get("/subtask/{subtask_id}", response=SubTaskOut, auth=django_auth)
def get_subtask_endpoint(request, subtask_id: int):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}

    try:
        subtask = SubTask.objects.get(
            id=subtask_id, task__list_of_tasks__user=user)  # Test this
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}

    return subtask


@router.put("/subtask/{subtask_id}", response={200: ListOfTasksOut, 403: Dict, 404: Dict}, auth=django_auth)
def edit_subtask_endpoint(request, subtask_id: int, payload: SubTaskIn):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}

    try:
        subtask = SubTask.objects.get(
            id=subtask_id, task__list_of_tasks__user=user)  # Test this
    except Exception as e:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}

    if payload.name:
        subtask.name = payload.name
    if payload.description:
        subtask.description = payload.description

    if payload.done is None:
        subtask.done = False
    else:
        subtask.done = payload.done

    list_of_tasks_id = subtask.task.list_of_tasks.id

    try:
        subtask.save()
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except IntegrityError as err:
        print(err)
        errors.append({
            "error": "auth-0001",
            "message": "Duplicated Username",
            "detail": "",
        })
        return 403, {"success": False, 'errors': errors}
    except ValidationError as err:
        for key, value in err.error_dict.items():
            print('key ' + key)
            print('value ' + value)
            for code in value:
                print('code ' + code)


@router.delete("/subtask/{subtask_id}", response={200: ListOfTasksOut, 403: Dict, 404: Dict}, auth=django_auth)
def delete_subtasks_endpoint(request, subtask_id: int):
    errors = []
    user = request.auth
    # Validate Login
    if user is None:
        errors.append({
            "error": "auth-0002",
            "message": "Not Log In",
            "detail": "",
        })
        return 403, {"success": False, "errors": errors}
    try:
        subtask = SubTask.objects.get(
            id=subtask_id, task__list_of_tasks__user=user)  # Test this
    except:
        errors.append({
            "error": "auth-0002",
            "message": "List of task not found",
            "detail": "",
        })
        return 404, {"success": False, "errors": errors}
    list_of_tasks_id = subtask.task.list_of_tasks.id
    try:
        subtask.delete()
        list_of_tasks = ListOfTasks.objects.get(id=list_of_tasks_id, user=user)
        return 200, list_of_tasks
    except IntegrityError:
        errors.append({
            "error": "auth-0001",
            "message": "Duplicated Username",
            "detail": "",
        })
        return 403, {"success": False, 'errors': errors}
    except ValidationError as err:
        for key, value in err.error_dict.items():
            print('key ' + key)
            print('value ' + value)
            for code in value:
                print('code ' + code)
