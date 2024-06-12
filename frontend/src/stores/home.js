import { defineStore } from 'pinia';
import { get_request } from './services/request_http';

export const useHomeStore = defineStore('homeStore', {
  state: () => ({
    home: null,
    banners: [],
    home_categories: [],
    header_categories: [],
    secondary_categories: [],
    dataLoaded: false,
  }),
  actions: {
    /**
     * Fetches the home data from the backend.
     * Calls the API endpoint to get the data and updates the store's state.
     * Checks if the data has already been loaded to prevent redundant requests.
     */
    async fetchHomeData() {
      if (!this.dataLoaded) {
        try {
          const homeData = await get_request('home-data/');
          this.home = homeData.home;
          this.banners = homeData.banners;
          this.home_categories = homeData.home_categories;
          
          const categoriesData = await get_request('categories/');
          
          // Separar las categorías en principales y secundarias
          this.header_categories = categoriesData.filter(category => category.main);
          this.secondary_categories = categoriesData.filter(category => !category.main);

          this.dataLoaded = true;
        } catch (error) {
          console.error('Failed to fetch home data:', error);
        }
      }
    }
  }
});
