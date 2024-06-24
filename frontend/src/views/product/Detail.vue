<template>
    <Header></Header>

    <div v-if="product && product.product_detail" class="relative px-8 lg:px-8">
        <div class="mx-auto max-w-2xl py-16 sm:py-6 lg:max-w-7xl lg:px-8">
            <div class="lg:grid lg:grid-cols-2 lg:items-start lg:gap-x-8">

                <!-- Image gallery -->
                <TabGroup as="div" class="flex flex-col-reverse">

                    <!-- Image selector -->
                    <div class="mt-6 hidden w-full max-w-2xl sm:block lg:max-w-none">
                        <TabList class="grid grid-cols-4 gap-6">
                            <Tab v-for="image in product.gallery_urls" :key="image.id"
                                class="relative flex h-24 cursor-pointer items-center justify-center rounded-md bg-white text-sm font-medium uppercase text-black_p hover:bg-gray-50 focus:outline-none focus:ring focus:ring-opacity-50 focus:ring-offset-4 transition-transform duration-300 transform hover:scale-110">
                                <span class="absolute inset-0 overflow-hidden rounded-md">
                                    <img :src="image" alt="" class="h-full w-full object-cover object-center" />
                                </span>
                                <span :class="[
                                        'ring-transparent',
                                        'pointer-events-none absolute inset-0 rounded-md ring-2 ring-offset-2',
                                    ]" aria-hidden="true" />
                            </Tab>
                        </TabList>
                    </div>

                    <!-- Image panels -->
                    <TabPanels class="aspect-h-1 aspect-w-1 w-full">
                        <TabPanel v-for="image in product.gallery_urls" :key="image.id">
                            <img :src="image" alt=" ----- "
                                class="h-full w-full object-cover object-center sm:rounded-lg"
                                @mousemove="handleMouseMove" @mouseenter="handleMouseEnter(image)"
                                @mouseleave="handleMouseLeave" />
                        </TabPanel>
                    </TabPanels>
                </TabGroup>

                <!-- Product info -->
                <div class="relative mt-10 sm:mt-16 lg:mt-0">

                        <!-- Product Title and Brand -->
                        <div class="mb-12">
                            <p class="text-1xl text-slate-600">Caropa Couture</p>
                            <p class="text-3xl font-semibold">
                                <span v-if="currentLanguage === 'en'">
                                    {{ product.product_detail.name_en }}
                                </span>
                                <span v-else>{{ product.product_detail.name_es }}</span>
                            </p>
                            <p class="text-2xl text-slate-800 mt-2">
                                ${{ product.product_detail.price }}
                            </p>
                        </div>

                        <!-- Color Options -->
                        <div class="mb-12">
                            <h3 class="text-md font-medium text-gray-700">Color</h3>
                            <div class="flex space-x-2 mt-2">
                                <span v-for="color in colors" :key="color"
                                    class="w-8 h-8 border border-gray-300 cursor-pointer" 
                                    :class="[
                                        { 'ring-2 ring-primary_p': selectedColor === color },
                                        color === 'black' || color === 'white'
                                            ? `bg-${color}`
                                            : `bg-${color}-500`,
                                    ]" @click="updateProductByColor(color)">
                                </span>
                            </div>
                        </div>

                        <!-- Size Options -->
                        <div class="mb-12">
                            <h3 class="text-md font-medium text-gray-700">Size</h3>
                            <div class="grid grid-cols-2 gap-4 mt-2">
                                <div v-for="size in sizes" :key="size" class="p-4 border border-gray-300 rounded-md"
                                    :class="{
                                            'ring-2 ring-primary_p': selectedSize === size,
                                            'opacity-50 cursor-not-allowed': !sizesForColor.includes(size),
                                            'cursor-pointer': sizesForColor.includes(size)
                                        }" @click="setProductBySize(size)" :disabled="!sizesForColor.includes(size)">
                                    <p class="font-semibold">{{ size }}</p>
                                </div>
                            </div>
                        </div>


                        <!-- Model Information -->
                        <div class="mb-4">
                            <p class="text-gray-700 text-sm">
                                The model is 1.74m tall and wears a size M
                            </p>
                            <a href="#" class="text-yellow-600 text-sm underline">
                                Find the perfect size?
                            </a>
                        </div>

                        <!-- Add to Bag Button -->
                        <div class="mt-4">
                            <button class="w-full py-3 bg-yellow-400 text-white font-semibold rounded-md"
                                @click="addToCart">
                                Add to Bag
                            </button>
                        </div>

                    <!-- Zoomed Image Display -->
                    <div v-if="selectedImage" class="absolute inset-0 z-20">
                        <div class="rounded-lg overflow-clip bg-black bg-opacity-75">
                            <img :src="selectedImage ? selectedImage : image" alt="Image selected to zoom" 
                                :style="{
                                    transform: `scale(${zoom}) translate(${mouseX}px, ${mouseY}px)`,
                                }" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <!-- Product Carousel -->
    <ProductCarousel></ProductCarousel>

    <!-- Last content -->
    <AboutShortCut></AboutShortCut>

    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import ProductCarousel from "@/components/ProductCarousel.vue";
    import AboutShortCut from "@/components/AboutShortCut.vue";
    import { Tab, TabGroup, TabList, TabPanel, TabPanels } from "@headlessui/vue";
    import { computed, onMounted, reactive, ref, watch } from "vue";
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";
    import { useRoute } from "vue-router";
    import Swal from 'sweetalert2';

    const route = useRoute();
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();
    const productsByRef = ref([]);
    const product = reactive({});
    const selectedColor = ref(null);
    const selectedSize = ref(null);

    // This code runs when the component is mounted
    onMounted(async () => {
        /**
         * Call the function to fetch and set the product when the component is mounted.
         * Scroll the window to the top.
         */
        await fetchAndSetProduct();
        window.scrollTo({ top: 0 });
    });

    // This watcher monitors changes to 'route.params.product_ref' and updates the product details accordingly
    watch(() => route.params.product_ref, async (newRef) => {
        /**
         * Call the function to fetch and set the product whenever the route parameter 'product_ref' changes.
         * Scroll the window to the top.
         */
        await fetchAndSetProduct();
        window.scrollTo({ top: 0 });
    });

    // This function fetches and sets the product based on the route parameter 'product_ref'
    const fetchAndSetProduct = async () => {
        /**
         * Fetch product by reference from the route parameter.
         * Assign the fetched product to the 'product' reactive object.
         * Set the selected color and size based on the fetched product details.
         */
        const ref = route.params.product_ref;        
        if (ref) {
            await productStore.fetchProducts();

            productsByRef.value = await productStore.productsByRef(ref);
            if (productsByRef.value.length > 0) {
                Object.assign(product, productsByRef.value[0]);
                selectedColor.value = product.color.name;
                selectedSize.value = product.size.name;
            }
        }
    };

    /**
     * Get unique colors for the product reference
     *
     * @returns {Array} - Array of unique colors
     */
    const colors = computed(() => {
        const colorSet = new Set();
        productsByRef.value.forEach((product) => {
            colorSet.add(product.color.name);
        });
        return Array.from(colorSet);
    });

    /**
     * Get unique sizes for the product reference
     *
     * @returns {Array} - Array of unique sizes
     */
    const sizes = computed(() => {
        const sizeSet = new Set();
        productsByRef.value.forEach((product) => {
            sizeSet.add(product.size.name);
        });
        return Array.from(sizeSet);
    });

    /**
     * Get sizes available for the selected color
     *
     * @returns {Array} - Array of sizes available for the selected color
     */
    const sizesForColor = computed(() => {
        return productsByRef.value
            .filter((product) => product.color.name === selectedColor.value)
            .map((product) => product.size.name);
    });

    /**
     * Update product based on selected color
     *
     * @param {string} color - The selected color
     */
    const updateProductByColor = (color) => {
        selectedColor.value = color;
        const selectedProduct = productsByRef.value.find(
            (product) => product.color.name === color
        );
        if (selectedProduct) {
            Object.assign(product, selectedProduct);
            selectedSize.value = product.size.name;
        }
    };

    /**
     * Update size of the product selected
     *
     * @param {string} size - The selected size
     */
    const setProductBySize = (size) => {
        selectedSize.value = size;
    };

    const addToCart = () => {
        productStore.addProductToCart(product, selectedColor.value);
        Swal.fire({
            title: "Product added to Shopping Cart successfully",
            icon: "success"
        });
    };

    const selectedImage = ref(null);
    const mouseX = ref(0);
    const mouseY = ref(0);
    const zoom = ref(2); // Adjust the value to reduce the zoom level

    /**
     * Handle mouse enter event on an image
     *
     * @param {string} image - The image URL
     */
    const handleMouseEnter = (image) => {
        selectedImage.value = image;
    };

    /**
     * Handle mouse leave event on an image
     */
    const handleMouseLeave = () => {
        selectedImage.value = null;
        resetZoom();
    };

    /**
     * Handle mouse move event on an image
     *
     * @param {Event} event - The mouse move event
     */
    const handleMouseMove = (event) => {
        if (!selectedImage.value) return;

        const img = event.target.getBoundingClientRect();
        mouseX.value = (event.clientX - img.left - img.width / 2) * -1;
        mouseY.value = (event.clientY - img.top - img.height / 2) * -1;
    };

    /**
     * Reset the zoom state
     */
    const resetZoom = () => {
        mouseX.value = 0;
        mouseY.value = 0;
        zoom.value = 2;
    };
</script>
