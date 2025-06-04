<script setup>
import { useMessageStore } from "./messageStore";
import { onMounted } from "vue";

const messageStore = useMessageStore();

onMounted(() => {
  messageStore.cleanErrors();
  messageStore.cleanInfos();
});
</script>
<template>
  <div v-if="messageStore.errors" class="alert alert-danger" role="alert">
    <p v-if="messageStore.errors.title">{{ messageStore.errors.title }}</p>
    <p v-else>Correct the next errors:</p>
    <ul class="my-0">
      <li v-for="error in messageStore.errors.list" :key="error.id">
        {{ error.message }}
      </li>
    </ul>
  </div>
  <div v-if="messageStore.infos" class="alert alert-info" role="alert">
    <p v-if="messageStore.infos.title">{{ messageStore.infos.title }}</p>
    <p v-else>Messages:</p>
    <ul class="my-0">
      <li v-for="info in messageStore.infos.list" :key="info.id">
        {{ info.value }}
      </li>
    </ul>
  </div>
</template>
<style></style>
