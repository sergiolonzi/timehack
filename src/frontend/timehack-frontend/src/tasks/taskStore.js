// store.js
/*
Old way
import { reactive } from 'vue'

export const store = reactive({'todos' : [
  { id: 1, title: 'My journeys with Vue' },
  { id: 2, title: 'Blogging with Vue' },
  { id: 3, title: 'Why Vue is so fun' }
]})
*/
import { defineStore } from "pinia";
import axios from "axios";
import { ref } from "vue";
import { useMessageStore } from "../messages/messageStore";

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export const useTaskStore = defineStore("taskStore", () => {
  const errors = ref([]);
  const listsOfTasks = ref([]);
  const currentListOfTasks = ref();
  const listOfTasksToEdit = ref({ name: "" });
  const messageStore = useMessageStore();
  /****************************************************************
   ** ListOfTasks
   ****************************************************************/
  function createListOfTasks(listOfTasksIn) {
    const csrftoken = getCookie("csrftoken");
    console.log(csrftoken);
    axios
      .post(
        "/api/list-of-tasks",
        {
          name: listOfTasksIn.name,
          description: listOfTasksIn.description,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        listsOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function cleanAll() {
    listsOfTasks.value = "";
    currentListOfTasks.value = "";
    listOfTasksToEdit.value = "";
  }

  function deleteListOfTasks(listOfTasksId) {
    const csrftoken = getCookie("csrftoken");
    console.log(csrftoken);
    axios
      .delete("/api/list-of-tasks/" + listOfTasksId, {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(function (response) {
        listsOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function loadListsOfTasks() {
    const csrftoken = getCookie("csrftoken");
    axios
      .get("/api/list-of-tasks", {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(function (response) {
        listsOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function loadCurrentListOfTasks(listOfTasksId) {
    const csrftoken = getCookie("csrftoken");
    axios
      .get("/api/list-of-tasks/" + listOfTasksId, {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function loadEditListOfTasks(listOfTasksId) {
    const csrftoken = getCookie("csrftoken");
    axios
      .get("/api/list-of-tasks/" + listOfTasksId, {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(function (response) {
        listOfTasksToEdit.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function editListOfTasks(listOfTasksIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .put(
        "/api/list-of-tasks/" + listOfTasksIn.id,
        {
          name: listOfTasksIn.name,
          done: false,
          description: listOfTasksIn.description,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        listsOfTasks.value = response.data;
        currentListOfTasks.value.name = listOfTasksIn.name;
        listOfTasksToEdit.value = "";
      })
      .catch(function (error) {
        listOfTasksToEdit.value = ""; //finally
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }
  /****************************************************************
   ** Task
   ****************************************************************/
  function createTask(taskIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .post(
        "/api/task",
        {
          name: taskIn.name,
          description: taskIn.description,
          done: false,
          list_of_tasks_id: taskIn.listOfTasksId,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function deleteTask(taskId) {
    const csrftoken = getCookie("csrftoken");
    axios
      .delete("/api/task/" + taskId, {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(
        function (response) {
          currentListOfTasks.value = response.data;
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function editTask(taskIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .put(
        "/api/task/" + taskIn.taskId,
        {
          name: taskIn.name,
          description: taskIn.description,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function doneTask(taskIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .put(
        "/api/task/" + taskIn.taskId,
        {
          done: taskIn.done,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }
  /****************************************************************
   ** SubTask
   ****************************************************************/
  function createSubtask(subtaskIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .post(
        "/api/subtask",
        {
          name: subtaskIn.name,
          done: false,
          description: subtaskIn.description,
          tasks_id: subtaskIn.taskId,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function editSubtask(subtaskIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .put(
        "/api/subtask/" + subtaskIn.subtaskId,
        {
          name: subtaskIn.name,
          description: subtaskIn.description,
        },
        {
          headers: { "X-CSRFToken": csrftoken },
        }
      )
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function deleteSubtask(subtaskId) {
    const csrftoken = getCookie("csrftoken");
    axios
      .delete("/api/subtask/" + subtaskId, {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  function doneSubtask(subtaskIn) {
    const csrftoken = getCookie("csrftoken");
    axios
      .put("/api/subtask/" + subtaskIn.subtaskId, {
        headers: { "X-CSRFToken": csrftoken },
      })
      .then(function (response) {
        currentListOfTasks.value = response.data;
      })
      .catch(function (error) {
        if (error.response) {
          let listOfErrors = error.response.data.errors;
          let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
          messageStore.addError(errorMessage);
        }
      });
  }

  return {
    errors,
    listsOfTasks,
    currentListOfTasks,
    listOfTasksToEdit,
    createListOfTasks,
    deleteListOfTasks,
    loadListsOfTasks,
    loadCurrentListOfTasks,
    loadEditListOfTasks,
    editListOfTasks,
    createTask,
    deleteTask,
    editTask,
    doneTask,
    createSubtask,
    editSubtask,
    deleteSubtask,
    doneSubtask,
    cleanAll,
  };
});
