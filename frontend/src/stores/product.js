import { defineStore } from "pinia";
import { create_request, get_request } from "./services/request_http";

export const useProductStore = defineStore("productStore", {
  state: () => ({
    products: [],
    dataLoaded: false,
    primaryCategorySeleted: "All",
    filteredProductsByCategory: [],
    filteredProducts: [],
    nonPrimaryCategoriesSelected: [],
    minPrice: 0,
    maxPrice: 0,
    colorsSelected: [],
    categoryFilterKey: 0,
    priceFilterKey: 0,
    colorFilterKey: 0,
    cartProducts: [],
  }),
  getters: {
    /**
     * Find product by ID
     * @param {Object} state - The state object
     * @returns {Function} - Function to get product by ID
     */
    productById: (state) => (productId) => {
      return state.products.find((product) => product.id === productId);
    },
    /**
     * Get products by reference
     * @param {Object} state - The state object
     * @returns {Function} - Function to get products by reference
     */
    productsByRef: (state) => (ref) => {
      return state.products.filter((product) => product.ref === ref);
    },
    /**
     * Get unique products by reference
     * @param {Object} state - The state object
     * @returns {Array} - Array of unique products by reference
     */
    uniqueProductsByRef: (state) => {
      const productsMap = new Map();
      state.products.forEach((product) => {
        const ref = product.ref;
        const color = product.color.name;
        if (!productsMap.has(ref)) {
          productsMap.set(ref, {
            ...product,
            colors: [color],
          });
        } else {
          const existingProduct = productsMap.get(ref);
          existingProduct.colors.push(color);
        }
      });
      return Array.from(productsMap.values());
    },
    /**
     * Get primary categories
     * @param {Object} state - The state object
     * @returns {Array} - Array of primary categories
     */
    primaryCategories: (state) => {
      const primaryCategories = new Set();
      primaryCategories.add("All");
      state.products.forEach((product) => {
        product.categories.forEach((category) => {
          if (category.is_primary) {
            primaryCategories.add(category.name);
          }
        });
      });
      return Array.from(primaryCategories);
    },
    /**
     * Get non-primary categories
     * @param {Object} state - The state object
     * @returns {Array} - Array of non-primary categories
     */
    nonPrimaryCategories: (state) => {
      const nonPrimaryCategories = new Set();
      state.products.forEach((product) => {
        product.categories.forEach((category) => {
          if (!category.is_primary) {
            nonPrimaryCategories.add(category.name);
          }
        });
      });
      return Array.from(nonPrimaryCategories);
    },
    /**
     * Get unique colors from filtered products by category
     * @param {Object} state - The state object
     * @returns {Array} - Array of unique colors
     */
    uniqueColors: (state) => {
      const colorSet = new Set();
      state.filteredProductsByCategory.forEach((product) => {
        if (product.colors && Array.isArray(product.colors)) {
          product.colors.forEach((color) => {
            if (color) {
              colorSet.add(color);
            }
          });
        }
      });
      return Array.from(colorSet);
    },
    /**
     * Get unique products by primary category
     * @param {Object} state - The state object
     * @returns {Function} - Function to get unique products by primary category
     */
    uniqueProductsByPrimaryCategory: (state) => (primaryCategory) => {
      const productsMap = new Map();
      state.products.forEach((product) => {
        if (
          product.categories.some(
            (category) =>
              category.name === primaryCategory && category.is_primary
          )
        ) {
          const ref = product.ref;
          const color = product.color.name;
          if (!productsMap.has(ref)) {
            productsMap.set(ref, {
              ...product,
              colors: [color],
            });
          } else {
            const existingProduct = productsMap.get(ref);
            existingProduct.colors.push(color);
          }
        }
      });
      return Array.from(productsMap.values());
    },
    /**
     * Get minimum price in filtered products
     * @param {Object} state - The state object
     * @returns {Number} - Minimum price
     */
    minPriceInFilteredProducts: (state) => {
      if (state.filteredProductsByCategory.length === 0) return 0;
      return Math.min(
        ...state.filteredProductsByCategory.map((product) =>
          parseFloat(product.product_detail.price)
        )
      );
    },
    /**
     * Get maximum price in filtered products
     * @param {Object} state - The state object
     * @returns {Number} - Maximum price
     */
    maxPriceInFilteredProducts: (state) => {
      if (state.filteredProductsByCategory.length === 0) return 0;
      return Math.max(
        ...state.filteredProductsByCategory.map((product) =>
          parseFloat(product.product_detail.price)
        )
      );
    },
    /**
     * Get all trending products.
     *
     * @param {object} state - The state object.
     * @returns {array} - The list of products that are trending.
     */
    trendingProducts: (state) => {
      return state.products.filter((product) => product.trending_now);
    },
    totalCartProducts: (state) => {
      return state.cartProducts.reduce((total, product) => {
        return total + product.quantity;
      }, 0);
    },
    totalCartPrice: (state) => {
      return state.cartProducts.reduce((total, product) => {
        return (
          total + parseFloat(product.product_detail.price) * product.quantity
        );
      }, 0);
    },
  },
  actions: {
    /**
     * Fetch products from the server
     */
    async fetchProducts() {
      if (!this.dataLoaded) {
        try {
          const response = await get_request("products-data/");
          const data = response.data;
          this.products = Array.isArray(data) ? data : [];

          this.dataLoaded = true;
          return response.status;
        } catch (error) {
          console.error("Failed to fetch products:", error);
        }
      }
    },
    /**
     * Filter products by category
     * @param {String} category - The category to filter by
     */
    filterProductsByCategory() {
      if (this.primaryCategorySeleted === "All") {
        this.filteredProductsByCategory = this.uniqueProductsByRef;
      } else {
        this.filteredProductsByCategory = this.uniqueProductsByPrimaryCategory(
          this.primaryCategorySeleted
        );
      }
      this.categoryFilterForceRerender();
      this.priceFilterForceRerender();
      this.colorFilterForceRerender();
      this.filteredProducts = this.filteredProductsByCategory;
    },
    /**
     * Filter products by various criteria
     * @param {Object} filters - The filters to apply
     */
    filterProducts({
      nonPrimaryCategoriesSelected = [],
      is_nonPrimaryCategoriesFilter = false,
      minPrice = 0,
      maxPrice = 0,
      is_priceFilter = false,
      colorsSelected = [],
      is_colorsFilter = false,
    } = {}) {
      this.filteredProducts = this.filteredProductsByCategory;

      if (
        JSON.stringify(this.nonPrimaryCategoriesSelected) !==
        JSON.stringify(nonPrimaryCategoriesSelected)
      ) {
        if (is_nonPrimaryCategoriesFilter)
          this.nonPrimaryCategoriesSelected = nonPrimaryCategoriesSelected;
      }
      if (this.minPrice !== minPrice && is_priceFilter) {
        this.minPrice = minPrice;
      }
      if (this.maxPrice !== maxPrice && is_priceFilter) {
        this.maxPrice = maxPrice;
      }
      if (
        JSON.stringify(this.colorsSelected) !== JSON.stringify(colorsSelected)
      ) {
        if (is_colorsFilter) this.colorsSelected = colorsSelected;
      }

      this.filterProductsByNonPrimaryCategory(
        this.nonPrimaryCategoriesSelected
      );
      this.filterProductsByPriceRange(this.minPrice, this.maxPrice);
      this.filterProductsByColor(this.colorsSelected);
    },
    /**
     * Filter products by non-primary categories
     * @param {Array} nonPrimaryCategoriesSelected - Selected non-primary categories
     */
    filterProductsByNonPrimaryCategory(nonPrimaryCategoriesSelected) {
      if (nonPrimaryCategoriesSelected.length === 0) return;

      const refSet = new Set();
      const uniqueProducts = [];

      this.filteredProducts.forEach((product) => {
        if (
          product.categories.some(
            (category) =>
              nonPrimaryCategoriesSelected.includes(category.name) &&
              !category.is_primary
          )
        ) {
          if (!refSet.has(product.ref)) {
            refSet.add(product.ref);
            uniqueProducts.push(product);
          }
        }
      });

      this.filteredProducts = uniqueProducts;
    },
    /**
     * Filter products by price range
     * @param {Number} minPrice - Minimum price
     * @param {Number} maxPrice - Maximum price
     */
    filterProductsByPriceRange(minPrice, maxPrice) {
      if (!minPrice) return;
      if (!maxPrice) return;

      this.filteredProducts = this.filteredProducts.filter((product) => {
        const price = parseFloat(product.product_detail.price);
        return price >= minPrice && price <= maxPrice;
      });
    },
    /**
     * Filter products by selected colors
     * @param {Array} colorsSelected - Selected colors
     */
    filterProductsByColor(colorsSelected) {
      if (colorsSelected.length === 0) return;

      this.filteredProducts = this.filteredProducts.filter((product) =>
        product.colors.some((color) => colorsSelected.includes(color))
      );
    },
    /**
     * Force rerender for category filter
     */
    categoryFilterForceRerender() {
      this.categoryFilterKey += 1;
      this.nonPrimaryCategoriesSelected = [];
    },
    /**
     * Force rerender for price filter
     */
    priceFilterForceRerender() {
      this.priceFilterKey += 1;
      this.minPrice = 0;
      this.maxPrice = 0;
    },
    /**
     * Force rerender for color filter
     */
    colorFilterForceRerender() {
      this.colorFilterKey += 1;
      this.colorsSelected = [];
    },
    addProductToCart(addProduct) {
      const existingProduct = this.cartProducts.find(
        (product) => product.id === addProduct.id
      );

      if (existingProduct) {
        existingProduct.quantity += 1;
      } else {
        this.cartProducts.push({ ...addProduct, quantity: 1 });
      }
      localStorage.setItem("cartProducts", JSON.stringify(this.cartProducts));
    },
    removeProductFromCart(removeProductId) {
      const removeProduct = this.cartProducts.find(
        (product) => product.id === removeProductId
      );

      if (removeProduct.quantity > 1) {
        removeProduct.quantity -= 1;
      } else {
        this.cartProducts = this.cartProducts.filter(
          (product) => product !== removeProduct
        );
      }
      localStorage.setItem("cartProducts", JSON.stringify(this.cartProducts));
    },
    async createSale(form) {
      try {
        const response = await create_request("create-sale/", {
          email: form.email,
          address: form.address,
          city: form.city,
          state: form.state,
          postal_code: form.postalCode,
          sold_products: form.soldProducts,
        });

        return response.status
      } catch (error) {
        console.error("Error creating sale:", error);
      }
    },
  },
});
