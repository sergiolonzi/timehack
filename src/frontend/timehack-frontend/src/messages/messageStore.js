import { defineStore } from "pinia";
import { ref } from "vue";

export const useMessageStore = defineStore("messageStore", () => {
  const errors = ref();
  const infos = ref();

  function addError(errorIn) {
    errors.value = [];
    let title = errorIn.title;
    errors.value = { title: title, list: [] };
    let i = 0;
    for (const errorItem of errorIn.list) {
      errors.value.list.push({
        id: i,
        message: errorItem.message,
        associated_field: errorItem.associated_field,
      });

      i++;
    }
  }

  function cleanErrors() {
    errors.value = null;
  }

  function addInfo(infosIn) {
    infos.value = [];
    let title = infosIn.title;
    infos.value = { title: title, list: [] };
    let i = 0;
    for (const infoItem of infosIn.list) {
      infos.value.list.push({
        id: i,
        message: infoItem.message,
        associated_field: errorItem.associated_field,
      });
      i++;
    }
  }
  function cleanInfos() {
    infos.value = null;
  }

  return { errors, addError, cleanErrors, infos, addInfo, cleanInfos };
});
