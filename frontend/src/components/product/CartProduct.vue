<template>
    <div class="flex justify-between items-center border-b pb-4 mb-4">
        <img :src="product.gallery_urls[0]" alt="Product Image" class="w-20 h-20 rounded" />
        <div class="flex-1 ml-4">
            <h3 class="font-semibold">
                <span v-if="currentLanguage === 'en'">{{ product.product_detail.name_en }}</span>
                <span v-else>{{ product.product_detail.name_es }}</span>
            </h3>
            <p class="text-sm text-gray-500">{{ product.color.name }}</p>
            <p class="text-sm">Qty {{ product.quantity }}</p>
        </div>
        <div class="text-right">
            <p class="text-lg font-semibold">${{ product.product_detail.price }}</p>
            <div class="space-x-8">
                <button @click="$emit('addProduct', product)" class="text-yellow-400 hover:underline">
                    Add
                </button>
                <button @click="$emit('removeProduct', product.id)" class="text-red-500 hover:underline">
                    Remove
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { useAppStore } from '@/stores/language.js';

    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const props = defineProps({
        product: Object,
    });
</script>