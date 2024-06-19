<template>
    <div>
        <Banner></Banner>
        <header class="bg-white h-16 flex items-center px-8 py-2 w-full">
            <div class="inline-block">
                <div class="flex gap-3 items-center">
                    <a
                        class="text-black font-famil-semibold text-md cursor-pointer flex items-center"><span>EN</span></a>
                    <span class="text-black font-semibold text-lg">|</span>
                    <a
                        class="text-black font-famil-semibold text-md cursor-pointer flex items-center"><span>ES</span></a>
                </div>
            </div>
            <div class="grow flex justify-evenly items-center">
                <div v-for="category in categories.slice(0, 5)" :key="category.id" @click="filterProducts(category)"
                    class="flex-1 flex justify-center items-center">
                    <a class="inline-block font-famil-semibold text-lg uppercase text-center" :class="{
                    'text-primary': selectedCategory === category,
                    'hover:text-yellow-300': selectedCategory !== category,
                    'cursor-pointer': true
                }">
                        {{ category }}
                    </a>
                </div>
                <div class="flex-1 flex justify-center items-center">
                    <img src="@/assets/images/logo2.png" alt="Secondary logo of Caropa Couture" class="h-full">
                </div>
                <div v-for="category in categories.slice(5, 10)" :key="category.id" @click="filterProducts(category)"
                    class="flex-1 flex justify-center items-center">
                    <a class="inline-block font-famil-semibold text-lg uppercase text-center" :class="{
                    'text-primary': selectedCategory === category,
                    'hover:text-yellow-300': selectedCategory !== category,
                    'cursor-pointer': true
                }">
                        {{ category }}
                    </a>
                </div>
            </div>
            <div class="flex items-center justify-end gap-6">
                <MagnifyingGlassIcon @click="showSearchBar = true" class="text-black size-6 cursor-pointer">
                </MagnifyingGlassIcon>
                <div class="relative cursor-pointer">
                    <ShoppingBagIcon class="size-6 text-black" @click="shoppingCartToggle = true" />
                    <span @click="shoppingCartToggle = true" v-if="totalCartProducts > 0"
                        class="absolute top-0 left-1/2 font-regular bg-primary text-white rounded-full text-xxs w-4 h-4 flex items-center justify-center shadow-lg">
                        {{ totalCartProducts }}
                    </span>
                </div>
            </div>
        </header>
    </div>
    <div class="fixed z-30 top-0">
        <SearchBar :visible="showSearchBar" @update:visible="showSearchBar = $event"></SearchBar>
    </div>
    <div v-if="shoppingCartToggle" class="fixed z-30 w-full h-screen top-0">
        <ShoppingCart :shoppingCartToggle="shoppingCartToggle" @update:shoppingCartToggle="shoppingCartToggle = $event">
        </ShoppingCart>
    </div>
</template>

<script setup>
    import { computed, onMounted, ref } from 'vue';
    import SearchBar from './SearchBar.vue';
    import Banner from '@/components/layouts/Banner.vue'
    import ShoppingCart from "@/components/product/ShoppingCart.vue";
    import { ShoppingBagIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline';
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";
    import { useRouter, useRoute } from 'vue-router';

    const showSearchBar = ref(false);

    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const productStore = useProductStore();
    const categories = computed(() => productStore.primaryCategories(currentLanguage.value));
    /**
     * Router instance
     */
    const router = useRouter();
    const route = useRoute();

    const selectedCategory = computed(() => productStore.primaryCategorySeleted);
    const shoppingCartToggle = ref(false);
    const totalCartProducts = computed(() => productStore.totalCartProducts);

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
        productStore.filterProductsByCategory(currentLanguage.value);
    };
</script>
