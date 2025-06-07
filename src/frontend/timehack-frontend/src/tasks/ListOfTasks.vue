<script setup>
import { ref } from "vue";
import { useTaskStore } from "./taskStore";
import ModalEditListOfTask from "./ModalEditListOfTask.vue";

const taskStore = useTaskStore();
const showModal = ref(false);
const listOfTaskId = ref(false);
const listOfTaskName = ref(false);

function deleteListOfTask(id) {
  taskStore.deleteListOfTasks(id);
}

function loadEditListOfTasks(id, name) {
  showModal.value = true;
  listOfTaskId.value = id;
  listOfTaskName.value = name;
}
</script>
<template>
  <ul class="list-group list-group-flush mb-5">
    <li
      class="list-group-item px-0 py-1"
      style="background-color: rgba(0, 0, 0, 0)"
      v-for="listOfTask in taskStore.listsOfTasks"
      :key="listOfTask.id"
    >
      <div class="float-start">
        <a
          href="#"
          class="link-underline-opacity-0 link-underline"
          @click.prevent="taskStore.loadCurrentListOfTasks(listOfTask.id)"
          >{{ listOfTask.name }}</a
        >
      </div>
      <div class="float-end">
        <button
          class="btn btn btn btn-link py-0 px-0"
          @click="deleteListOfTask(listOfTask.id)"
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
          @click="loadEditListOfTasks(listOfTask.id, listOfTask.name)"
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
  <Teleport to="body">
    <ModalEditListOfTask
      :show="showModal"
      :listOfTaskId="listOfTaskId"
      :listOfTaskName="listOfTaskName"
      @close="showModal = false"
    />
  </Teleport>
</template>

<style></style>
