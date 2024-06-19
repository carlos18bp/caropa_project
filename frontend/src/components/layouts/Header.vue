<template>
    <!-- Banner component -->
    <Banner></Banner>

    <!-- Main header -->
    <header ref="header" class="bg-white">
        <div class="w-full grid grid-cols-3 px-8">
            <div class="pt-2 text-md font-famil-semibold text-black flex gap-6">
                <!-- Navigation links -->
                <a @click="goTo('catalog')" class="cursor-pointer">Shop</a>
                <a class="cursor-pointer" data-modal-toggle="contact_modal" data-modal-target="contact_modal">
                    Contact
                </a>
                <!-- Contact modal component -->
                <ContactModel></ContactModel>
                <a @click="goTo('about_us')" class="cursor-pointer">About</a>
                <div>
                    <div class="flex items-center gap-1 cursor-pointer">
                        Blue Mom
                        <div>
                            <img src="@/assets/images/icons/heart.png" alt="Icon blue heart">
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex items-center justify-center">
                <!-- Home link with logo -->
                <RouterLink :to="{ name: 'home' }" class="cursor-pointer">
                    <img class="h-full pt-2" src="@/assets/images/logo1.png" alt="Principal logo of Caropa Couture">
                </RouterLink>
            </div>
            <div class="pt-2 flex justify-end gap-6">
                <!-- Search bar trigger -->
                <div>
                    <div @click="showSearchBar = true" class="flex items-center justify-center gap-3 cursor-pointer">
                        <MagnifyingGlassIcon class="text-black size-6"></MagnifyingGlassIcon>
                        <a class="text-md font-famil-semibold text-black">Search</a>
                    </div>
                </div>

                <!-- Shopping cart icon -->
                <div class="relative cursor-pointer">
                    <ShoppingBagIcon class="size-6 text-black" @click="shoppingCartToggle = true" />
                    <span @click="shoppingCartToggle = true" v-if="totalCartProducts > 0"
                        class="absolute top-0 left-1/2 font-regular bg-primary text-white rounded-full text-xxs w-4 h-4 flex items-center justify-center shadow-lg">
                        {{ totalCartProducts }}
                    </span>
                </div>

                <!-- Language switcher -->
                <div class="flex gap-3">
                    <a class="text-black font-famil-semibold text-md cursor-pointer" @click="handleLanguage('en')">
                        <span :class="{ 'border-b-2 border-black border-current': currentLanguage === 'en' }">EN</span>
                    </a>
                    <span class="text-black font-semibold text-lg">|</span>
                    <a class="text-black font-famil-semibold text-md cursor-pointer" @click="handleLanguage('es')">
                        <span :class="{ 'border-b-2 border-black border-current': currentLanguage === 'es' }">ES</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Categories navigation -->
        <div class="py-4 flex justify-center items-center gap-8">
            <a v-for="(category, index) in categories" :key="category.id" @click="filterProducts(category)"
                class="inline-block font-famil-semibold text-lg uppercase hover:text-yellow-300 cursor-pointer"
                :class="{ 'text-primary': selectedCategory === category && route.name !== 'home' }">
                {{ category }}
            </a>
        </div>
    </header>

    <!-- Short header for scroll effect -->
    <div ref="headerShort" class="fixed top-0 left-0 z-20 opacity-0">
        <HeaderShort></HeaderShort>
    </div>

    <!-- Search bar component -->
    <div v-if="showSearchBar" class="fixed z-30 top-0">
        <SearchBar :visible="showSearchBar" @update:visible="showSearchBar = $event"></SearchBar>
    </div>

    <!-- Shopping cart component -->
    <div v-if="shoppingCartToggle" class="fixed z-30 w-full h-screen top-0">
        <ShoppingCart :shoppingCartToggle="shoppingCartToggle" @update:shoppingCartToggle="shoppingCartToggle = $event">
        </ShoppingCart>
    </div>
</template>

<script setup>
    // Importing necessary modules and components
    import { computed, onMounted, ref } from 'vue';
    import { MagnifyingGlassIcon, ShoppingBagIcon } from '@heroicons/vue/24/outline';
    import { useRouter, useRoute } from 'vue-router';
    import { gsap } from 'gsap';
    import { ScrollTrigger } from 'gsap/ScrollTrigger';

    import Banner from "@/components/layouts/Banner.vue";
    import ContactModel from "@/components/ContactModel.vue";
    import HeaderShort from "./HeaderShort.vue";
    import SearchBar from "@/components/layouts/SearchBar.vue";
    import ShoppingCart from "@/components/product/ShoppingCart.vue";
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";

    gsap.registerPlugin(ScrollTrigger);

    // References to DOM elements
    const header = ref(null);
    const headerShort = ref(null);
    const showSearchBar = ref(false);

    // Initialize app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);

    // Initialize product store to access products and categories
    const productStore = useProductStore();
    const categories = computed(() => productStore.primaryCategories(currentLanguage.value));

    // Router instance
    const router = useRouter();
    const route = useRoute();

    // Computed properties
    const selectedCategory = computed(() => productStore.primaryCategorySeleted);
    const shoppingCartToggle = ref(false);
    const totalCartProducts = computed(() => productStore.totalCartProducts);

    // Fetch products when component is mounted and setup scroll animation
    onMounted(async () => {
        await productStore.fetchProducts();
        gsap.fromTo(headerShort.value,
            {
                opacity: 0,
                y: -100
            },
            {
                y: 0,
                opacity: 1,
                duration: 1,
                ease: 'power2.inOut',
                scrollTrigger: {
                    trigger: header.value,
                    start: 'bottom top',
                    toggleActions: 'play none reverse none',
                },
            });
    });

    /**
     * Handle language change
     * @param {string} lang - Language to set
     */
    const handleLanguage = (lang) => {
        appStore.setCurrentLanguage(lang);
    };

    /**
     * Navigate to a different route
     * @param {string} route - The name of the route to navigate to
     */
    const goTo = (route) => {
        router.push({ name: route });
    };

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
