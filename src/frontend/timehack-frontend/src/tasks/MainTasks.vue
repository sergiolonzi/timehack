<script setup>
import FormListOfTasks from "./FormListOfTasks.vue";
import Tasks from "./Tasks.vue";
import ListOfTasks from "./ListOfTasks.vue";
import UserNavbar from "../auth/UserNavbar.vue";
import { useTaskStore } from "./taskStore";
import { useAuthStore } from "../auth/authStore";
import { onMounted } from "vue";

const taskStore = useTaskStore();
const authStore = useAuthStore();
onMounted(() => {
  taskStore.loadListsOfTasks();
  authStore.loadUserInfo();
});
</script>
<template>
  <div class="container-fluid">
    <div class="row" style="min-height: 100vh">
      <div class="col-3 border-end px-4" style="background-color: #f5f7fa">
        <UserNavbar />
        <h2 class="fs-3">Lists</h2>
        <FormListOfTasks />
        <ListOfTasks />
      </div>
      <div class="col-9">
        <Tasks />
      </div>
    </div>
  </div>
</template>
<style></style>
