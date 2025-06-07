<script setup>
import { ref, computed } from "vue";
import { useTaskStore } from "./taskStore";

const taskStore = useTaskStore();
const props = defineProps({
  show: Boolean,
  listOfTaskId: Number,
  listOfTaskName: String,
});
const emit = defineEmits(["close"]);
const name = ref(false);

const nameValue = computed({
  // getter
  get() {
    return props.listOfTaskName;
  },
  // setter
  set(newValue) {
    name.value = newValue;
  },
});

function editListOfTasks(listOfTaskId) {
  taskStore.editListOfTasks({
    id: listOfTaskId,
    name: name.value,
    description: "",
  });
  emit("close");
}
</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-container">
        <div>
          <h3 name="header">Edit List</h3>
        </div>
        <div class="modal-body">
          <form @submit.prevent="editListOfTasks(listOfTaskId)">
            <div class="form-group my-3">
              <label for="exampleInputEmail1">New Name:</label>
              <input
                type="text"
                v-model="nameValue"
                required
                class="form-control rounded-0"
              />
            </div>
            <div class="d-grid gap-2 d-md-flex justify-content-end">
              <button class="btn btn-primary rounded-0" id="button-addon1">
                Save
              </button>
              <button
                class="btn rounded-0"
                @click.prevent="$emit('close')"
                id="button-addon1"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}

.modal-container {
  width: 300px;
  margin: auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
