<template>
    <div class="">
        <Banner></Banner>
        <header class="bg-white h-12 flex px-8 py-2 w-full">
            <div class="inline-block">
                <div class="flex gap-3 items-center">
                    <a class="text-black font-famil-semibold text-md cursor-pointer flex items-center"><span>EN</span></a>
                    <span class="text-black font-semibold text-lg">|</span>
                    <a class="text-black font-famil-semibold text-md cursor-pointer flex items-center"><span>ES</span></a>
                </div>
            </div>
            <div class="grow flex justify-center items-center gap-8">
                <a v-for="category in categories" :key="category.id"
                    @click="filterProducts(category)" 
                    class="inline-block font-famil-semibold text-lg uppercase"
                    :class="{
                    'text-primary': selectedCategory === category, 
                    'hover:text-yellow-300': selectedCategory !== category, 
                    'cursor-pointer': true
                    }">
                        {{ category }}
                </a>
            </div>
            <div class="flex items-center justify-end gap-6">
                <MagnifyingGlassIcon class="text-black size-6 cursor-pointer"></MagnifyingGlassIcon>
                <ShoppingBagIcon class="text-black size-6 cursor-pointer"></ShoppingBagIcon>
            </div>
        </header>
    </div>
</template>

<script setup>
    import { computed, onMounted, ref } from 'vue';
    import Banner from '@/components/layouts/Banner.vue'
    import { ShoppingBagIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline';
    import { useProductStore } from "@/stores/product";
    import { useRouter, useRoute } from 'vue-router';  

    const productStore = useProductStore();
    const categories = computed(() => productStore.primaryCategories);
    /**
     * Router instance
     */
    const router = useRouter();
    const route = useRoute();

    const selectedCategory = computed(() => productStore.primaryCategorySeleted);

    onMounted(async () => {
        await productStore.fetchProducts();
    });

    /**
     * Filters products based on selected category
     * @param {String} category - The selected category
     */
     const filterProducts = (category) => {
        if (route.name !== 'catalog') {
            router.push({ name: 'catalog' });
        }
        productStore.primaryCategorySeleted = category;
        productStore.filterProductsByCategory();        
    };
</script>
