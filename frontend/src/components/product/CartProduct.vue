<template>
    <div v-if="product" class="flex border-b pb-4 h-40 mb-4">
        <!-- Product Image -->
        <img :src="product.gallery_urls[0]" alt="Product Image" class="w-40 h-full rounded" />
        <div class="h-full relative flex-1 pl-4">

            <!-- Product Title -->
            <h3 class="font-semibold text-xl" v-if="currentLanguage === 'en'">
                {{ product.product_detail.name_en }}
            </h3>
            <h3 class="font-semibold text-xl" v-else>{{ product.product_detail.name_es }}</h3>
            <!-- Selected Color -->
            <p class="text-md font-medium text-gray-500">
                {{ product.color.name }}
            </p>

            <!-- Quantity -->
            <p class="text-md text-gray-500 font-medium absolute bottom-0">
                Qty {{ product.quantity }}
            </p>
        </div>
        <div class="text-right h-full grid">
            <!-- Total Price -->
            <p class="text-xl font-semibold">${{ product.product_detail.price * product.quantity }}</p>
            <div class="grid grid-cols-2 items-end text-md font-medium">
                <!-- Add Product Button -->
                <button @click="$emit('addProduct', product)" 
                    class="text-primary hover:underline">
                    Add
                </button>
                <!-- Remove Product Button -->
                <button @click="$emit('removeProduct', product.id)" 
                    class="text-gray-500 hover:underline">
                    Remove
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
    // Importing necessary modules
    import { computed } from 'vue';
    import { useAppStore } from '@/stores/language.js';

    // Initializing app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);

    // Defining component props
    const props = defineProps({
        product: Object,
    });
    console.log(props.product)
</script>
