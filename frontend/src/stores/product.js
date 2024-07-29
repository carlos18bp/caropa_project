import { defineStore } from "pinia";
import { create_request, get_request } from "./services/request_http";

/**
 * Define the product store using Pinia
 */
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
     * Filter products by name and language
     * @param {Object} state - The current state of the store
     * @return {Function} - A function that takes a product name and language,
     *                      and returns a filtered list of products that match
     *                      the name in the specified language and have stock available
     */
    productsByName: (state) => (name, lang) => {
      const lowerCaseName = name.toLowerCase();
      return state.uniqueProductsByRef.filter((product) => {
        const productName =
          lang === "en"
            ? product.product_detail.name_en.toLowerCase()
            : product.product_detail.name_es.toLowerCase();
        return productName.includes(lowerCaseName) && product.stock > 0;
      });
    },
    /**
     * Get products by reference
     * @param {Object} state - The state object
     * @returns {Function} - Function to get products by reference
     */
    productsByRef: (state) => (ref) => {
      return state.products.filter(
        (product) => product.ref === ref && product.stock > 0
      );
    },
    /**
     * Get unique products by reference
     * @param {Object} state - The state object
     * @returns {Array} - Array of unique products by reference
     */
    uniqueProductsByRef: (state) => {
      const productsMap = new Map();
      state.products.forEach((product) => {
        if (product.stock > 0) {
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
     * Get a list of primary categories
     * @param {Object} state - The current state of the store
     * @return {Function} - A function that takes a language and returns a list
     *                      of unique primary category names in the specified language
     */
    primaryCategories: (state) => (lang) => {
      const primaryCategories = new Set();
      primaryCategories.add("All");
      state.products.forEach((product) => {
        product.categories.forEach((category) => {
          if (category.is_primary) {
            const categoryName =
              lang === "en" ? category.name_en : category.name_es;
            primaryCategories.add(categoryName);
          }
        });
      });
      return Array.from(primaryCategories);
    },
    /**
     * Get a list of non-primary categories
     * @param {Object} state - The current state of the store
     * @return {Function} - A function that takes a language and returns a list
     *                      of unique non-primary category names in the specified language
     */
    nonPrimaryCategories: (state) => (lang) => {
      const nonPrimaryCategories = new Set();
      state.products.forEach((product) => {
        product.categories.forEach((category) => {
          if (!category.is_primary) {
            const categoryName =
              lang === "en" ? category.name_en : category.name_es;
            nonPrimaryCategories.add(categoryName);
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
     * @param {Object} state - The current state of the store
     * @return {Function} - A function that takes a primary category name and language,
     *                      and returns a list of unique products with their colors in the specified category
     */
    uniqueProductsByPrimaryCategory: (state) => (primaryCategory, lang) => {
      const productsMap = new Map();
      state.products.forEach((product) => {
        if (
          product.stock > 0 &&
          product.categories.some(
            (category) =>
              (lang === "en" ? category.name_en : category.name_es) ===
                primaryCategory && category.is_primary
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
     * Get all trending products
     * @param {object} state - The state object
     * @returns {array} - The list of products that are trending
     */
    trendingProducts: (state) => {
      return state.products.filter((product) => product.trending_now);
    },
    /**
     * Get total number of products in the cart
     * @param {object} state - The state object
     * @returns {number} - The total number of products in the cart
     */
    totalCartProducts: (state) => {
      return state.cartProducts.reduce((total, product) => {
        return total + product.quantity;
      }, 0);
    },
    /**
     * Get total price of products in the cart
     * @param {object} state - The state object
     * @returns {number} - The total price of products in the cart
     */
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
     * Filter products by primary category
     * @param {String} lang - The language to use for filtering
     */
    filterProductsByCategory(lang) {
      if (this.primaryCategorySeleted === "All") {
        this.filteredProductsByCategory = this.uniqueProductsByRef;
      } else {
        this.filteredProductsByCategory = this.uniqueProductsByPrimaryCategory(
          this.primaryCategorySeleted,
          lang
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
      lang = "en",
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
        this.nonPrimaryCategoriesSelected,
        lang
      );
      this.filterProductsByPriceRange(this.minPrice, this.maxPrice);
      this.filterProductsByColor(this.colorsSelected);
    },
    /**
     * Filter products by non-primary categories
     * @param {Array} nonPrimaryCategoriesSelected - The list of selected non-primary category names
     * @param {String} lang - The language to use for filtering
     */
    filterProductsByNonPrimaryCategory(nonPrimaryCategoriesSelected, lang) {
      if (nonPrimaryCategoriesSelected.length === 0) return;

      const refSet = new Set();
      const uniqueProducts = [];

      this.filteredProducts.forEach((product) => {
        if (
          product.categories.some((category) => {
            const categoryName =
              lang === "en" ? category.name_en : category.name_es;
            return (
              nonPrimaryCategoriesSelected.includes(categoryName) &&
              !category.is_primary
            );
          })
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
    /**
     * Add product to the cart
     * @param {Object} addProduct - The product to add to the cart
     */
    addProductToCart(addProduct, colorSelected) {
      const existingProduct = this.cartProducts.find(
        (product) => product === addProduct
      );

      if (existingProduct) {
        existingProduct.quantity += 1;
      } else {
        this.cartProducts.push({ ...addProduct, quantity: 1, color_selected: colorSelected });
      }
      localStorage.setItem("cartProducts", JSON.stringify(this.cartProducts));
    },
    /**
     * Remove product from the cart
     * @param {Number} removeProductId - The ID of the product to remove from the cart
     */
    removeProductFromCart(removeProduct) {
      const removeProductFound = this.cartProducts.find(
        (product) => product === removeProduct
      );

      if (removeProductFound.quantity > 1) {
        removeProductFound.quantity -= 1;
      } else {
        this.cartProducts = this.cartProducts.filter(
          (product) => product !== removeProductFound
        );
      }
      localStorage.setItem("cartProducts", JSON.stringify(this.cartProducts));
    },
  },
});
