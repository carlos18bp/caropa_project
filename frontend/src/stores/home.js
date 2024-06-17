import { defineStore } from 'pinia';
import { get_request } from './services/request_http';

export const useHomeStore = defineStore('homeStore', {
  state: () => ({
    home: null,
    banners: [],
    home_categories: [],
    dataLoaded: false,
  }),
  actions: {
    /**
     * Fetches the home data from the backend.
     * Calls the API endpoint to get the data and updates the store's state.
     * Checks if the data has already been loaded to prevent redundant requests.
     */
    async fetchHome() {
      if (!this.dataLoaded) {
        try {
          const response = await get_request('home-data/');
          const homeData = response.data;
          this.home = homeData.home;
          this.banners = homeData.banners;
          this.home_categories = homeData.home_categories;

          this.dataLoaded = true;
          return response.status;
        } catch (error) {
          console.error('Failed to fetch home data:', error);
        }
      }
    }
  }
});
