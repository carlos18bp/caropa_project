<template>
    <div class="min-h-screen flex flex-col">
        <!-- Top Banner -->
        <div class="bg-black text-white p-2 text-center text-sm">
            {{ $t('free_shipping') }}
        </div>

        <!-- Header -->
        <header class="flex justify-between items-center p-6 bg-white shadow">
            <router-link :to="{ name: 'home' }">
                <img src="@/assets/images/logo2.png" alt="Caropa Couture Logo" class="h-14 cursor-pointer" />
            </router-link>
            <div class="flex items-center space-x-4">
                <div class="flex">
                    <ShoppingBagIcon class="size-5 text-black m-2 cursor-pointer" @click="toggleShoppingCart" />
                    <span v-if="totalCartProducts > 0"
                        class="bg-gray-300 text-white rounded-full text-xs size-5 flex items-center justify-center shadow-lg m-2 ml-0">
                        ({{ totalCartProducts }})
                    </span>
                </div>
                <div class="flex items-center space-x-2">
                    <span class="text-gray-700 text-sm font-bold">{{ $t('purchase_safety') }}</span>
                </div>
                <ShoppingCart :shoppingCartToggle="shoppingCartToggle" @toggle-cart="toggleShoppingCart" />
                <div class="flex items-center space-x-2 text-sm">
                    <span class="cursor-pointer font-bold"
                        :class="{ 'border-b-2 border-black border-current': currentLanguage === 'en' }"
                        @click="handleLanguage('en')">
                        EN
                    </span>
                    <span class="font-bold">|</span>
                    <span class="cursor-pointer font-bold"
                        :class="{ 'border-b-2 border-black border-current': currentLanguage === 'es' }"
                        @click="handleLanguage('es')">
                        ES
                    </span>
                </div>
            </div>
        </header>

        <!-- Main Content -->
        <div class="flex justify-center bg-gray-100">
            <div class="w-full bg-white rounded-lg shadow-lg flex flex-col lg:flex-row">
                <!-- Left Column -->
                <div class="w-full lg:w-1/2 p-5">
                    <h2 class="text-2xl font-bold mb-5">{{ $t('contact_information') }}</h2>
                    <form @submit.prevent="handleSubmit">
                        <div class="mb-5">
                            <label class="block text-gray-700 mb-2">{{ $t('email_address') }}</label>
                            <input type="email" v-model="form.email" class="w-full p-3 border rounded-lg" required />
                        </div>

                        <h2 class="text-2xl font-bold mb-5">{{ $t('payment_details') }}</h2>
                        <div class="mb-5">
                            <label class="block text-gray-700 mb-2">{{ $t('card_number') }}</label>
                            <input type="text" v-model="form.cardNumber" class="w-full p-3 border rounded-lg"
                                required />
                        </div>
                        <div class="mb-5 flex space-x-5">
                            <div class="w-1/2">
                                <label class="block text-gray-700 mb-2">{{ $t('expiration_date') }}</label>
                                <input type="text" v-model="form.expirationDate" class="w-full p-3 border rounded-lg"
                                    required />
                            </div>
                            <div class="w-1/2">
                                <label class="block text-gray-700 mb-2">CVC</label>
                                <input type="text" v-model="form.cvc" class="w-full p-3 border rounded-lg" required />
                            </div>
                        </div>

                        <h2 class="text-2xl font-bold mb-5">{{ $t('shipping_address') }}</h2>
                        <div class="mb-5">
                            <label class="block text-gray-700 mb-2">{{ $t('address') }}</label>
                            <input type="text" v-model="form.address" class="w-full p-3 border rounded-lg" required />
                        </div>
                        <div class="mb-5 flex space-x-5">
                            <div class="w-1/3">
                                <label class="block text-gray-700 mb-2">{{ $t('city') }}</label>
                                <input type="text" v-model="form.city" class="w-full p-3 border rounded-lg" required />
                            </div>
                            <div class="w-1/3">
                                <label class="block text-gray-700 mb-2">{{ $t('state_province') }}</label>
                                <input type="text" v-model="form.state" class="w-full p-3 border rounded-lg" required />
                            </div>
                            <div class="w-1/3">
                                <label class="block text-gray-700 mb-2">{{ $t('postal_code') }}</label>
                                <input type="text" v-model="form.postalCode" class="w-full p-3 border rounded-lg"
                                    required />
                            </div>
                        </div>

                        <div class="flex justify-end">
                            <button type="submit"
                                class="w-36 bg-yellow-500 text-white p-3 rounded-lg hover:bg-yellow-600">
                                {{ $t('pay_now') }}
                            </button>
                        </div>
                    </form>
                </div>

                <!-- Right Column -->
                <div
                    class="w-full lg:w-1/2 bg-gray-50 p-5 rounded-lg mt-10 lg:mt-0 lg:ml-10 border-l-2 border-t-2 border-yellow-400">
                    <h2 class="text-2xl font-bold mb-5">{{ $t('amount_due') }}</h2>
                    <div class="space-y-4 flex-1 overflow-y-auto">
                        <div v-for="product in cartProducts" :key="product.id"
                            class="flex justify-between items-center border-b pb-4 mb-4">
                            <!-- Product Image -->
                            <img :src="product.gallery_urls[0]" alt="Product Image" class="size-36 rounded" />
                            <div class="flex-1 ml-4 space-y-20">
                                <div>
                                    <!-- Product Title -->
                                    <h3 class="font-semibold" v-if="currentLanguage === 'en'">
                                        {{ product.product_detail.name }}
                                    </h3>
                                    <h3 class="font-semibold" v-else>{{ product.titulo }}</h3>
                                    <!-- Selected Color -->
                                    <p class="text-sm text-gray-500">{{ product.colorSelected }}</p>
                                </div>
                                <!-- Quantity -->
                                <p class="text-sm">Qty {{ product.quantity }}</p>
                            </div>
                            <div class="text-right mb-20">
                                <!-- Total Price -->
                                <p class="text-lg font-semibold">${{ product.product_detail.price * product.quantity }}
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="mt-10 space-y-2 border-t-2">
                        <div class="flex justify-between">
                            <span class="text-gray-700">Subtotal</span>
                            <span class="text-gray-700">$ {{ cartSubtotal }}</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-700">{{ $t('shipping') }}</span>
                            <span class="text-gray-700">$ {{ shippingCost }}</span>
                        </div>
                    </div>

                    <div class="mt-5 flex justify-between font-bold text-xl border-t-2">
                        <span>Total</span>
                        <span>$ {{ total }}</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="bg-black text-white p-2 text-center text-sm">
            © 2024 Caropa Couture. All rights reserved.
        </div>
    </div>
</template>

<script setup>
    import { computed, reactive, ref, watchEffect } from 'vue';
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from '@/stores/product';
    import ShoppingCart from "@/components/product/ShoppingCart.vue";
    import { ShoppingBagIcon } from '@heroicons/vue/24/outline';
    import enMessages from '@/locales/product/checkout/en.js';
    import esMessages from '@/locales/product/checkout/es.js';

    // Product store references
    const productStore = useProductStore();
    const cartProducts = computed(() => productStore.cartProducts);
    const cartSubtotal = ref(0);
    const shippingCost = ref(25.00); // Example shipping cost
    const total = computed(() => productStore.totalCartPrice + shippingCost.value);
    const totalCartProducts = computed(() => productStore.totalCartProducts);

    const shoppingCartToggle = ref(false);

    // Reactive references for language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages);

    // Translation function
    const $t = (key) => messages.value[key];

    // Form reference
    const form = reactive({
        email: '',
        cardNumber: '',
        expirationDate: '',
        cvc: '',
        address: '',
        city: '',
        state: '',
        postalCode: '',
        soldProducts: '',
    });

    watchEffect(() => {
        messages.value = currentLanguage.value === 'en' ? enMessages : esMessages;
    });

    /**
     * Handle form submission
     */
    const handleSubmit = () => {
        form.soldProducts = extractProductInfo(cartProducts.value);
        productStore.createSale(form);
        localStorage.removeItem('cartProducts');
        productStore.cartProducts = [];
    }

    /**
     * Extract specific fields from a list of products.
     * 
     * @param {Array} products - The list of products to process. 
     * @returns {Array} A new array of objects, where each object contains only the properties of each product.
     */
    const extractProductInfo = (products) => {
        return products.map(product => ({
            product_id: product.id,
            color_selected: product.color.name,
            quantity: product.quantity,
        }));
    };

    /**
     * Toggle shopping cart visibility
     */
    const toggleShoppingCart = () => {
        shoppingCartToggle.value = !shoppingCartToggle.value;
    }

    /**
     * Handle language change
     * @param {string} lang - Language to set
     */
    const handleLanguage = (lang) => {
        appStore.setCurrentLanguage(lang);
    }
</script>

<style scoped>
    body {
        font-family: 'Arial', sans-serif;
    }
</style>