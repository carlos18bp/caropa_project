<template>
    <Header></Header>

    <div class="relative px-8">
        <div>

            <main class="mx-auto xl:max-w-7xl">
                <section aria-labelledby="products-heading">
                    <div class="grid gap-x-8 gap-y-10 grid-cols-4">

                        <!-- Filters -->
                        <div class="col-span-4 md:col-span-1">
                            <CategoryFilter class="mb-16" :key="categoryFilterKey" />
                            <PriceFilter class="mb-6" :key="priceFilterKey" />
                            <ColorFilter :key="colorFilterKey" />
                        </div>

                        <!-- Product Listing -->
                        <div class="col-span-4 md:col-span-3">
                            <div class="mx-auto pt-8 pb-16 max-w-7xl">
                                <div class="mt-6 grid gap-x-6 gap-y-10 md:grid-cols-2 xl:grid-cols-3">
                                    <div v-for="product in paginatedProducts" :key="product.id" class="group relative">
                                        <div
                                            class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 aspect-none group-hover:opacity-75 h-80 mb-4">
                                            <img :src="product.gallery_urls[0]"
                                                class="object-cover object-center h-full w-full" />
                                        </div>
                                        <div class="mt-2 flex justify-between">
                                            <RouterLink :to="{ name: 'product', params: { product_ref: product.ref } }">
                                                <span aria-hidden="true" class="absolute inset-0" />
                                                <h3 class="text-sm">
                                                    <span v-if="currentLanguage === 'en'">
                                                        {{ product.product_detail.name_en }}
                                                    </span>
                                                    <span v-else>{{ product.product_detail.name_es }}</span>
                                                </h3>
                                                <p class="text-sm font-medium text-gray-700 text-left mb-2">
                                                    <span v-if="currentLanguage === 'en'">{{product.product_detail.description_en }}</span>
                                                    <span v-else>{{product.product_detail.description_es }}</span>
                                                </p>
                                                <p class="text-sm font-medium text-gray-900 text-left">$ {{
                                product.product_detail.price }}</p>
                                            </RouterLink>
                                        </div>
                                    </div>
                                </div>

                                <!-- Pagination -->
                                <nav class="flex items-center justify-between border-t border-gray-200 px-4 mt-8">
                                    <a href="#"
                                        class="inline-flex items-center border-t-2 border-transparent pr-1 pt-4 text-sm font-medium text-gray-500 hover:border-terciary_p hover:text-terciary_p"
                                        @click="goToPage(currentPage - 1)" :disabled="currentPage === 1">
                                        <ArrowLongLeftIcon class="mr-3 h-5 w-5 text-primary_p" aria-hidden="true" />
                                        Previous
                                    </a>

                                    <div>
                                        <template v-for="page in totalPages" :key="page">
                                            <a href="#"
                                                class="inline-flex items-center border-t-2 border-transparent px-4 pt-4 text-sm font-medium"
                                                :class="{
                                'border-primary_p text-primary_p': currentPage === page,
                                'text-gray-500 hover:text-terciary_p hover:border-terciary_p': currentPage !== page
                            }" @click="goToPage(page)">
                                                {{ page }}
                                            </a>
                                        </template>
                                    </div>

                                    <a href="#"
                                        class="inline-flex items-center border-t-2 border-transparent pl-1 pt-4 text-sm font-medium text-gray-500 hover:border-terciary_p hover:text-terciary_p"
                                        @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages">
                                        Next
                                        <ArrowLongRightIcon class="ml-3 h-5 w-5 text-primary_p" aria-hidden="true" />
                                    </a>
                                </nav>
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    </div>

    <Footer></Footer>
</template>


<script setup>
    import CategoryFilter from "@/components/product/CategoryFilter.vue";
    import ColorFilter from "@/components/product/ColorFilter.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import Header from "@/components/layouts/Header.vue";
    import PriceFilter from "@/components/product/PriceFilter.vue";
    import { ArrowLongLeftIcon, ArrowLongRightIcon } from "@heroicons/vue/20/solid";
    import { computed, onMounted, ref } from "vue";
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";

    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();

    /**
     * Computed property for filtered products
     * @returns {Array} List of filtered products
     */
    const filteredProducts = computed(() => productStore.filteredProducts);

    /**
     * Computed properties for filter keys
     */
    const categoryFilterKey = computed(() => productStore.categoryFilterKey);
    const priceFilterKey = computed(() => productStore.priceFilterKey);
    const colorFilterKey = computed(() => productStore.colorFilterKey);

    /**
     * Ref for the current page in pagination
     * @type {Number}
     */
    const currentPage = ref(1);

    /**
     * Ref to track if products are loaded
     * @type {Boolean}
     */
    const isProductsLoaded = ref(false);

    /**
     * Number of products per page based on window width
     * @type {Number}
     */
    let productsPerPage;
    if (window.innerWidth >= 1024) {
        productsPerPage = 6;
    } else if (window.innerWidth < 1024 && 760 <= window.innerWidth) {
        productsPerPage = 4;
    } else if (window.innerWidth < 760) {
        productsPerPage = 3;
    }

    /**
     * Lifecycle hook to fetch products on mount and initialize category filter
     */
    onMounted(async () => {
        await productStore.fetchProducts();
        productStore.filterProductsByCategory(currentLanguage.value);
        isProductsLoaded.value = true;
        window.scrollTo({ top: 0 });
    });

    /**
     * Computed property for total pages based on filtered products
     * @returns {Number} Total pages
     */
    const totalPages = computed(() => {
        if (isProductsLoaded.value) {
            return Math.ceil(filteredProducts.value.length / productsPerPage);
        }
        return 0;
    });

    /**
     * Computed property for paginated products
     * @returns {Array} List of products for the current page
     */
    const paginatedProducts = computed(() => {
        if (isProductsLoaded.value) {
            const start = (currentPage.value - 1) * productsPerPage;
            const end = start + productsPerPage;
            return filteredProducts.value.slice(start, end);
        }
        return [];
    });

    /**
     * Ref to store the scroll position
     * @type {Number}
     */
    const scrollPosition = ref(0);

    /**
     * Navigates to the specified page and retains scroll position
     * @param {Number} page - The page to navigate to
     */
    const goToPage = (page) => {
        if (isProductsLoaded.value && page >= 1 && page <= totalPages.value) {
            scrollPosition.value = window.scrollY;
            currentPage.value = page;
            setTimeout(() => {
                window.scrollTo(0, scrollPosition.value);
            }, 0);
        }
    };
</script>
