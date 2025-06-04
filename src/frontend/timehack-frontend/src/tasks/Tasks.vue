<script setup>
import { ref } from "vue";
import { useTaskStore } from "./taskStore";
import FormTasks from "./FormTasks.vue";
import ModalAddSubtask from "./ModalAddSubtask.vue";
import ModalEditSubtask from "./ModalEditSubtask.vue";
import ModalEditTask from "./ModalEditTask.vue";
import Message from "../messages/Message.vue";

const taskStore = useTaskStore();
const showModal = ref(false);
const showModalEditSubtask = ref(false);
const showModalEditTask = ref(false);
const taskId = ref(0);
const subtaskId = ref(0);
const subtaskDone = ref(0);

function showAddSubtask(id) {
  showModal.value = true;
  taskId.value = id;
}

function showEditSubtask(id) {
  showModalEditSubtask.value = true;
  subtaskId.value = id;
}

function showEditTask(id) {
  showModalEditTask.value = true;
  taskId.value = id;
}

function deleteTask(id) {
  taskStore.deleteTask(id);
}

function deleteSubtask(id) {
  taskStore.deleteSubtask(id);
}

function doneTask(id, done) {
  taskStore.doneTask({ done: done, taskId: id });
}

function doneSubtask(id, done) {
  taskStore.doneSubtask({ done: done, subtaskId: id });
}
</script>

<template>
  <div
    v-if="taskStore.currentListOfTasks"
    class="container-fluid py-5 px-3"
    style="min-height: 100vh"
  >
    <div class="row">
      <div class="col" style="height: 100%">
        <h2>{{ taskStore.currentListOfTasks.name }}</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-8 offset-2" style="height: 100%">
        <Message />
      </div>
    </div>
    <div class="row" style="min-height: 100vh">
      <div class="col" style="height: 100%">
        <FormTasks />
        <ul class="list-group list-group-flush mb-5">
          <li
            class="list-group-item px-0 py-0 border border-0"
            v-for="task in taskStore.currentListOfTasks.tasks"
            :key="task.id"
          >
            <div class="clearfix border-bottom py-2">
              <div class="float-start mx-3">
                <input
                  @change="(event) => doneTask(task.id, event.target.checked)"
                  v-model="task.done"
                  type="checkbox"
                />
              </div>
              <div class="float-start">
                <p class="mb-0" :class="{ done: task.done }">{{ task.name }}</p>
              </div>
              <div class="float-end">
                <button
                  class="btn btn btn btn-link py-0 px-0"
                  @click="deleteTask(task.id)"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="14"
                    height="14"
                    fill="currentColor"
                    class="bi bi-x-lg"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"
                    />
                  </svg>
                </button>
              </div>
              <div class="float-end mx-1">
                <button
                  class="btn btn btn-link py-0 px-0"
                  id="show-modal"
                  @click="showEditTask(task.id)"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="14"
                    height="14"
                    fill="currentColor"
                    class="bi bi-pencil"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"
                    />
                  </svg>
                </button>
              </div>
              <div class="float-end mx-3">
                <button
                  class="btn btn btn-link py-0 px-0"
                  @click="showAddSubtask(task.id)"
                >
                  Add Subtask
                </button>
              </div>
            </div>
            <ul class="list-group list-group-flush ms-5">
              <li
                class="list-group-item px-0 py-1 border border-top-0 border-start-0 border-end-0"
                v-for="subtask in task.sub_tasks"
                :key="subtask.id"
              >
                <div class="float-start mx-3">
                  <input
                    @change="
                      (event) => doneSubtask(subtask.id, event.target.checked)
                    "
                    v-model="subtask.done"
                    type="checkbox"
                  />
                </div>
                <div class="float-start">
                  <p class="mb-1" :class="{ done: subtask.done }">
                    {{ subtask.name }}
                  </p>
                </div>
                <div class="float-end">
                  <button
                    class="btn btn btn btn-link py-0 px-0"
                    @click="deleteSubtask(subtask.id)"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="14"
                      height="14"
                      fill="currentColor"
                      class="bi bi-x-lg"
                      viewBox="0 0 16 16"
                    >
                      <path
                        d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"
                      />
                    </svg>
                  </button>
                </div>
                <div class="float-end mx-1">
                  <button
                    class="btn btn btn-link py-0 px-0"
                    id="show-modal"
                    @click="showEditSubtask(subtask.id)"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="14"
                      height="14"
                      fill="currentColor"
                      class="bi bi-pencil"
                      viewBox="0 0 16 16"
                    >
                      <path
                        d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"
                      />
                    </svg>
                  </button>
                </div>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <div v-else class="container-fluid py-5 px-3" style="min-height: 100vh">
    <div class="row">
      <div class="col" style="height: 100%">
        <h2>Welcome</h2>
      </div>
    </div>
  </div>

  <Teleport to="body">
    <ModalAddSubtask
      :show="showModal"
      :taskId="taskId"
      @close="showModal = false"
    />
  </Teleport>

  <Teleport to="body">
    <ModalEditSubtask
      :show="showModalEditSubtask"
      :subtaskId="subtaskId"
      @close="showModalEditSubtask = false"
    />
  </Teleport>
  <Teleport to="body">
    <ModalEditTask
      :show="showModalEditTask"
      :taskId="taskId"
      @close="showModalEditTask = false"
    />
  </Teleport>
</template>
<style>
.done {
  text-decoration: line-through;
}
</style>
