<template>
    <!-- Modal overlay -->
    <div v-if="visible" class="w-screen h-screen bg-gray-500 bg-opacity-40 backdrop-blur-md">
        <!-- Close modal when clicking outside the modal content -->
        <div @click="closeModal" class="absolute inset-0"></div>
        <!-- Modal content -->
        <div class="relative z-50 bg-white shadow-lg w-full p-6">
            <!-- Modal header with search input -->
            <div class="flex items-center justify-between border-b pb-4">
                <input type="text"
                    class="w-full p-2 text-lg border-transparent focus:border-none focus:ring-0 focus:outline-none font-semibold"
                    placeholder="Search..." v-model="searchQuery" @input="onSearch(searchQuery)" />
                <XMarkIcon @click="closeModal" class="h-6 w-6 cursor-pointer me-6 text-gray-500"></XMarkIcon>
            </div>
            <!-- Modal body with search results -->
            <div class="mt-4">
                <div class="grid grid-cols-3 gap-4">
                    <!-- Suggestion items -->
                    <RouterLink v-if="products" :to="{ name: 'product', params: { product_ref: product.ref } }"
                        v-for="product in products" :key="product.id" @click.native="closeModal"
                        class="flex items-center">
                        <img :src="product.gallery_urls[0]" alt="Product image"
                            class="w-16 h-16 object-cover rounded" />
                        <div class="ml-4">
                            <p class="text-lg font-bold">
                                <span v-if="currentLanguage === 'en'">{{ product.product_detail.name_en }}</span>
                                <span v-else>{{ product.product_detail.name_es }}</span>
                            </p>
                            <p class="text-sm text-gray-600">Ref: {{ product.ref }}</p>
                        </div>
                    </RouterLink>
                </div>
                <!-- Link to see all products -->
                <div class="mt-4 text-right">
                    <RouterLink :to="{ name: 'catalog' }" @click="closeModal" class="font-medium me-6">See all products
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { computed, ref, onMounted } from "vue";
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";
    import { XMarkIcon } from "@heroicons/vue/24/outline";

    // Define component props and events
    const props = defineProps({
        visible: Boolean,
    });
    const emit = defineEmits(["update:visible"]);

    // Store instances and reactive variables
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();
    const products = ref([]);
    const searchQuery = ref(null);

    // Close modal function
    const closeModal = () => {
        emit("update:visible", false);
        products.value = [];
        searchQuery.value = null;
    };

    // Search function to filter products by name
    const onSearch = (name) => {
        if (name !== "") {
            products.value = productStore.productsByName(name, currentLanguage.value);
        }
    };

    // Fetch products when the component is mounted
    onMounted(async () => {
        await productStore.fetchProducts();
    });
</script>
