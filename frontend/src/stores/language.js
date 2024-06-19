import { defineStore } from 'pinia';

/**
 * Define the app store using Pinia
 */
export const useAppStore = defineStore({
  id: 'app',
  state: () => ({
    currentLanguage: 'en', // Default language is English
  }),
  actions: {
    /**
     * Set the current language
     * @param {string} language - The language to set as current
     */
    setCurrentLanguage(language) {
      this.currentLanguage = language;
    },
  },
  getters: {
    /**
     * Get the current language
     * @returns {string} - The current language
     */
    getCurrentLanguage() {
      return this.currentLanguage;
    },
  },
});
