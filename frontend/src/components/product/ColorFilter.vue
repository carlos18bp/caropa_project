<template>
    <div>

        <!-- Disclosure Component for Color Filter -->
        <Disclosure defaultOpen>
            <template #default="{ open }">

                <!-- Disclosure Button -->
                <DisclosureButton
                    class="flex justify-between w-full px-4 py-2 text-sm font-medium text-gray-700 rounded-lg hover:bg-gray-100">
                    <span>Color ({{ colorsSelected.length }})</span>
                    <ChevronUpIcon class="w-5 h-5 text-gray-500" :class="{ 'transform rotate-180': open }" />
                </DisclosureButton>

                <!-- Disclosure Panel -->
                <DisclosurePanel class="px-4 pt-4 pb-2 text-sm text-gray-700 border-t">
                    <div class="grid grid-cols-3 gap-4">
                        <!-- List of Colors with Buttons -->
                        <div v-for="color in colors" :key="color"
                            class="relative flex flex-col items-center cursor-pointer">
                            <!-- Color Button -->
                            <button @click="handleColorChange(color)" 
                                :class="[
                                    'w-8 h-8 rounded-full border-4 flex items-center justify-center',
                                    color === 'black' || color === 'white' ? `bg-${color}` :
                                        (color === 'yellow' ? `bg-${color}-300` : `bg-${color}-500`),
                                ]">
                                <!-- Checked Icon for Selected Colors -->
                                <img v-if="colorsSelected.includes(color) && color !== 'white'"
                                    src="@/assets/images/product/checked_white.png" alt="checked"
                                    class="absolute size-3" />
                                <img v-if="colorsSelected.includes(color) && color === 'white'"
                                    src="@/assets/images/product/checked_black.png" alt="checked"
                                    class="absolute size-3" />
                            </button>
                            <!-- Color Label -->
                            <span class="mt-1 text-xs text-center">{{ capitalizeFirstLetter(color) }}</span>
                        </div>
                    </div>
                </DisclosurePanel>
            </template>
        </Disclosure>
    </div>
</template>

<script setup>
    import { ChevronUpIcon } from '@heroicons/vue/24/solid';
    import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue';
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from '@/stores/product';
    import { computed, ref } from 'vue';

    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();

    /**
     * Computed property for unique colors
     * @returns {Array} List of unique colors
     */
    const colors = computed(() => productStore.uniqueColors);

    /**
     * Ref for selected colors
     * @type {Array}
     */
    const colorsSelected = ref([]);

    /**
     * Handles changes in color selection.
     * Adds or removes the color from the selected colors list.
     * Forces a re-render and filters products based on selected colors.
     * @param {String} color - The selected color
     */
    const handleColorChange = (color) => {
        if (colorsSelected.value.includes(color)) {
            colorsSelected.value = colorsSelected.value.filter(colorSelected => colorSelected !== color);
        } else {
            colorsSelected.value.push(color);
        }

        // Force a re-render of the price filter
        productStore.priceFilterForceRerender();

        // Filter products based on selected colors
        productStore.filterProducts({
            colorsSelected: colorsSelected.value,
            is_colorsFilter: true,
            lang: currentLanguage.value
        });
    };

    /**
     * Capitalizes the first letter of a given string.
     * @param {String} string - The string to capitalize
     * @returns {String} The capitalized string
     */
    const capitalizeFirstLetter = (string) => {
        return string.charAt(0).toUpperCase() + string.slice(1);
    };
</script>
