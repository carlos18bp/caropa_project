<template>
    <div class="flex flex-col bg-white">
        <Banner></Banner>
        <!-- Header -->
        <header class="flex justify-between items-center px-8 py-4">
            <router-link :to="{ name: 'home' }" class="flex items-center">
                <img src="@/assets/images/logo2.png" alt="Caropa Couture Logo" class="h-12 cursor-pointer" />
            </router-link>

            <div class="flex items-center space-x-4">
                <LockClosedIcon class="text-black_p w-6 h-6 hidden lg:block"></LockClosedIcon>
                <div class="items-center space-x-2 hidden lg:flex">
                    <span class="text-black_p text-lg font-bold">{{
                $t("purchase_safety")
            }}</span>
                </div>
                <div class="flex items-center space-x-2 text-lg">
                    <span class="cursor-pointer font-bold" @click="handleLanguage('en')">
                        EN
                    </span>
                    <span class="font-bold">|</span>
                    <span class="cursor-pointer font-bold" @click="handleLanguage('es')"> ES </span>
                </div>
            </div>
        </header>

        <!-- Main Content -->
        <div class="w-full grid lg:grid-cols-2">
            <!-- Left Column -->
            <div class="relative w-full order-2 lg:order-1">
                <form @submit.prevent="handleSubmit" class="sticky top-0 py-8 px-8">
                    <h2 class="text-2xl font-semibold">
                        {{ $t("contact_information") }}
                    </h2>
                    <div class="mt-4">
                        <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                $t("email_address")
            }}</label>
                        <input type="email" v-model="form.email"
                            class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                            required />
                    </div>

                    <h2 class="text-2xl font-semibold mt-6">
                        {{ $t("payment_details") }}
                    </h2>
                    <div class="mt-4">
                        <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                $t("card_number")
            }}</label>
                        <input type="text" v-model="form.cardNumber"
                            class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                            required />
                    </div>
                    <div class="mt-4 grid grid-cols-4 gap-4">
                        <div class="col-span-4 md:col-span-3">
                            <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                                $t("expiration_date")
                            }}</label>
                            <input type="text" v-model="form.expirationDate"
                                class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                                required />
                        </div>
                        <div class="col-span-4 md:col-span-1">
                            <label class="block text-gray-500 mb-2 font-semibold text-md">CVC</label>
                            <input type="text" v-model="form.cvc"
                                class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                                required />
                        </div>
                    </div>

                    <h2 class="text-2xl font-semibold mt-6">
                        {{ $t("shipping_address") }}
                    </h2>
                    <div class="mt-4">
                        <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                $t("address")
            }}</label>
                        <input type="text" v-model="form.address"
                            class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                            required />
                    </div>
                    <div class="mt-4 lg:grid lg:grid-cols-3 lg:gap-4">
                        <div class="">
                            <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                $t("city")
            }}</label>
                            <input type="text" v-model="form.city"
                                class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                                required />
                        </div>
                        <div class="">
                            <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                $t("state_province")
            }}</label>
                            <input type="text" v-model="form.state"
                                class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                                required />
                        </div>
                        <div class="">
                            <label class="block text-gray-500 mb-2 font-semibold text-md">{{
                $t("postal_code")
            }}</label>
                            <input type="text" v-model="form.postalCode"
                                class="w-full p-3 font-regular border border-gray-500 rounded-lg bg-transparent focus:ring-0 focus:ring-transparent focus:outline-none focus:border-black_p"
                                required />
                        </div>
                    </div>

                    <div class="flex justify-end mt-6">
                        <button type="submit"
                            class="w-36 bg-primary text-white p-3 rounded-lg hover:bg-primary_p font-semibold text-md tracking-wider">
                            {{ $t("pay_now") }}
                        </button>
                    </div>
                </form>
            </div>

            <!-- Right Column -->
            <div class="w-full border-t-2 border-t-primary border-b-2 border-b-primary px-8 py-8 order-1 lg:order-2 lg:border-l-2 lg:border-l-primary lg:border-b-0">
                <h2 class="text-xl font-semibold text-gray-500">
                    {{ $t("amount_due") }}
                </h2>
                <h2 class="font-semibold text-3xl text-black -mt-1">
                    $ {{ productStore.totalCartPrice }}
                </h2>
                <div class="mt-8 divide-y-2 divide-brown overflow-auto lg:ps-12">
                    <div v-for="product in cartProducts" :key="product.id"
                        class="flex items-center justify-between h-40 py-4 box-content">
                        <!-- Product Image -->
                        <img :src="product.gallery_urls[0]" alt="Product Image" class="w-24 h-24 rounded lg:w-40 lg:h-full" />
                        <div class="h-full relative flex-1 pl-4">
                            <div>
                                <!-- Product Title -->
                                <h3 class="font-semibold text-xl text-black" v-if="currentLanguage === 'en'">
                                    {{ product.product_detail.name_en }}
                                </h3>
                                <h3 class="font-semibold text-xl text-black" v-else>
                                    {{ product.product_detail.name_es }}
                                </h3>
                                <!-- Selected Color -->
                                <p class="text-md font-semibold text-gray-500">
                                    {{ product.color.name }}
                                </p>
                            </div>
                            <!-- Quantity -->
                            <p class="absolute bottom-0 text-md font-semibold text-gray-500">
                                Qty {{ product.quantity }}
                            </p>
                        </div>
                        <div class="text-right relative h-full grid">
                            <!-- Total Price -->
                            <p class="text-xl font-semibold text-black">
                                ${{ product.product_detail.price * product.quantity }}
                            </p>
                            <!-- Remove Product Button -->
                            <div class="flex items-end">
                                <a @click="removeProduct(product.id)"
                                    class="text-black font-semibold text-lg cursor-pointer">
                                    {{ $t("remove") }}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="mt-10 border-t-2 border-t-brown">
                    <div class="flex justify-between mt-4">
                        <span class="text-gray-500 font-semibold text-2xl">Subtotal</span>
                        <span class="text-gray-500 font-semibold text-2xl">$ {{ productStore.totalCartPrice }}</span>
                    </div>
                    <div class="flex justify-between mt-4">
                        <span class="text-gray-500 font-semibold text-2xl">{{
                            $t("shipping")
                            }}</span>
                        <span class="text-gray-500 font-semibold text-2xl">$ {{ shippingCost }}</span>
                    </div>
                    <div class="flex justify-between mt-4">
                        <span class="text-gray-500 font-semibold text-2xl">{{
                            $t("taxes")
                            }}</span>
                        <span class="text-gray-500 font-semibold text-2xl">$ {{ taxes }}</span>
                    </div>
                </div>

                <div class="mt-4 border-t-2 border-brown">
                    <div class="mt-4 flex justify-between font-semibold text-2xl">
                        <span class="text-black">Total</span>
                        <span class="text-black">$ {{ total }}</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="bg-black text-white p-4 text-start text-lg font-medium">
            © 2024 Caropa Couture. All rights reserved.
        </div>
    </div>
</template>

<script setup>
    import { computed, reactive, ref, watchEffect, onMounted } from "vue";
    import Banner from "@/components/layouts/Banner.vue";
    import { LockClosedIcon } from "@heroicons/vue/24/outline";
    import { useAppStore } from "@/stores/language.js";
    import { useProductStore } from "@/stores/product";
    import enMessages from "@/locales/product/checkout/en.js";
    import esMessages from "@/locales/product/checkout/es.js";
    import Swal from 'sweetalert2';
    import { useRouter } from 'vue-router';

    // Product store references
    const productStore = useProductStore();
    const cartProducts = computed(() => productStore.cartProducts);
    const shippingCost = ref(25.0);
    const taxes = ref(30.0);
    const total = computed(
        () => productStore.totalCartPrice + shippingCost.value + taxes.value
    );

    // Reactive references for language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages);

    // Translation function
    const $t = (key) => messages.value[key];

    const router = useRouter();

    // Form reference
    const form = reactive({
        email: "",
        cardNumber: "",
        expirationDate: "",
        cvc: "",
        address: "",
        city: "",
        state: "",
        postalCode: "",
        soldProducts: "",
    });

    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });

    // It's necesary to activate overflow after Shopping Cart component
    onMounted(() => {
        document.body.style.overflow = 'auto'
    })

    /**
     * Handle form submission
     */
    const handleSubmit = () => {
        form.soldProducts = extractProductInfo(cartProducts.value);
        productStore.createSale(form);

        localStorage.removeItem("cartProducts");
        productStore.cartProducts = [];

        Swal.fire({
            title: "The payment has been processed successfully",
            icon: "success"
        });

        router.push({ name: "home" });
    };

    /**
     * Handle language change
     * @param {string} lang - Language to set
     */
    const handleLanguage = (lang) => {
        appStore.setCurrentLanguage(lang);
    };

    /**
     * Extract specific fields from a list of products.
     *
     * @param {Array} products - The list of products to process.
     * @returns {Array} A new array of objects, where each object contains only the properties of each product.
     */
    const extractProductInfo = (products) => {
        return products.map((product) => ({
            product_id: product.id,
            color_selected: product.color_selected,
            quantity: product.quantity,
        }));
    };

    /**
     * Remove product from cart
     * @param {Number} productId - The ID of the product to remove
     */
    const removeProduct = (productId) => {
        productStore.removeProductFromCart(productId);
    };
</script>