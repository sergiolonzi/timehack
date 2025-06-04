<script setup>
import { ref } from "vue";
import { useTaskStore } from "./taskStore";

const taskNameValue = ref("");
const taskStore = useTaskStore();

function createTask() {
  taskStore.createTask({
    name: taskNameValue.value,
    description: "",
    listOfTasksId: taskStore.currentListOfTasks.id,
  });
  taskNameValue = "";
}
</script>

<template>
  <form @submit.prevent="createTask">
    <div class="input-group mb-4 rounded-0">
      <input
        type="text"
        v-model="taskNameValue"
        name="addTask"
        required
        class="form-control rounded-0"
        placeholder="Task Name"
      />
      <button
        class="btn btn-outline-secondary rounded-0"
        style="border-color: rgb(222, 226, 230)"
        id="button-addon1"
      >
        Add Task
      </button>
    </div>
  </form>
</template>
<style></style>
