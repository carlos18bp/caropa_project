<template>
    <header class="bg-white">
        <div class="w-full grid grid-cols-3 px-8">
            <div class="pt-2 text-md font-famil-semibold text-black flex gap-6">
                <a @click="goTo('catalog')" class="cursor-pointer">Shop</a>
                <a  class="cursor-pointer"
                data-modal-toggle="contact_modal"
                data-modal-target="contact_modal"> 
                    Contact
                </a>
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
                <RouterLink :to="{ name: 'home' }" class="cursor-pointer">
                    <img class="h-full pt-2" src="@/assets/images/logo1.png" alt="Principal logo of Caropa Couture">
                </RouterLink>
            </div>
            <div class="pt-2 flex justify-end gap-6">
                <div>
                    <div class="flex items-center justify-center gap-3 cursor-pointer">
                        <MagnifyingGlassIcon class="text-black size-6"></MagnifyingGlassIcon>
                        <a class="text-md font-famil-semibold text-black">Search</a>
                    </div>
                </div>
                
                <div class="flex cursor-pointer">
                    <ShoppingBagIcon class="size-6 text-black" @click="toggleShoppingCart"/>
                    <span v-if="totalCartProducts > 0" 
                        class="bg-gray-400 text-white rounded-full text-xs w-6 h-6 flex items-center justify-center shadow-lg">
                        ({{ totalCartProducts }})
                    </span>
                </div>
                
                <ShoppingCart :shoppingCartToggle="shoppingCartToggle" 
                    @toggle-cart="toggleShoppingCart">
                </ShoppingCart>

                <div class="flex gap-3">
                    <a class="text-black font-famil-semibold text-md cursor-pointer">EN</a>
                    <span class="text-black font-semibold text-lg">|</span>
                    <a class="text-black font-famil-semibold text-md cursor-pointer">ES</a>
                </div>
            </div>
        </div>

        <div class="py-4 flex justify-center items-center gap-8">
            <a v-for="(category, index) in categories" :key="category.id"
                @click="filterProducts(category)" 
                class="inline-block font-famil-semibold text-lg uppercase hover:text-yellow-300 cursor-pointer"
                :class="{
                'text-primary': selectedCategory === category && route.name !== 'home',
                }">
                    {{ category }}
            </a>
        </div>
    </header>
</template>

<script setup>
    import ContactModel from "@/components/ContactModel.vue";
    import { computed, onMounted, ref } from 'vue';
    import { ShoppingBagIcon } from '@heroicons/vue/24/outline';
    import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline';
    import ShoppingCart from "@/components/product/ShoppingCart.vue";
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
    const shoppingCartToggle = ref(false);
    const totalCartProducts = computed(() => productStore.totalCartProducts);

    onMounted(async () => {
        await productStore.fetchProducts();
    })

    const goTo = (route) => {
        router.push({ name: route });
    };

    const toggleShoppingCart = () => {
        shoppingCartToggle.value = !shoppingCartToggle.value;
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
        productStore.filterProductsByCategory();        
    };
</script>