<template>
  <!-- Shopping Cart Overlay -->
  <div 
  class="w-full h-full inset-0 flex justify-end bg-gray-500 bg-opacity-40 backdrop-blur-md"
  v-if="shoppingCartToggle">
    <div @click="closeModal" class="absolute inset-0"></div>
    <div class="relative z-50 bg-white h-full w-full max-w-md shadow-lg flex flex-col">
      
      <!-- Cart Header -->
      <div class="flex justify-between items-center border-b p-4">
        <h2 class="text-xl font-semibold">Shopping cart</h2>
        <XMarkIcon @click="closeModal" class="h-6 w-6 cursor-pointer text-gray-500"></XMarkIcon>
      </div>
      
      <!-- Cart Items -->
      <div v-if="cartProduct.length" class="p-4 space-y-4 flex-1 overflow-y-auto">
        <CartProduct
          v-for="product in cartProduct"
          :key="product.id"
          :product="product"
          @addProduct="addProduct"
          @removeProduct="removeProduct"
        />
      </div>
      <div v-else>
        <p class="p-4">No products on the cart</p>
      </div>
      
      <!-- Cart Footer -->
      <div v-if="cartProduct.length" class="border-t p-4">
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
  import CartProduct from './CartProduct.vue';
  import { computed } from 'vue';
  import { useProductStore } from "@/stores/product";
  import { XMarkIcon } from '@heroicons/vue/24/outline';

  const productStore = useProductStore();
  const cartProduct = computed(() => productStore.cartProducts);
  const cartTotalPrice = computed(() => productStore.totalCartPrice);

  const props = defineProps({
    shoppingCartToggle: {
      type: Boolean,
      required: true
    }
  });
  const emit = defineEmits(["update:shoppingCartToggle"]);

  const closeModal = () => {
    emit('update:shoppingCartToggle', false);
  }

  const addProduct = (product) => {
    productStore.addProductToCart(product);
  };
  
  const removeProduct = (productId) => {
    productStore.removeProductFromCart(productId)
  };
</script>
  