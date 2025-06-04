from typing import List, Optional

from ninja import Field, Schema


#######################################
# All
#######################################
class Error(Schema):
    message: str

#######################################
# Auth
#######################################


class UserSchemaOut(Schema):
    id: int
    username: str
    email: str


class UserSchemaIn(Schema):
    username: str
    password: str
    password_confirm: str
    email: str


class UserUpdateSchemaIn(Schema):
    password: Optional[str] = None
    password_confirm: Optional[str] = None
    email: Optional[str] = None


class LoginSchemaIn(Schema):
    username: str
    password: str

#######################################
# Tasks
#######################################
# **************************************
# ** SubTask
# **************************************


class SubTaskOut(Schema):
    id: int
    name: str
    done: bool
    description: str


class SubTaskIn(Schema):
    name: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None
    tasks_id: Optional[int] = None

# **************************************
# ** Tasks
# **************************************


class TaskIn(Schema):
    name: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None
    list_of_tasks_id: Optional[int] = None


class TaskOut(Schema):
    id: int
    name: str
    done: bool
    description: str
    sub_tasks: List[SubTaskOut] = Field(None, alias="subtask_set")

# **************************************
# ** ListOfTasks
# **************************************


class ListOfTasksIn(Schema):
    name: str
    description: str


class ListOfTasksOut(Schema):
    id: int
    name: str
    description: str
    tasks: List[TaskOut] = Field(None, alias="task_set")
