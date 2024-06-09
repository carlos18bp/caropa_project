import { defineStore } from 'pinia';
import { get_request } from './services/request_http';

export const useProductStore = defineStore('productStore', {
  state: () => ({
    products: [],
    currentCategories: [],
    searchQuery: '',
  }),
  getters: {
    /**
     * Get product by id.
     * @param {object} state - State.
     * @returns {function} - A function that takes a product id and returns the product.
     */
    productById: (state) => (productId) => {
      return state.products.find((product) => product.id === productId);
    },
    /**
     * Get all products by a given reference.
     * @param {object} state - The state object.
     * @returns {function} - A function that takes a reference and returns the list of products.
     */
    productsByRef: (state) => (ref) => {
      return state.products.filter(product => product.ref === ref);
    },
    /**
     * Get a unique list of products by reference.
     * 
     * @param {object} state - The state object.
     * @returns {array} - The list of unique products by reference.
     */
    uniqueProductsByRef: (state) => {
      const refSet = new Set();
      const uniqueProducts = [];

      state.products.forEach(product => {
        if (!refSet.has(product.ref)) {
          refSet.add(product.ref);
          uniqueProducts.push(product);
        }
      });

      return uniqueProducts;
    },
  },
  actions: {
    /**
     * Fetches the list of products from the backend.
     */
    async fetchProducts() {
      try {
        const data = await get_request('products/');
        this.products = Array.isArray(data) ? data : []; // Ensure products is always an array
      } catch (error) {
        console.error('Failed to fetch products:', error);
      }
    },
    /**
     * Sets the current categories for filtering.
     * 
     * @param {array} categories - The list of selected categories.
     */
    setCurrentCategories(categories) {
      this.currentCategories = categories;
    },
    /**
     * Sets the search query for filtering.
     * 
     * @param {string} query - The search query.
     */
    setSearchQuery(query) {
      this.searchQuery = query;
    }
  }
});
