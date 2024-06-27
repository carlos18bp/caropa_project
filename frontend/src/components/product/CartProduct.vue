<template>
    <div v-if="product" class="flex border-b pb-4 h-40 mb-4">
        <!-- Product Image -->
        <img :src="product.gallery_urls[0]" alt="Product Image" class="w-20 h-20 lg:w-40 lg:h-full rounded" />
        <div class="h-full relative grid flex-1 pl-4">
            <div class="flex justify-between">
                <div>
                    <!-- Product Title -->
                    <h3 class="font-semibold text-xl" v-if="currentLanguage === 'en'">
                        {{ product.product_detail.name_en }}
                    </h3>
                    <h3 class="font-semibold text-xl" v-else>{{ product.product_detail.name_es }}</h3>
                    <!-- Selected Color -->
                    <p class="text-md font-medium text-gray-500">
                        {{ product.color.name }}
                    </p>
                </div>
                <!-- Total Price -->
                <p class="text-xl font-semibold">${{ product.product_detail.price * product.quantity }}</p>
            </div>
            <div class="flex justify-between items-end">
                <!-- Quantity -->
                <p class="text-md text-gray-500 font-medium">
                    Qty {{ product.quantity }}
                </p>
                <div class="flex gap-2">
                    <!-- Add Product Button -->
                    <button @click="$emit('addProduct', product)" 
                        class="text-primary hover:underline test-shoppingCart-cartProduct-add">
                        {{ $t('shoppingCart').cartProduct.add }}
                    </button>
                    <!-- Remove Product Button -->
                    <button @click="$emit('removeProduct', product.id)" 
                        class="text-gray-500 hover:underline test-shoppingCart-cartProduct-remove">
                        {{ $t('shoppingCart').cartProduct.remove }}
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    // Importing necessary modules
    import { computed, ref, watchEffect } from 'vue';
    import { useAppStore } from '@/stores/language.js';
    import enMessages from "@/locales/layouts/header/en";
    import esMessages from "@/locales/layouts/header/es";
    

    // Initializing app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages)

    // Defining component props
    const props = defineProps({
        product: Object,
    });

    // Translation function
    const $t = (key) => messages.value[key];

    // Change messages in function to currently language
    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });
</script>
