<template>
  <!-- Shopping Cart Overlay -->
  <div class="fixed inset-0 flex justify-end bg-black bg-opacity-50 z-50"
    v-show="shoppingCartToggle">
    <div class="bg-white h-full w-full max-w-md shadow-lg flex flex-col">
      
      <!-- Cart Header -->
      <div class="flex justify-between items-center border-b p-4">
        <h2 class="text-xl font-semibold">Shopping cart</h2>
        <button @click="$emit('toggle-cart')" class="text-gray-500 hover:text-gray-700">
          <span class="text-xl">&times;</span>
        </button>
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
      <div class="border-t p-4">
        <div class="flex justify-between items-center mb-4">
          <span class="text-lg font-semibold">Total</span>
          <span class="text-lg font-semibold">$ {{ cartTotalPrice }}</span>
        </div>
        <button class="bg-yellow-400 text-white w-full py-2 rounded hover:bg-yellow-600">
          Checkout
        </button>
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

  const productStore = useProductStore();
  const cartProduct = computed(() => productStore.cartProducts);
  const cartTotalPrice = computed(() => productStore.totalCartPrice);

  const props = defineProps({
    shoppingCartToggle: {
      type: Boolean,
      required: true
    }
  });

  const addProduct = (product) => {
    productStore.addProductToCart(product);
  };
  
  const removeProduct = (productId) => {
    productStore.removeProductFromCart(productId)
  };
</script>
  