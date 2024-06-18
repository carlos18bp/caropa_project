<template>
  <div
    v-if="visible"
    class="w-screen h-screen bg-gray-500 bg-opacity-40 backdrop-blur-md"
  >
    <div @click="closeModal" class="absolute inset-0"></div>
    <div class="relative z-50 bg-white shadow-lg w-full p-6">
      <div class="flex items-center justify-between border-b pb-4">
        <input
          type="text"
          class="w-full p-2 text-lg border-transparent focus:border-none focus:ring-0 focus:outline-none font-semibold"
          placeholder="Buscar..."
          v-model="searchQuery"
          @input="onSearch(searchQuery)"
        />
        <XMarkIcon
          @click="closeModal"
          class="h-6 w-6 cursor-pointer me-6 text-gray-500"
        ></XMarkIcon>
      </div>
      <div class="mt-4">
        <div class="grid grid-cols-3 gap-4">
          <!-- Suggestion items -->
          <RouterLink
            v-if="products"
            :to="{ name: 'product', params: { product_ref: product.ref } }"
            v-for="product in products"
            :key="products.id"
            class="flex items-center"
          >
            <img
              :src="product.gallery_urls[0]"
              alt="Product image"
              class="w-16 h-16 object-cover rounded"
            />
            <div class="ml-4">
              <p class="text-lg font-bold">{{ product.product_detail.name }}</p>
              <p class="text-sm text-gray-600">Item: {{ product.ref }}</p>
            </div>
          </RouterLink>
        </div>
        <div class="mt-4 text-right">
          <RouterLink :to="{ name: 'catalog' }" class="font-medium me-6"
            >See all products</RouterLink
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useProductStore } from "@/stores/product";
import { XMarkIcon } from "@heroicons/vue/24/outline";

const props = defineProps({
  visible: Boolean,
});
const emit = defineEmits(["update:visible"]);

const productStore = useProductStore();
const products = ref([]);
const searchQuery = ref(null);

const closeModal = () => {
  emit("update:visible", false);
  products.value = [];
  searchQuery.value = null;
};

const onSearch = (name) => {
  if (name !== "") {
    products.value = productStore.productsByName(name);
  }
};

onMounted(async () => {
  await productStore.fetchProducts();
});
</script>
