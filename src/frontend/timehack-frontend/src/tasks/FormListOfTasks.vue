<script setup>
import { ref } from "vue";
import { useTaskStore } from "./taskStore";

const listOfTasksNameValue = ref("");
const taskStore = useTaskStore();

function createListOfTasks() {
  taskStore.createListOfTasks({
    name: listOfTasksNameValue.value,
    description: "",
  });
  listOfTasksNameValue.value = "";
}
</script>

<template>
  <form @submit.prevent="createListOfTasks">
    <div class="input-group mb-4 rounded-0">
      <input
        type="text"
        v-model="listOfTasksNameValue"
        name="listOfTasksNameValue"
        placeholder="List Name"
        required
        class="form-control rounded-0"
      />
      <button
        class="btn btn-outline-secondary rounded-0"
        style="border-color: rgb(222, 226, 230)"
        id="buttonAddTask"
      >
        Add Task
      </button>
    </div>
  </form>
</template>
<style></style>
