<template>
  <div v-if="productsOnTrending" class="carousel-container px-72 py-16">
    <div class="text-center mb-8">
      <h2 class="text-3xl font-semibold">TRENDING NOW</h2>
      <p class="text-xl font-medium text-gray-500">
        Discover the trending dresses everyone loves. Explore now |
        <span class="border-b-2 border-b-gray-500">SHOP NOW</span>
      </p>
    </div>
    <div class="relative">
      <button
        class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-black text-white rounded-full shadow size-6 flex items-center justify-center z-10"
        @click="prev"
      >
        <span class="sr-only">Previous</span>
        <span class="block text-sm leading-none">&lsaquo;</span>
      </button>
      <div class="overflow-hidden">
        <ul
          class="flex transition-transform duration-500 ease-in-out"
          :style="{ transform: `translateX(-${(currentIndex * 100) / 5}%)` }"
        >
          <router-link
            :to="{ name: 'product', params: { product_ref: product.ref } }"
            v-for="product in productsOnTrending"
            :key="product.id"
            class="flex-none w-full sm:w-1/2 lg:w-1/5 px-2 cursor-pointer"
          >
            <div class="shadow">
              <img
                :src="product.gallery_urls[0]"
                :alt="product.product_detail.name"
                class="w-full object-cover mb-4"
              />
              <div class="text-center">
                <h3 class="text-lg font-semibold">
                  {{ product.product_detail.name }}
                </h3>
                <p class="text-lg font-semibold">
                  ${{ product.product_detail.price }}
                </p>
              </div>
            </div>
          </router-link>
        </ul>
      </div>
      <button
        class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-black text-white rounded-full shadow size-6 flex items-center justify-center z-10"
        @click="next"
      >
        <span class="sr-only">Next</span>
        <span class="block text-sm leading-none">&rsaquo;</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useProductStore } from "@/stores/product";

const productStore = useProductStore();
const currentIndex = ref(0);
const interval = ref(null);
const productsOnTrending = ref(null);

// Fetch products when component is mounted
onMounted(async () => {
  await productStore.fetchProducts();
  productsOnTrending.value = productStore.trendingProducts;
  startCarousel();
});

onUnmounted(() => {
  stopCarousel();
});

// Compute unique products to be displayed in the carousel

// Move to the next set of products in the carousel
const next = () => {
  if (currentIndex.value < Math.ceil(productsOnTrending.value.length / 5) - 1) {
    currentIndex.value++;
  } else {
    currentIndex.value = 0;
  }
};

// Move to the previous set of products in the carousel
const prev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  } else {
    currentIndex.value = Math.ceil(productsOnTrending.value.length / 5) - 1;
  }
};

// Start the automatic carousel rotation
const startCarousel = () => {
  interval.value = setInterval(() => {
    next();
  }, 3000);
};

// Stop the automatic carousel rotation
const stopCarousel = () => {
  if (interval.value) {
    clearInterval(interval.value);
  }
};
</script>
