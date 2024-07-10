<template>
    <!-- Shopping Cart Overlay -->
    <div class="fixed inset-0 flex justify-end z-50" v-if="visible">
        <div ref="background" 
            @click="closeCart()" 
            class="absolute inset-0 bg-gray-500 bg-opacity-40 backdrop-blur-md">
        </div>
        <div ref="cart" class="relative bg-white h-full w-full shadow-lg flex flex-col z-60 lg:w-2/5">
            <!-- Cart Header -->
            <div class="flex justify-between items-center p-10">
                <h2 class="text-2xl font-famil-semibold">{{ $t('shoppingCart').shoppingCart }}</h2>
                <XMarkIcon @click="closeCart()" class="text-gray-500 cursor-pointer w-6 h-6">
                </XMarkIcon>
            </div>

            <!-- Cart Items -->
            <div v-if="cartProduct.length" class="p-10 space-y-4 flex-1 overflow-y-auto">
                <CartProduct v-for="product in cartProduct" 
                    :key="product.id" 
                    :product="product"
                    @addProduct="addProduct(product)" 
                    @removeProduct="removeProduct(product)" />
            </div>
            <div v-else class="text-lg font-regular ps-10">
                <p>{{ $t('shoppingCart').noProducts }}</p>
                <RouterLink :to="{ name: 'catalog' }" class="cursor-pointer">
                    <span class="text-primary test-shoppingCart-continueShopping">
                        {{ $t('shoppingCart').continueShopping }}
                    </span>
                </RouterLink>
            </div>

            <!-- Cart Footer -->
            <div v-if="cartProduct.length" class="border-t p-4">
                <div class="flex justify-between items-center mb-4">
                    <div>
                        <h3 class="text-2xl font-semibold">Subtotal</h3>
                        <p class="text-md text-gray-500 font-medium test-shoppingCart-shipping">
                            {{ $t('shoppingCart').shipping }}
                        </p>
                    </div>
                    <span class="text-xl font-semibold">${{ cartTotalPrice }}</span>
                </div>
                <router-link to="/checkout">
                    <button
                        class="bg-primary text-white w-full mt-4 py-2 rounded-lg hover:bg-terciary font-medium text-xl tracking-wide test-shoppingCart-checkout">
                        {{ $t('shoppingCart').checkout }}
                    </button>
                </router-link>
                <div class="text-center mt-4 font-regular text-lg">
                    <RouterLink :to="{ name: 'catalog' }" class="cursor-pointer">
                        <span class="text-black test-shoppingCart-or">{{ $t('shoppingCart').or }}</span> <span class="text-primary test.shoppingCart-continueShopping">{{ $t('shoppingCart').continueShopping }}</span>
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { computed, ref, watchEffect } from "vue";
    import CartProduct from "./CartProduct.vue";
    import { gsap } from "gsap";
    import { XMarkIcon } from "@heroicons/vue/24/outline";
    import { useProductStore } from "@/stores/product";
    import Swal from 'sweetalert2';
    import { useAppStore } from '@/stores/language.js';
    import enMessages from "@/locales/layouts/header/en";
    import esMessages from "@/locales/layouts/header/es";

    // Create references for Background and Cart Elements
    const background = ref(null);
    const cart = ref(null);
    const messages = ref(enMessages)

    // Initialize app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);

    // Product store references
    const productStore = useProductStore();
    const cartProduct = computed(() => productStore.cartProducts);
    const cartTotalPrice = computed(() => productStore.totalCartPrice);

    // Props definition
    const props = defineProps({
        visible: {
            type: Boolean,
            required: true,
        },
    });
    const emit = defineEmits(["update:visible"]);

    // Translation function
    const $t = (key) => messages.value[key];

    // Watch for changes in the state of shoppingCartToggle and change messages in function to currently language
    watchEffect(() => {
        
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;

        if (props.visible) {
            document.body.style.overflow = "hidden";
            if (background.value) {
                gsap.fromTo(
                    background.value,
                    {
                        opacity: 0,
                    },
                    {
                        opacity: 1,
                        duration: 1,
                        ease: "power2.inOut",
                    }
                );
            }
            if (cart.value) {
                gsap.fromTo(
                    cart.value,
                    {
                        x: cart.value.offsetWidth,
                    },
                    {
                        x: 0,
                        duration: 1,
                        ease: "power2.inOut",
                    }
                );
            }
        } else {
            document.body.style.overflow = "auto";
        }
    });

    const closeCart = () => {
        // Create the animations like a promises
        const cartAnimation = gsap
            .fromTo(
                cart.value,
                {
                    x: 0,
                },
                {
                    x: cart.value.offsetWidth,
                    duration: 1,
                    ease: "power2.inOut",
                }
            )
            .then();

        const backgroundAnimation = gsap
            .fromTo(
                background.value,
                {
                    opacity: 1,
                },
                {
                    opacity: 0,
                    duration: 1,
                    ease: "power2.inOut",
                }
            )
            .then();

        // Wait while both are finished
        Promise.all([cartAnimation, backgroundAnimation]).then(() => {
            document.body.style.overflow = "auto";
            emit("update:visible", false);
        });
    };

    /**
     * Add product to cart
     * @param {Object} product - The product to add
     */
    const addProduct = (product) => {
        if ((product.quantity + 1) <= product.stock) {
            productStore.addProductToCart(product, product.colorSelected);
        } else {
            Swal.fire({
                title: "Sorry, we have no more units for this product",
                icon: "warning"
            });
        }
    };

    /**
     * Remove product from cart
     * @param {Number} productId - The ID of the product to remove
     */
    const removeProduct = (product) => {
        productStore.removeProductFromCart(product);
    };
</script>