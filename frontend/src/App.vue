<template>
  <RouterView/>
</template>

<script setup>
  import { onMounted } from 'vue';
  import { RouterView } from "vue-router";
  import { useProductStore } from '@/stores/product';
  import { useHomeStore } from '@/stores/home'

  // Initialize the product store and home store
  const productStore = useProductStore()
  const homeStore = useHomeStore()

  /**
   * Fetch the list of products from the store when the component is mounted.
   * Fetch the home objects from the store when the component is mounted.
   */
  onMounted(async () => {
    await productStore.fetchProducts();
    await homeStore.fetchHome();
  })
</script>