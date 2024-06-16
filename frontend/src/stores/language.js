import { defineStore } from 'pinia';

export const useAppStore = defineStore({
  id: 'app',
  state: () => ({
    currentLanguage: 'en',
  }),
  actions: {
    setCurrentLanguage(language) {
      this.currentLanguage = language;
    },
  },
  getters: {
    getCurrentLanguage() {
      return this.currentLanguage;
    },
  },
});