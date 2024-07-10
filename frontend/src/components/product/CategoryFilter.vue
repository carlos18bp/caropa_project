<template>
    <div>
        <!-- Disclosure Component for Category Filter -->
        <Disclosure >
            <template #default="{ open }">

                <!-- Disclosure Button -->
                <DisclosureButton
                    class="flex justify-between w-full px-4 py-2 text-sm font-medium text-gray-700 rounded-lg hover:bg-gray-100">
                    <span><span class="test-filters-category">{{ $t('filters').category }}</span> ({{ nonPrimaryCategoriesSelected.length }})</span>
                    <ChevronUpIcon class="w-5 h-5 text-gray-500" :class="{ 'transform rotate-180': open }" />
                </DisclosureButton>

                <!-- Disclosure Panel -->
                <DisclosurePanel class="px-4 pt-4 pb-2 text-sm text-gray-700 border-t">
                    <ul class="space-y-2">
                        <!-- List of Non-Primary Categories with Checkboxes -->
                        <li v-for="category in nonPrimaryCategories" :key="category" class="flex items-center">
                            <input type="checkbox" :id="category" :value="category"
                                v-model="nonPrimaryCategoriesSelected" @change="handleCategoryChange"
                                class="h-4 w-4 text-yellow-300 border-gray-300 rounded focus:ring-yellow-400" />
                            <label :for="category" class="ml-3 text-sm text-gray-700">{{ category }}</label>
                        </li>
                    </ul>
                </DisclosurePanel>
            </template>
        </Disclosure>
    </div>
</template>

<script setup>
    import { ChevronUpIcon } from '@heroicons/vue/24/solid';
    import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue';
    import { ref, computed, watchEffect } from 'vue';
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from '@/stores/product';
    import enMessages from "@/locales/product/catalog/en";
    import esMessages from "@/locales/product/catalog/es";

    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();
    const messages = ref(enMessages)

    // Translation function
    const $t = (key) => messages.value[key];

    /**
     * Computed property for non-primary categories
     * @returns {Array} List of non-primary categories
     */
    const nonPrimaryCategories = computed(() => productStore.nonPrimaryCategories(currentLanguage.value));

    /**
     * Ref for selected non-primary categories
     * @type {Array}
     */
    const nonPrimaryCategoriesSelected = ref([]);

    // Change messages in function to currently language
    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });

    /**
     * Handles changes in category selection.
     * Forces a re-render and filters products based on selected non-primary categories.
     */
    const handleCategoryChange = () => {
        // Force a re-render of the price filter
        productStore.priceFilterForceRerender();

        // Filter products based on selected non-primary categories
        productStore.filterProducts({
            nonPrimaryCategoriesSelected: nonPrimaryCategoriesSelected.value,
            is_nonPrimaryCategoriesFilter: true,
            lang: currentLanguage.value
        });
    };
</script>