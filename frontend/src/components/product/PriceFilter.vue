<template>
    <div>

        <!-- Disclosure Component for Price Filter -->
        <Disclosure defaultOpen>
            <template #default="{ open }">

                <!-- Disclosure Button -->
                <DisclosureButton
                    class="flex justify-between w-full px-4 py-2 text-sm font-medium text-gray-700 rounded-lg hover:bg-gray-100">
                    <span>Price</span>
                    <ChevronUpIcon class="w-5 h-5 text-gray-500" :class="{ 'transform rotate-180': open }" />
                </DisclosureButton>

                <!-- Disclosure Panel -->
                <DisclosurePanel class="px-4 pt-4 pb-2 text-sm text-gray-700 border-t">
                    <!-- Price Inputs -->
                    <div class="flex items-center space-x-4 mb-4">
                        <input type="text" v-model="formattedMinPrice" class="w-1/2 px-2 py-1 border rounded"
                            placeholder="Min" readonly />
                        <input type="text" v-model="formattedMaxPrice" class="w-1/2 px-2 py-1 border rounded"
                            readonly />
                    </div>

                    <!-- Price Range Slider -->
                    <vue-3-slider-component v-if="minMaxLoaded" v-model="priceRange" :min="minPrice" :max="maxPrice"
                        :interval="1" :dot-size="25" :height="4" class="w-full"
                        :processStyle="{ backgroundColor: 'black' }" />
                </DisclosurePanel>
            </template>
        </Disclosure>
    </div>
</template>

<script setup>
    import { ChevronUpIcon } from '@heroicons/vue/24/solid';
    import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue';
    import { computed, nextTick, onMounted, ref, watch } from 'vue';
    import Vue3SliderComponent from 'vue-3-slider-component';
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";

    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();

    /**
     * Computed property for minimum price in filtered products
     * @returns {Number} Minimum price
     */
    const minPrice = computed(() => productStore.minPriceInFilteredProducts);

    /**
     * Computed property for maximum price in filtered products
     * @returns {Number} Maximum price
     */
    const maxPrice = computed(() => productStore.maxPriceInFilteredProducts);

    /**
     * Ref to track if min and max prices are loaded
     * @type {Boolean}
     */
    const minMaxLoaded = ref(false);

    /**
     * Ref for the price range slider
     * @type {Array}
     */
    const priceRange = ref([minPrice.value, maxPrice.value]);

    /**
     * Ref for formatted minimum price
     * @type {String}
     */
    const formattedMinPrice = ref(`$ ${minPrice.value}`);

    /**
     * Ref for formatted maximum price
     * @type {String}
     */
    const formattedMaxPrice = ref(`$ ${maxPrice.value}`);

    /**
     * Lifecycle hook to set minMaxLoaded to true when minPrice and maxPrice are available on mount
     */
    onMounted(() => {
        if (minPrice.value && maxPrice.value) minMaxLoaded.value = true;
    });

    /**
     * Watcher for changes in minPrice
     * Updates the price range and formattedMinPrice
     */
    watch(minPrice, async (newMin) => {
        minMaxLoaded.value = false;
        priceRange.value[0] = newMin;
        formattedMinPrice.value = `$ ${newMin}`;

        await nextTick();
        minMaxLoaded.value = true;
    });

    /**
     * Watcher for changes in maxPrice
     * Updates the price range and formattedMaxPrice
     */
    watch(maxPrice, async (newMax) => {
        minMaxLoaded.value = false;
        priceRange.value[1] = newMax;
        formattedMaxPrice.value = `$ ${newMax}`;

        await nextTick();
        minMaxLoaded.value = true;
    });

    /**
     * Watcher for changes in priceRange
     * Updates the formatted prices and triggers product filtering
     */
    watch(priceRange, ([newMin, newMax]) => {
        formattedMinPrice.value = `$ ${newMin}`;
        formattedMaxPrice.value = `$ ${newMax}`;
        productStore.filterProducts({ minPrice: newMin, maxPrice: newMax, is_priceFilter: true, lang: currentLanguage.value });
    });
</script>