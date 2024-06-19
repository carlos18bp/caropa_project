<template>
    <!-- Shopping Cart Overlay -->
    <div class="w-full h-full inset-0 flex justify-end bg-gray-500 bg-opacity-40 backdrop-blur-md" v-if="shoppingCartToggle">
        <div @click="closeModal" class="absolute inset-0"></div>
        <div class="relative z-50 bg-white h-full w-full max-w-md shadow-lg flex flex-col">

            <!-- Cart Header -->
            <div class="flex justify-between items-center border-b p-4">
                <h2 class="text-xl font-semibold">Shopping cart</h2>
                <XMarkIcon @click="closeModal" class="h-6 w-6 cursor-pointer text-gray-500"></XMarkIcon>
            </div>

            <!-- Cart Items -->
            <div v-if="cartProducts.length" class="p-4 space-y-4 flex-1 overflow-y-auto">
                <CartProduct v-for="product in cartProducts" :key="product.id" :product="product"
                    @addProduct="addProduct" @removeProduct="removeProduct" />
            </div>
            <div v-else>
                <p class="p-4">No products in the cart</p>
            </div>

            <!-- Cart Footer -->
            <div v-if="cartProducts.length" class="border-t p-4">
                <div class="flex justify-between items-center mb-4">
                    <span class="text-lg font-semibold">Total</span>
                    <span class="text-lg font-semibold">$ {{ cartTotalPrice }}</span>
                </div>
                <router-link to="/checkout">
                    <button class="bg-yellow-400 text-white w-full py-2 rounded hover:bg-yellow-600">
                        Checkout
                    </button>
                </router-link>
                <div class="text-center mt-4">
                    <RouterLink :to="{ name: 'catalog' }" class="cursor-pointer text-yellow-400 hover:underline">
                        or Continue Shopping
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    // Importing necessary modules and components
    import { computed } from 'vue';
    import { XMarkIcon } from '@heroicons/vue/24/outline';
    import Swal from 'sweetalert2';
    
    import CartProduct from './CartProduct.vue';
    import { useProductStore } from "@/stores/product";

    // Initialize product store to access cart products and total price
    const productStore = useProductStore();
    const cartProducts = computed(() => productStore.cartProducts);
    const cartTotalPrice = computed(() => productStore.totalCartPrice);

    // Define props
    const props = defineProps({
        shoppingCartToggle: {
            type: Boolean,
            required: true
        }
    });

    // Define custom events
    const emit = defineEmits(["update:shoppingCartToggle"]);

    // Close the shopping cart modal
    const closeModal = () => {
        emit('update:shoppingCartToggle', false);
    };

    /**
     * Add a product to the cart
     * @param {Object} product - The product to add
     */
    const addProduct = (product) => {
        if ((product.quantity + 1) <= product.stock) {
            productStore.addProductToCart(product);
        } else {
            Swal.fire({
                title: "Sorry, we have no more units for this product",
                icon: "warning"
            });
        }
    };

    /**
     * Remove a product from the cart
     * @param {number} productId - The ID of the product to remove
     */
    const removeProduct = (productId) => {
        productStore.removeProductFromCart(productId);
    };
</script>
